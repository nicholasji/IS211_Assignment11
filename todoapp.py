#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Week 11


from flask import Flask, redirect, render_template, request
import re


app = Flask(__name__)

todol = []


@app.route('/')
def index():
    return render_template('index.html', todol=todol)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['Task']
    priority = request.form['Priority']
    email = request.form['Email']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif not task:
        return redirect('/')
    elif priority == 'Priority Level':
        return redirect('/')
    else:
        todol.append((task, priority, email))

    print todol
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    del todol[:]
    return redirect('/')


if __name__ == '__main__':
    app.run()
