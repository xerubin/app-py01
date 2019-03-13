from flask import Flask
application = Flask(__name__)

@application.route("/hola")
def hello():
    return "Hola OPENSHIFT desde Python!"

if __name__ == "__main__":
    application.run()
