from flask import Blueprint
from flask import Flask,render_template
from simpledu.models import Course

front = Blueprint('front',__name__)

@front.route('/')
def index():
	courses = Course.query.all()
	return render_template('index.html',courses=courses)
	