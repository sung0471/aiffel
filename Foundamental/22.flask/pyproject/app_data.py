from flask import Flask, render_template, request
import os
import sqlite3
import pandas as pd


app = Flask(__name__)

'''
DB 함수
'''
# DB 연결을 위한 함수
def get_db(db_name):
    return sqlite3.connect(db_name)

# SQL 쿼리를 이용해 DB에 요청하기 위한 함수
def sql_command(conn, command):
    # try 내부의 코드가 정상적으로 동작하면, try 내부 코드만 실행됨
    try:

        conn.execute(command)
        conn.commit()
        command = command.lower()   # 명령어를 소문자로 바꿈

        if "select" in command:     # 쿼리가 select인 경우

            command_split = command.split(" ")
            select_command = "SELECT * FROM " + command_split[command_split.index("from")+1]

            # conn에 담긴 DB에 연결하여 select_command 쿼리를 수행함
            # 수행한 결과를 DataFrame 타입으로 변환해 df에 저장
            df = pd.read_sql(select_command, conn, index_col=None)
            html = df.to_html()

            conn.close()

            return html

        conn.close()

        return True
    # try 내부 코드 실행 중 오류 발생 시, except 내부 코드 실행
    except :

        conn.close()

        return False


'''
File upload
'''
@app.route("/index")
def index():
    return render_template('data.html')

# data.html의 form에서 /dbsql로 POST 전송요청이 오면
# 아래의 함수로 라우팅(경로를 설정)하여 실행해줌
@app.route('/dbsql', methods=['POST'])
def sql_processing():
    if request.method == 'POST':

        # form의 db_name이라고 된 이름의 UI 컴포넌트에 있는 값으로
        # DB 연결하는 connection 객체를 생성
        con = get_db(request.form.get('db_name'))
        sql = request.form.get('sql')
        # True, False, 코드 중 하나 반환
        result_sql = sql_command(con, sql)

        if result_sql == False :
            return render_template('data.html', label="비정상")

        elif result_sql == True :
            return render_template('data.html', label="정상 작동")

        else :
            result_sql = "<html><body> " + result_sql + "</body></html>"
            return result_sql


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000))

"""
- DB 만들기
create table if not exists 도서대출내역
(ID, varchar, 이름 varchar, 도서ID varchar, 대출일 varchar, 반납일 varchar)

- DB에 데이터 추가
insert into 도서대출내역 (ID, 이름, 도서ID, 대출일, 반납일) VALUES('101', '문강태', 'aaa', '2020-06-01', '2020-06-05'), ('101', '문강태', 'ccc', '2020-06-20', '2020-06-25')

- DB table의 데이터 확인
select * from 도서대출내역
"""
