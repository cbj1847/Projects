from flask import Blueprint, request, render_template, session, redirect, flash
import numpy as np
import pandas as pd
import math
import hashlib, base64, json
from health_bp.bp_util import su_bp5, su_bp6, su_bp7, su_bp8,su_bp9,su_bp10,su_bp11,su_bp12,su_bp13,su_bp14,su_bp15,su_bp16,su_bp17,su_bp18
from health_bp.bp_util import iw_bp5, iw_bp6, iw_bp7, iw_bp8,iw_bp9,iw_bp10,iw_bp11,iw_bp12,iw_bp13,iw_bp14,iw_bp15,iw_bp16,iw_bp17,iw_bp18
from health_bp.bp_util import gbhd5, gbhd6, gbhd7, gbhd8,gbhd9,gbhd10,gbhd11,gbhd12,gbhd13,gbhd14,gbhd15,gbhd16,gbhd17,gbhd18
from health_bp.bp_util import tgdict5, tgdict6, tgdict7, tgdict8,tgdict9,tgdict10,tgdict11,tgdict12,tgdict13,tgdict14,tgdict15,tgdict16,tgdict17,tgdict18
from health_bp.bp_util import hdldict5, hdldict6, hdldict7, hdldict8,hdldict9,hdldict10,hdldict11,hdldict12,hdldict13,hdldict14,hdldict15,hdldict16,hdldict17,hdldict18
from health_bp.bp_util import ldldict5, ldldict6, ldldict7, ldldict8,ldldict9,ldldict10,ldldict11,ldldict12,ldldict13,ldldict14,ldldict15,ldldict16,ldldict17,ldldict18
from health_bp.bp_util import ttcdict5, ttcdict6, ttcdict7, ttcdict8,ttcdict9,ttcdict10,ttcdict11,ttcdict12,ttcdict13,ttcdict14,ttcdict15,ttcdict16,ttcdict17,ttcdict18
from health_bp.bp_util import hgdict_male5, hgdict_male6, hgdict_male7, hgdict_male8,hgdict_male9,hgdict_male10,hgdict_male11,hgdict_male12,hgdict_male13,hgdict_male14,hgdict_male15,hgdict_male16,hgdict_male17,hgdict_male18
from health_bp.bp_util import hgdict_female5, hgdict_female6, hgdict_female7, hgdict_female8,hgdict_female9,hgdict_female10,hgdict_female11,hgdict_female12,hgdict_female13,hgdict_female14,hgdict_female15,hgdict_female16,hgdict_female17,hgdict_female18
from health_bp.bp_util import ydbdict5, ydbdict6, ydbdict7, ydbdict8,ydbdict9,ydbdict10,ydbdict11,ydbdict12,ydbdict13,ydbdict14,ydbdict15,ydbdict16,ydbdict17,ydbdict18
from health_bp.bp_util import ast5, ast6, ast7, ast8,ast9,ast10,ast11,ast12,ast13,ast14,ast15,ast16,ast17,ast18
from health_bp.bp_util import alt5, alt6, alt7, alt8,alt9,alt10,alt11,alt12,alt13,alt14,alt15,alt16,alt17,alt18
from health_bp.bp_util import gtp_male5, gtp_male6, gtp_male7, gtp_male8,gtp_male9,gtp_male10,gtp_male11,gtp_male12,gtp_male13,gtp_male14,gtp_male15,gtp_male16,gtp_male17,gtp_male18
from health_bp.bp_util import gtp_female5, gtp_female6, gtp_female7, gtp_female8,gtp_female9,gtp_female10,gtp_female11,gtp_female12,gtp_female13,gtp_female14,gtp_female15,gtp_female16,gtp_female17,gtp_female18
from health_bp.bp_util import hcc5, hcc6, hcc7, hcc8,hcc9,hcc10,hcc11,hcc12,hcc13,hcc14,hcc15,hcc16,hcc17,hcc18, ast_aged, alt_aged, gtp_female_aged
from health_bp.bp_util import tg_list, hdl_list, ldl_list, tdl_list, male, female, hg_male_list, hg_female_list, ydb_abnormal, gtp_male_aged
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
    if request.method == 'GET':
        return render_template('my_disease.html',)
    else:
        # 웹에서 입력받은 값 요청 / 사용자가 입력안할시 0으로 출력
        jm = int(request.values["jm"]) if (request.values["jm"]) != '' else 0
        bp1 = int(request.values["bp1"]) if (request.values["bp1"]) != '' else 0
        bp2 = int(request.values["bp2"]) if (request.values["bp2"]) != '' else 0
        bs = int(request.values["bs"]) if (request.values["bs"]) != '' else 0
        tg = int(request.values["tg"]) if (request.values["tg"]) != '' else 0
        hdl = int(request.values["hdl"]) if (request.values["hdl"]) != '' else 0
        ldl = int(request.values["ldl"]) if (request.values["ldl"]) != '' else 0
        hg = int(request.values["hg"]) if (request.values["hg"]) != '' else 0
        up = int(request.values["up"]) if (request.values["up"]) != '' else 0
        bc = int(request.values["bc"]) if (request.values["bc"]) != '' else 0
        gtp = int(request.values["gpt"]) if (request.values["gpt"]) != '' else 0
        ast = int(request.values["ast"]) if (request.values["ast"]) != '' else 0
        alt = int(request.values["alt"]) if (request.values["alt"]) != '' else 0
        
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
        
        # 공복혈당 건강 연령대
        g = male[f-1]['연령']
       
        # 트리글리세라이드 컬럼 찾기용
        h=1
        tg_1 = [0,  150,  200]
        tg_2 = [150,  200,  10000]
        for i, j in zip(tg_1, tg_2):
            if i <= tg < j:
                break
            else:
                h = h + 1
        
        # HDL 컬럼 찾기용
        hdlc=1
        hdl_1 = [0,  40,  60]
        hdl_2 = [40,  60,  10000]
        for m, n in zip(hdl_1, hdl_2):
            if m <= hdl < n:
                break
            else:
                hdlc = hdlc + 1        
        
        # LDL 컬럼 찾기용
        ldlc=1
        ldl_1 = [0,  130,  160]
        ldl_2 = [130,  160,  10000]
        for m, n in zip(ldl_1, ldl_2):
            if m <= ldl < n:
                break
            else:
                ldlc = ldlc + 1
        
        # 총콜레스테롤 컬럼 찾기용
        k=1
        ttc_1 = [0,  200,  240]
        ttc_2 = [200,  240,  10000]
        for m, n in zip(ttc_1, ttc_2):
            if m <= ldl+hdl < n:
                break
            else:
                k = k + 1
        
        # 성별 갈리는거 판별용
        l=1
        hgdict_male_list = [hgdict_male5, hgdict_male6, hgdict_male7, hgdict_male8,hgdict_male9,hgdict_male10,hgdict_male11,hgdict_male12,hgdict_male13,hgdict_male14,hgdict_male15,hgdict_male16,hgdict_male17,hgdict_male18][b]
        hgdict_female_list = [hgdict_female5, hgdict_female6, hgdict_female7, hgdict_female8,hgdict_female9,hgdict_female10,hgdict_female11,hgdict_female12,hgdict_female13,hgdict_female14,hgdict_female15,hgdict_female16,hgdict_female17,hgdict_female18][b]
        gtp_male_list = [gtp_male5, gtp_male6, gtp_male7, gtp_male8,gtp_male9,gtp_male10,gtp_male11,gtp_male12,gtp_male13,gtp_male14,gtp_male15,gtp_male16,gtp_male17,gtp_male18][b]
        gtp_female_list = [gtp_female5, gtp_female6, gtp_female7, gtp_female8,gtp_female9,gtp_female10,gtp_female11,gtp_female12,gtp_female13,gtp_female14,gtp_female15,gtp_female16,gtp_female17,gtp_female18][b]
        if gender == '남성':
            hg_1 = [0,  13,  17.5]
            hg_2 = [13,  17.5,  10000]
            hgval = hg_male_list[b]
            gtpval = gtp_male_aged[b]
            age_list = male
            hgdict_list = hgdict_male_list
            gtp_list = gtp_male_list
            # 혈색소 컬럼찾기용
            for m, n in zip(hg_1, hg_2):
                if m <= hg < n:
                    break
                else:
                    l = l + 1
            # gtp 컬럼 찾기용
            q=1
            gtp_1 = [-10,  63]
            gtp_2 = [63,  10000]
            for i, j in zip(gtp_1, gtp_2):
                if i < gtp <= j:
                    break
                else:
                    q = q + 1
        elif gender == '여성':
            hg_female_1 = [0,  12,  15.5]
            hg_female_2 = [12,  15.5,  10000]
            gtpval = gtp_female_aged[b]
            hgval = hg_female_list[b]
            age_list = female
            hgdict_list = hgdict_female_list
            gtp_list = gtp_female_list
            # 혈색소 컬럼찾기용
            for m, n in zip(hg_female_1, hg_female_2):
                if m <= hg < n:
                    break
                else:
                    l = l + 1
            # gtp 컬럼 찾기용
            q=1
            gtp_1 = [-10,  35]
            gtp_2 = [35,  10000]
            for i, j in zip(gtp_1, gtp_2):
                if i < gtp <= j:
                    break
                else:
                    q = q + 1 

        # 요단백 컬럼 찾기용
        m=1
        for i in range(1, 7):
            if i == up:
                break
            else:
                m = m + 1
        # 혈청크레아티닌 컬럼 찾기용
        n=1
        hcc_1 = [0,  12,  15.5]
        hcc_2 = [12,  15.5,  10000]
        for i, j in zip(hcc_1, hcc_2):
            if i <= bc < j:
                break
            else:
                n = n + 1
        # AST 컬럼 찾기용
        o=1
        ast_1 = [-10,  40]
        ast_2 = [40,  10000]
        for i, j in zip(ast_1, ast_2):
            if i < ast <= j:
                break
            else:
                o = o + 1
        # ALT 컬럼 찾기용
        p=1
        alt_1 = [-10,  40]
        alt_2 = [40,  10000]
        for i, j in zip(alt_1, alt_2):
            if i < alt <= j:
                break
            else:
                p = p + 1   

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
        # 연령대 평균수치
        tgsval, hdlval, ldlval, tdlval = tg_list[b], hdl_list[b], ldl_list[b], tdl_list[b]
        tgs_list = [tgdict5, tgdict6, tgdict7, tgdict8,tgdict9,tgdict10,tgdict11,tgdict12,tgdict13,tgdict14,tgdict15,tgdict16,tgdict17,tgdict18][b]
        hdldict_list = [hdldict5, hdldict6, hdldict7, hdldict8,hdldict9,hdldict10,hdldict11,hdldict12,hdldict13,hdldict14,hdldict15,hdldict16,hdldict17,hdldict18][b]
        ldldict_list = [ldldict5, ldldict6, ldldict7, ldldict8,ldldict9,ldldict10,ldldict11,ldldict12,ldldict13,ldldict14,ldldict15,ldldict16,ldldict17,ldldict18][b]
        ttcdict_list = [ttcdict5, ttcdict6, ttcdict7, ttcdict8,ttcdict9,ttcdict10,ttcdict11,ttcdict12,ttcdict13,ttcdict14,ttcdict15,ttcdict16,ttcdict17,ttcdict18][b]
        ydbdict_list = [ydbdict5, ydbdict6, ydbdict7, ydbdict8,ydbdict9,ydbdict10,ydbdict11,ydbdict12,ydbdict13,ydbdict14,ydbdict15,ydbdict16,ydbdict17,ydbdict18][b]
        ast_list = [ast5, ast6, ast7, ast8,ast9,ast10,ast11,ast12,ast13,ast14,ast15,ast16,ast17,ast18][b]
        alt_list = [alt5, alt6, alt7, alt8,alt9,alt10,alt11,alt12,alt13,alt14,alt15,alt16,alt17,alt18][b]
        hcc_list = [hcc5, hcc6, hcc7, hcc8,hcc9,hcc10,hcc11,hcc12,hcc13,hcc14,hcc15,hcc16,hcc17,hcc18][b]

        # 이상지질혈증 유병자 판별
        if tg >= 200 or hdl < 40 or ldl >= 160 or hdl+ldl >= 240:
            ejh = '입니다.' 
        else:
            ejh = '가 아닙니다.'
    
        return render_template('my_disease_res.html', age_list = age_list, age=str(age), gender=gender, b=b, scg=scg_bp[b], iwg=iwg_bp[b],
            gha = gha, su_list = subp, iw_list = iwbp, c=c, d=d, e=e, gbhd_list=gbhd, f=f, dnb=dnb, g=g, tgsval=tgsval, hdlval=hdlval, ldlval=ldlval,
            tdlval=tdlval, ejh=ejh, tgs_list=tgs_list, h=h, hdlc=hdlc, hdldict_list=hdldict_list,ldldict_list=ldldict_list, ldlc=ldlc,k=k, ttcdict_list=ttcdict_list,
            hgdict_list=hgdict_list, l=l, hgval=hgval, ydbdict = ydbdict_list, m=m, ydb_abnormal = ydb_abnormal[b], hcc_list=hcc_list, n=n,
            astval=ast_aged[b], altval=alt_aged[b], gtpval=gtpval, ast_list = ast_list, o=o, alt_list = alt_list, p=p, gtp_list = gtp_list, q=q,
            )
