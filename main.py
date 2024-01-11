

from flask import Flask, render_template, Response
import pygame
#import cv2
import numpy as np

app = Flask(__name__)

# Initialize Pygame
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

def generate_frame():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        # Replace this with your Pygame graphics code
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (width // 2, height // 2), 50)

        _, buffer = cv2.imencode('.jpg', pygame.surfarray.array3d(screen))
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

