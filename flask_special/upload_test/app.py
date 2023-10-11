from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    # 对文件进行处理或存储逻辑
    file.save('/root/upload_test/upload/mn.png')

    return 'File uploaded successfully.'
@app.route('/')
def index():
    return render_template('1.html')
if __name__ == '__main__':
    app.run()
