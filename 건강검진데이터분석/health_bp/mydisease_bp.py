from flask import Blueprint, request, render_template, session, redirect, flash
import numpy as np
import pandas as pd
import math
import hashlib, base64, json
from health_bp.bp_util import su_bp5, su_bp6, su_bp7, su_bp8,su_bp9,su_bp10,su_bp11,su_bp12,su_bp13,su_bp14,su_bp15,su_bp16,su_bp17,su_bp18
from health_bp.bp_util import iw_bp5, iw_bp6, iw_bp7, iw_bp8,iw_bp9,iw_bp10,iw_bp11,iw_bp12,iw_bp13,iw_bp14,iw_bp15,iw_bp16,iw_bp17,iw_bp18
from health_bp.bp_util import gbhd5, gbhd6, gbhd7, gbhd8,gbhd9,gbhd10,gbhd11,gbhd12,gbhd13,gbhd14,gbhd15,gbhd16,gbhd17,gbhd18
from health_bp.bp_util import tg_list, hdl_list, ldl_list, tdl_list
health_bp2 = Blueprint('health_bp2', __name__)

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

# 연령대/성별 비율 출력 
@health_bp2.route('/disease', methods=['GET', 'POST'])
def disease():
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
        return render_template('my_disease.html',)
    else:
        # 웹에서 입력받은 값 요청
        try:
            jm = int(request.values["jm"])
            bp1 = int(request.values["bp1"])
            bp2 = int(request.values["bp2"])
            bs = int(request.values["bs"])
            tg = int(request.values["tg"])
            hdl = int(request.values["hdl"])
            ldl = int(request.values["ldl"])
            hg = int(request.values["hg"])
            up = int(request.values["up"])
            bc = int(request.values["bc"])
            gpt = int(request.values["gpt"])
            ast = int(request.values["ast"])
            alt = int(request.values["alt"])
        except:
            pass
        
        # 입력받은 주민번호 토대로 성별/나이 판별
        gender = age_gen(jm)[0]
        age = age_gen(jm)[1]
        
        # 사용자의 연령대에 해당하는 컬럼을 찾기 위한 판별식
        b=1
        for i, j in zip(np.arange(20, 100, 5), np.arange(24, 104, 5)):
            if i <= age <= j:
                break
            else:
                b = b + 1
        # 사용자의 혈압에 해당하는 컬럼을 찾기 위한 판별식
        sc_range1 = [0, 110, 115, 120, 125, 130, 135, 140, 145, 150]
        sc_range2 = [110, 115, 120, 125, 130, 135, 140, 145, 150, 1000]
        c=1
        for i, j in zip(sc_range1, sc_range2):
            if i <= bp1 < j:
                break
            else:
                c = c + 1
        iw_range1 = [0,  60,  65,  70,  75,  80,  85,  90,  95, 100]
        iw_range2 = [60,  65,  70,  75,  80,  85,  90,  95, 100, 1000]
        d=1
        for i, j in zip(iw_range1, iw_range2):
            if i <= bp2 < j:
                break
            else:
                d = d + 1
        # 고혈압 건강 연령대
        e = math.floor((c+d)/2)
        e = male[e-1]['연령']
        # 공복혈당 컬럼 찾기용
        bs_1 = [0,  100,  126]
        bs_2 = [100,  126,  10000]
        f=1
        for i, j in zip(bs_1, bs_2):
            if i <= bs < j:
                break
            else:
                f = f + 1
        # 고혈압 건강 연령대
        g = male[f-1]['연령']

        # 연령대별 수축기/이완기혈압 비율 테이블 찾기
        subp = [su_bp5, su_bp6, su_bp7, su_bp8,su_bp9,su_bp10,su_bp11,su_bp12,su_bp13,su_bp14,su_bp15,su_bp16,su_bp17,su_bp18][b]
        iwbp = [iw_bp5, iw_bp6, iw_bp7, iw_bp8,iw_bp9,iw_bp10,iw_bp11,iw_bp12,iw_bp13,iw_bp14,iw_bp15,iw_bp16,iw_bp17,iw_bp18][b]
        gbhd = [gbhd5, gbhd6, gbhd7, gbhd8,gbhd9,gbhd10,gbhd11,gbhd12,gbhd13,gbhd14,gbhd15,gbhd16,gbhd17,gbhd18][b]
        # 연령대 평균 수축기 혈압
        scg_bp = [115, 117, 119, 120, 120, 121, 123, 124, 126, 128, 130, 131, 132,131]
        iwg_bp = [71, 72, 74, 76, 76, 77, 77, 77, 77, 77, 76, 76, 76, 75]

        #고혈압 유병자 판별
        if bp1 >= 140 or bp2 >= 90:
            gha = '이며,'
        else:
            gha = '가 아니며,'
        #당뇨병 유병자 판별
        if bs >= 126:
            dnb = '입니다.'
        else:
            dnb = '가 아닙니다.'
        # 트리글리세라이드, hdl, ldl 연령대 평균수치
        tgsval, hdlval, ldlval, tdlval = tg_list[b], hdl_list[b], ldl_list[b], tdl_list[b]
        # 이상지질혈증 유병자 판별
        if tg >= 200 or hdl < 40 or ldl >= 160 or hdl+ldl >= 240:
            ejh = '입니다.' 
        else:
            ejh = '가 아닙니다.'

        if gender == '남성':    
            return render_template('my_disease_res.html', age_list = male, age=str(age), gender=gender, b=b, scg=scg_bp[b], iwg=iwg_bp[b],
                gha = gha, su_list = subp, iw_list = iwbp, c=c, d=d, e=e, gbhd_list=gbhd, f=f, dnb=dnb, g=g, tgsval=tgsval, hdlval=hdlval, ldlval=ldlval,
                tdlval=tdlval, ejh = ejh)
        elif gender == '여성':
            return render_template('my_disease_res.html', age_list = female, age=str(age), gender=gender, b=b, scg=scg_bp[b], iwg=iwg_bp[b],
                gha = gha, su_list = subp, iw_list = iwbp, c=c, d=d, e=e, gbhd_list=gbhd, f=f, dnb=dnb, g=g, tgsval=tgsval, hdlval=hdlval, ldlval=ldlval,
                tdlval=tdlval, ejh = ejh)

# 혈압 비율        
@health_bp2.route('/disease', methods=['GET', 'POST'])
def blood_pressure():
    pass
