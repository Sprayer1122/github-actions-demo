from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!" #this is the new era

if __name__ == '__main__':
    app.run(debug=True)
