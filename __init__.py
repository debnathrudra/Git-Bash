from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
    if _name_ == "_main_":
        app.run(debug=True)
        