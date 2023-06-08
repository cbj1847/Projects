from flask import Blueprint, request, render_template, session, redirect, flash
import db_sqlite.user_dao as udao
import datetime

screening_output = Blueprint('screening_output', __name__)

@screening_output.route('/output', methods=['GET', 'POST'])
def scr_output():
    if request.method == 'GET':
        return render_template('screening_output.html')
    else :
        if request.values["uid"]:
            uid = request.values["uid"]
            screening_list = udao.get_disease(uid)
            return render_template('screening_output.html', scr_list = screening_list)
        else :
            flash('로그인 후 이용해주세요.')
            return redirect('/')