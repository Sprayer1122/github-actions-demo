from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! this is the era" 


#comment
if __name__ == '__main__':
    app.run(debug=True)
