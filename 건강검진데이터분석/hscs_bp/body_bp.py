from flask import Blueprint, request, render_template, session, redirect, flash

hscs_body = Blueprint('hscs_body', __name__)

@hscs_body.route('/height')
def barchart():
    return render_template('hscs_body/신체.html')

@hscs_body.route('/weight')
def barchart_2():
    return render_template('hscs_body/체중.html',)


@hscs_body.route('/obsesity')
def barchart_6():
    return render_template('hscs_body/비만율.html' )

@hscs_body.route('/waist')
def barchart_3():
    return render_template('hscs_body/허리.html' )

@hscs_body.route('/obsesity2')
def barchart_7():
    return render_template('hscs_body/복부비만.html' )

@hscs_body.route('/sight')
def barchart_4():
    return render_template('hscs_body/시력.html' )

@hscs_body.route('/hearing')
def barchart_5():
    return render_template('hscs_body/청력.html' )