from flask import render_template
import datetime
import json

name_web = "MyKala"
date = datetime.datetime.now().year

def home_page():
    return(render_template("home.html", name=name_web,date=date))

def shopping():
    return ''