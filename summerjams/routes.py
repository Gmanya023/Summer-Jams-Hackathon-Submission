from flask import render_template, url_for, send_from_directory, redirect
from summerjams import app
from summerjams.forms import UploadForm
from werkzeug.utils import secure_filename
import os
import pathlib
import io
from summerjams.create_music import process_labels
from summerjams.create_music import sound_manipulation
from summerjams.create_music import nameGenerator
from keypath import keypath


@app.route("/", methods=["GET", "POST"])
def main():
    form = UploadForm()
    return render_template("main.html", form=form)

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)

@app.route("/play", methods=["GET", "POST"])
def play():
    print("hello")
    form = UploadForm()
    print(form.validate_on_submit())
    print(form.base.data)
    name = ""
    if form.validate_on_submit():
        f = form.upload.data
        filename = secure_filename(f.filename)
        folder = app.config['UPLOAD_FOLDER']
        pathlib.Path(folder).mkdir(exist_ok=True)
        # Creates if the folder if it doesn't exist
        f.save(os.path.join(folder, filename))
        # This saves the file to the designated upload folder
        name = vision_api_call(filename, form.base.data)

    if name == "":
        return redirect("/")

    return render_template("player.html", music=name)

def vision_api_call(filename, theme_type):
    from google.cloud import vision
    from google.cloud.vision import types
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(keypath,'key.json')
    client = vision.ImageAnnotatorClient()
    file = os.path.abspath(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    with io.open(file, 'rb') as loaded_image:
        content = loaded_image.read()
    image_file = types.Image(content=content)
    response = client.label_detection(image = image_file)
    labels_received = response.label_annotations
    labels = []
    for value in labels_received:
        labels.append(value.description)

    # calling the process labels function
    sounds = process_labels(labels)
    # user selection of music: acoustic, piano or electronic
    file = sound_manipulation(theme_type, sounds)

    print(file)

    return file
    
