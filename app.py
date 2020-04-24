from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "madmadmadlibs"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/story_form/<story_name>')
def madlib_form(story_name):
    madlib = story_dict[story_name]
    title = madlib.title
    prompts = madlib.prompts
    img = madlib.img
    return render_template("story_form.html", title=title, prompts=prompts, story_name=story_name, img=img)

@app.route('/story_txt/<story_name>')
def mablib_text(story_name):
    madlib = story_dict[story_name]
    title = madlib.title
    img = madlib.img
    answers = request.args
    mad_dict = answers.to_dict()
    madstory = madlib.generate(mad_dict)
    return render_template("story_txt.html", madstory=madstory, title=title, img=img)