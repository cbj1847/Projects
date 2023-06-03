from flask import Blueprint, request, render_template, session, redirect, flash
import numpy as np
import pandas as pd
import hashlib, base64, json

health_bp1 = Blueprint('health_bp1', __name__)

def age_gen(a) :
    age_12 = 123 - int(str(a)[:2])
    age_34 = 23 - int(str(a)[:2])
    if str(a)[-1] == '1':
        return '남성', age_12
    elif str(a)[-1] == '2':
        return '여성', age_12
    elif str(a)[-1] == '3':
        return '남성', age_34
    else:
        return '여성', age_34

@health_bp1.route('/body', methods=['GET', 'POST'])
def age():
    male = [{'연령': '20~24세', '비율': 1.8},{'연령': '25~29세', '비율': 6.63},{'연령': '30~34세', '비율': 9.28},
            {'연령': '35~39세', '비율': 11.27},{'연령': '40~44세', '비율': 12.63},{'연령': '45~49세', '비율': 11.71},
            {'연령': '50~54세', '비율': 12.38},{'연령': '55~59세', '비율': 10.51},{'연령': '60~64세', '비율': 9.76},
            {'연령': '65~69세', '비율': 5.37},{'연령': '70~74세', '비율': 4.71},{'연령': '75~79세', '비율': 2.37},
            {'연령': '80~84세', '비율': 1.33},{'연령': '85세+', '비율': 0.23}]   
    female = [{'연령': '20~24세', '비율': 2.53},{'연령': '25~29세', '비율': 6.43},{'연령': '30~34세', '비율': 5.99},
              {'연령': '35~39세', '비율': 5.75},{'연령': '40~44세', '비율': 11.8},{'연령': '45~49세', '비율': 11.33},
            {'연령': '50~54세', '비율': 14.05},{'연령': '55~59세', '비율': 11.87},{'연령': '60~64세', '비율': 11.87},
            {'연령': '65~69세', '비율': 6.37},{'연령': '70~74세', '비율': 6.0},{'연령': '75~79세', '비율': 3.35},
            {'연령': '80~84세', '비율': 2.12},{'연령': '85세+', '비율': 0.55}]
    if request.method == 'GET':
        return render_template('my_body.html',)
    else:
        jm = int(request.values["jm"])
        gender = age_gen(jm)[0]
        age = age_gen(jm)[1]
        b=1
        for i, j in zip(np.arange(20, 100, 5),   np.arange(24, 104, 5)):
            if i <= age <= j:
                break
            else:
                b = b + 1
        if gender == '남성':    
            return render_template('my_body.html', age_list = male, age=str(age), gender=gender, b=b)
        elif gender == '여성':
            return render_template('my_body.html', age_list = female, age=str(age), gender=gender, b=b)

