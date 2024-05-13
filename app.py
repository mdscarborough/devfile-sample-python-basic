from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!\n\n\nThis Page Was Created by MScarborough Using a Sample Project and Then Modifying It!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
