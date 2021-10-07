from io import BytesIO
from PIL import Image, ImageFilter
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/gallery/")
def gallery():
    return """
    <div>
    <img src='/?resize=10&blur=1' />
    <img src='/?resize=2&blur=0' />
    </div>
    """

@app.route("/", methods=['GET'])
def howdy_world():
    img_io = BytesIO()
    filename = "slc.jpg"
    im = Image.open(filename)

    # operations to run on the final img
    resize_multiplier = int(request.args.get('resize', 1))
    blur = request.args.get('blur', False)
    if blur:
        if int(blur) > 0:
            blur = True

    im = im.resize((im.width // resize_multiplier, im.height // resize_multiplier))
    if blur:
        im = im.filter(ImageFilter.BLUR)

    im.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)


    return send_file(img_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)