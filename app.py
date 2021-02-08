from flask import Flask, render_template
import sys
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("hello.html")

@application.route("/list")
def list():
    return render_template("list.html")

@application.route("/apply")
def apply():
    return render_template("apply.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5002)