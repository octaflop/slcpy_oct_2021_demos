from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def howdy_world():
    greeting = request.args.get('greeting', 'Howdy')

    return f"<h1>{greeting} World! 🤠</h1>"
