from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    print("Hello world log console")
    return 'Hello World from Python Flask!'

app.run(host='0.0.0.0', port=4444)
