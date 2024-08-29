from flask import Flask, Response
import cv2

app = Flask(__name__)

def generate_frames():
    cap = cv2.VideoCapture(0)  # Mở camera mặc định
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Encode frame dưới dạng JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Trả về frame dưới dạng luồng dữ liệu
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    #Lấy địa chỉ tại ipconfig của máy tính
    app.run(host='0.0.0.0', port=5000)
