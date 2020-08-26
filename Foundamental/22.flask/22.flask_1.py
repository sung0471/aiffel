from flask import Flask     # flask 패키지에서 Flask 모듈 가져옴
import datetime

app = Flask(__name__)       # Flask 객체가 생성됨, app 변수에 할당


@app.route('/')
# @로 시작하는 코드 : 데코레이터(decorator)
# http://IP:(port_number) + '/' 라는 주소로 접근하면 아래 함수를 실행하게 함
def hello():
    return '플라스크 동작 확인!'


# 코드 선언부
def datetime_decorator(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated


@datetime_decorator
def main_function():
    print ("test function")


# 코드 실행부
main_function()


if __name__ == '__main__':
    app.run()