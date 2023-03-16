from flask import Flask, jsonify, request
from process_image import get_emotion

classes = {
    'neutral': 0,
    'happy': 1,
    'sad': 2,
    'surprised': 3,
    'fearful': 4,
    'disgusted': 5,
    'angry': 6,
    'contempt': 7
}

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/')
def index():
    return jsonify({'message': 'Backend is working!'})

@app.route('/image', methods=['POST'])
def image():
    image = request.files['image']
    emotion = get_emotion(image)
    return jsonify({'emotion': emotion})


if __name__ == '__main__':
    app.run()