from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "est"

@app.route("/ata")
def test():
    return "test"

if __name__ == '__main__':
    app.run()