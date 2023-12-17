from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
camera_indices = [0,1] 

# def generate_frames():
#     cameras = [cv2.VideoCapture(index) for index in camera_indices]
    
#     while True:
#         frames = [cap.read()[1] for cap in cameras]
#         # frames = [cv2.resize(frame, (400, 300)) for frame in frames]  # Optional: Resize frames for consistent display
#         ret, buffer = cv2.imencode('.jpg', cv2.hconcat(frames))
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
def generate_frames_me():
    camera = cv2.VideoCapture(0) 
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames_me(), mimetype='multipart/x-mixed-replace; boundary=frame')    
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/me')
def Show_me():
    return render_template('index.html')
# @app.route('/all')
# def Show_all():
#     return render_template('allCams.html')

# @app.route('/all_video')
# def video_feed_all():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(debug=True)
