from flask import Flask, render_template, Response
import cv2
import threading

app = Flask(__name__)

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.lock = threading.Lock()

    def __del__(self):
        self.camera.release()

    def get_frame(self):
        success, frame = self.camera.read()
        if not success:
            return None
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        return frame

def generate_frames(camera):
    while True:
        frame = camera.get_frame()
        if frame is None:
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    camera = Camera()
    return Response(generate_frames(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/me')
def Show_me():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
