from flask import Flask

app = Flask(__name__)


@app.route("/")
def howdy_world():
    return "<h1>Howdy World! 🤠</h1>"

# How do we combine the two (eg with Pillow)?