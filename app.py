from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Retrieve an environment variable, useful for CI/CD testing
    message = os.environ.get('APP_MESSAGE', 'Hello World from Flask! CI/CD Test v1.0')
    return f"<h1>{message}</h1>"

if __name__ == '__main__':
    # Run the application on all interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
