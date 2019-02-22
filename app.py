from flask import Flask, render_template
import tweet_gen as t
import clean_text as c 
import random

app = Flask(__name__)


@app.route('/')
def index():
    start = t.Markov(c.clean_up_text('queen_reign.txt'))
    start.getting_types()
    start.logic()
    sentence = start.multiple_runs(random.randint(5 , 15))

    return render_template("index.html", title=None, sentence=sentence)




