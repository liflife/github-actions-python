from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"


if __name__ == "__main__":
    print("run hello")
    app.run()
    
