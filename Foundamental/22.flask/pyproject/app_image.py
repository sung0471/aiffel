from flask import Flask, render_template, request
import os
from PIL import Image


app = Flask(__name__)

'''
이미지 처리 함수
'''
# 이미지 사이즈 변환 함수
# 높이, 너비를 둘 다 입력하여 변환
def image_resize(image, width, height):
        return image.resize((int(width), int(height)))

# 이미지를 180도 회전
def image_rotate(image):
    return image.transpose(Image.ROTATE_180)

# 이미지 색공간을 흑백으로 바꿈
def image_change_bw(image):
    return image.convert('L')


'''
플라스크
'''
@app.route("/index")
def index():
    return render_template('image.html')

# HTML에서 설정한 라우팅 경로
@app.route('/image_preprocess', methods=['POST'])
def preprocessing():
    if request.method == 'POST':
        file = request.files['uploaded_image']
        if not file: return render_template('index.html', label="No Files")

        # PIL.Image를 이용해 이미지 로드
        img = Image.open(file)

        is_rotate_180 = request.form.get('pre_toggle_0')
        is_change_bw = request.form.get('pre_toggle_1')
        is_change_size = request.form.get('pre_toggle_2')

        if is_rotate_180 == 'on':
            img = image_rotate(img)

        if is_change_bw == 'on':
            img = image_change_bw(img)

        if is_change_size == 'on':
            img = image_resize(img,
                               request.form.get('changed_width'), request.form.get('changed_height'))

        img.save('result_image.png')

        src_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(src_dir, 'result_image.png')

        # 결과 리턴
        return render_template('image.html', label=image_path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000))
