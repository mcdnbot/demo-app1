from flask import Flask,render_template
import socket

app = Flask(__name__)

@app.route('/')
def index():
  local_ip = socket.gethostbyname(socket.gethostname())
  return render_template('index.html', ip=local_ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
