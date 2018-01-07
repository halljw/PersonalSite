#!/usr/bin/env python

from flask import Flask, render_template, request
from flask import send_file

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/resume')
def resume():
  return render_template('resume.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')

@app.route('/blog')
def blog():
  return render_template('blog.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/text_analyzer')
def text_analyzer():
  return render_template('text_analyzer.html')

@app.route('/resume.pdf')
def resume_pdf():
  return send_file('Documents/Hall_John_Resume.pdf')

if __name__=="__main__":
  app.run(debug=True)
