import datetime
now = datetime.datetime.now()

#만나이
def age_cal(a, b, c):
    birth_year, birth_month, birth_day = a, b, c
    if now.month > birth_month:
        american_age = now.year - birth_year
    elif now.month == birth_month:
        if(now.day > birth_day):
            american_age = now.year - birth_year
        else:
            american_age = now.year - birth_year - 1 
    else:
        american_age = now.year - birth_year - 1
    return american_age

male = [{'연령': '20~24세', '비율': 1.8},{'연령': '25~29세', '비율': 6.63},{'연령': '30~34세', '비율': 9.28},{'연령': '35~39세', '비율': 11.27},{'연령': '40~44세', '비율': 12.63},{'연령': '45~49세', '비율': 11.71},{'연령': '50~54세', '비율': 12.38},{'연령': '55~59세', '비율': 10.51},{'연령': '60~64세', '비율': 9.76},{'연령': '65~69세', '비율': 5.37},{'연령': '70~74세', '비율': 4.71},{'연령': '75~79세', '비율': 2.37},{'연령': '80~84세', '비율': 1.33},{'연령': '85세+', '비율': 0.23}]   
female = [{'연령': '20~24세', '비율': 2.53},{'연령': '25~29세', '비율': 6.43},{'연령': '30~34세', '비율': 5.99},  {'연령': '35~39세', '비율': 5.75},{'연령': '40~44세', '비율': 11.8},{'연령': '45~49세', '비율': 11.33},{'연령': '50~54세', '비율': 14.05},{'연령': '55~59세', '비율': 11.87},{'연령': '60~64세', '비율': 11.87},{'연령': '65~69세', '비율': 6.37},{'연령': '70~74세', '비율': 6.0},{'연령': '75~79세', '비율': 3.35},{'연령': '80~84세', '비율': 2.12},{'연령': '85세+', '비율': 0.55}]
su_bp5=[{'혈압': '110미만', '비율': 28.37}, {'혈압': '110~115', '비율': 20.9}, {'혈압': '115~120', '비율': 16.8}, {'혈압': '120~125', '비율': 13.32}, {'혈압': '125~130', '비율': 7.32}, {'혈압': '130~135', '비율': 7.46}, {'혈압': '135~140', '비율': 4.24}, {'혈압': '140~145', '비율': 0.75}, {'혈압': '145~150', '비율': 0.37}, {'혈압': '150이상', '비율': 0.47}]
su_bp6=[{'혈압': '110미만', '비율': 25.19}, {'혈압': '110~115', '비율': 18.87}, {'혈압': '115~120', '비율': 16.44}, {'혈압': '120~125', '비율': 13.97}, {'혈압': '125~130', '비율': 8.43}, {'혈압': '130~135', '비율': 8.72}, {'혈압': '135~140', '비율': 5.52}, {'혈압': '140~145', '비율': 1.18}, {'혈압': '145~150', '비율': 0.64}, {'혈압': '150이상', '비율': 1.03}]
su_bp7=[{'혈압': '110미만', '비율': 22.25}, {'혈압': '110~115', '비율': 16.65}, {'혈압': '115~120', '비율': 15.68}, {'혈압': '120~125', '비율': 14.29}, {'혈압': '125~130', '비율': 9.44}, {'혈압': '130~135', '비율': 10.33}, {'혈압': '135~140', '비율': 6.98}, {'혈압': '140~145', '비율': 1.72}, {'혈압': '145~150', '비율': 0.9}, {'혈압': '150이상', '비율': 1.76}]
su_bp8=[{'혈압': '110미만', '비율': 18.36}, {'혈압': '110~115', '비율': 15.28}, {'혈압': '115~120', '비율': 14.97}, {'혈압': '120~125', '비율': 15.16}, {'혈압': '125~130', '비율': 10.17}, {'혈압': '130~135', '비율': 11.93}, {'혈압': '135~140', '비율': 7.9}, {'혈압': '140~145', '비율': 2.39}, {'혈압': '145~150', '비율': 1.28}, {'혈압': '150이상', '비율': 2.55}]
su_bp9=[{'혈압': '110미만', '비율': 20.03}, {'혈압': '110~115', '비율': 15.16}, {'혈압': '115~120', '비율': 14.29}, {'혈압': '120~125', '비율': 14.86}, {'혈압': '125~130', '비율': 9.91}, {'혈압': '130~135', '비율': 11.3}, {'혈압': '135~140', '비율': 7.24}, {'혈압': '140~145', '비율': 2.95}, {'혈압': '145~150', '비율': 1.4}, {'혈압': '150이상', '비율': 2.86}]
su_bp10=[{'혈압': '110미만', '비율': 17.67}, {'혈압': '110~115', '비율': 14.43}, {'혈압': '115~120', '비율': 13.78}, {'혈압': '120~125', '비율': 15.07}, {'혈압': '125~130', '비율': 10.08}, {'혈압': '130~135', '비율': 12.32}, {'혈압': '135~140', '비율': 8.17}, {'혈압': '140~145', '비율': 3.27}, {'혈압': '145~150', '비율': 1.72}, {'혈압': '150이상', '비율': 3.51}]
su_bp11=[{'혈압': '110미만', '비율': 15.9}, {'혈압': '110~115', '비율': 13.3}, {'혈압': '115~120', '비율': 12.93}, {'혈압': '120~125', '비율': 15.17}, {'혈압': '125~130', '비율': 10.33}, {'혈압': '130~135', '비율': 13.23}, {'혈압': '135~140', '비율': 8.84}, {'혈압': '140~145', '비율': 4.15}, {'혈압': '145~150', '비율': 2.03}, {'혈압': '150이상', '비율': 4.11}]
su_bp12=[{'혈압': '110미만', '비율': 13.54}, {'혈압': '110~115', '비율': 12.14}, {'혈압': '115~120', '비율': 12.22}, {'혈압': '120~125', '비율': 15.26}, {'혈압': '125~130', '비율': 10.62}, {'혈압': '130~135', '비율': 14.54}, {'혈압': '135~140', '비율': 9.81}, {'혈압': '140~145', '비율': 4.8}, {'혈압': '145~150', '비율': 2.43}, {'혈압': '150이상', '비율': 4.65}]
su_bp13=[{'혈압': '110미만', '비율': 10.87}, {'혈압': '110~115', '비율': 10.61}, {'혈압': '115~120', '비율': 10.96}, {'혈압': '120~125', '비율': 15.1}, {'혈압': '125~130', '비율': 10.81}, {'혈압': '130~135', '비율': 15.7}, {'혈압': '135~140', '비율': 10.86}, {'혈압': '140~145', '비율': 5.98}, {'혈압': '145~150', '비율': 3.02}, {'혈압': '150이상', '비율': 6.08}]
su_bp14=[{'혈압': '110미만', '비율': 8.33}, {'혈압': '110~115', '비율': 9.0}, {'혈압': '115~120', '비율': 9.78}, {'혈압': '120~125', '비율': 14.3}, {'혈압': '125~130', '비율': 10.94}, {'혈압': '130~135', '비율': 16.93}, {'혈압': '135~140', '비율': 11.83}, {'혈압': '140~145', '비율': 7.36}, {'혈압': '145~150', '비율': 3.8}, {'혈압': '150이상', '비율': 7.73}]
su_bp15=[{'혈압': '110미만', '비율': 6.44}, {'혈압': '110~115', '비율': 7.67}, {'혈압': '115~120', '비율': 8.38}, {'혈압': '120~125', '비율': 13.63}, {'혈압': '125~130', '비율': 10.54}, {'혈압': '130~135', '비율': 17.27}, {'혈압': '135~140', '비율': 12.27}, {'혈압': '140~145', '비율': 8.89}, {'혈압': '145~150', '비율': 4.81}, {'혈압': '150이상', '비율': 10.1}]
su_bp16=[{'혈압': '110미만', '비율': 5.69}, {'혈압': '110~115', '비율': 7.26}, {'혈압': '115~120', '비율': 7.5}, {'혈압': '120~125', '비율': 13.26}, {'혈압': '125~130', '비율': 9.52}, {'혈압': '130~135', '비율': 17.2}, {'혈압': '135~140', '비율': 11.9}, {'혈압': '140~145', '비율': 9.79}, {'혈압': '145~150', '비율': 5.25}, {'혈압': '150이상', '비율': 12.64}]
su_bp17=[{'혈압': '110미만', '비율': 5.54}, {'혈압': '110~115', '비율': 7.1}, {'혈압': '115~120', '비율': 7.52}, {'혈압': '120~125', '비율': 12.8}, {'혈압': '125~130', '비율': 8.6}, {'혈압': '130~135', '비율': 17.01}, {'혈압': '135~140', '비율': 11.08}, {'혈압': '140~145', '비율': 10.17}, {'혈압': '145~150', '비율': 5.62}, {'혈압': '150이상', '비율': 14.56}]
su_bp18=[{'혈압': '110미만', '비율': 6.6}, {'혈압': '110~115', '비율': 8.67}, {'혈압': '115~120', '비율': 7.17}, {'혈압': '120~125', '비율': 14.22}, {'혈압': '125~130', '비율': 7.9}, {'혈압': '130~135', '비율': 16.78}, {'혈압': '135~140', '비율': 9.38}, {'혈압': '140~145', '비율': 10.12}, {'혈압': '145~150', '비율': 4.86}, {'혈압': '150이상', '비율': 14.3}]
iw_bp5=[{'혈압': '60미만', '비율': 5.07}, {'혈압': '60~65', '비율': 17.49}, {'혈압': '65~70', '비율': 15.0}, {'혈압': '70~75', '비율': 27.85}, {'혈압': '75~80', '비율': 15.62}, {'혈압': '80~85', '비율': 13.48}, {'혈압': '85~90', '비율': 4.22}, {'혈압': '90~95', '비율': 0.77}, {'혈압': '95~100', '비율': 0.23}, {'혈압': '100이상', '비율': 0.25}]
iw_bp6=[{'혈압': '60미만', '비율': 4.68}, {'혈압': '60~65', '비율': 15.57}, {'혈압': '65~70', '비율': 13.91}, {'혈압': '70~75', '비율': 25.84}, {'혈압': '75~80', '비율': 16.29}, {'혈압': '80~85', '비율': 14.96}, {'혈압': '85~90', '비율': 6.04}, {'혈압': '90~95', '비율': 1.45}, {'혈압': '95~100', '비율': 0.58}, {'혈압': '100이상', '비율': 0.69}]
iw_bp7=[{'혈압': '60미만', '비율': 3.68}, {'혈압': '60~65', '비율': 12.72}, {'혈압': '65~70', '비율': 12.58}, {'혈압': '70~75', '비율': 23.73}, {'혈압': '75~80', '비율': 16.85}, {'혈압': '80~85', '비율': 16.97}, {'혈압': '85~90', '비율': 8.65}, {'혈압': '90~95', '비율': 2.31}, {'혈압': '95~100', '비율': 1.05}, {'혈압': '100이상', '비율': 1.46}]
iw_bp8=[{'혈압': '60미만', '비율': 2.78}, {'혈압': '60~65', '비율': 10.03}, {'혈압': '65~70', '비율': 10.63}, {'혈압': '70~75', '비율': 21.98}, {'혈압': '75~80', '비율': 17.33}, {'혈압': '80~85', '비율': 19.23}, {'혈압': '85~90', '비율': 10.71}, {'혈압': '90~95', '비율': 3.26}, {'혈압': '95~100', '비율': 1.67}, {'혈압': '100이상', '비율': 2.38}]
iw_bp9=[{'혈압': '60미만', '비율': 3.03}, {'혈압': '60~65', '비율': 10.38}, {'혈압': '65~70', '비율': 10.93}, {'혈압': '70~75', '비율': 20.76}, {'혈압': '75~80', '비율': 16.58}, {'혈압': '80~85', '비율': 18.67}, {'혈압': '85~90', '비율': 10.92}, {'혈압': '90~95', '비율': 4.17}, {'혈압': '95~100', '비율': 1.97}, {'혈압': '100이상', '비율': 2.59}]
iw_bp10=[{'혈압': '60미만', '비율': 2.59}, {'혈압': '60~65', '비율': 9.18}, {'혈압': '65~70', '비율': 9.86}, {'혈압': '70~75', '비율': 20.44}, {'혈압': '75~80', '비율': 16.37}, {'혈압': '80~85', '비율': 20.06}, {'혈압': '85~90', '비율': 11.66}, {'혈압': '90~95', '비율': 4.82}, {'혈압': '95~100', '비율': 2.22}, {'혈압': '100이상', '비율': 2.79}]
iw_bp11=[{'혈압': '60미만', '비율': 2.36}, {'혈압': '60~65', '비율': 8.33}, {'혈압': '65~70', '비율': 9.4}, {'혈압': '70~75', '비율': 19.98}, {'혈압': '75~80', '비율': 16.51}, {'혈압': '80~85', '비율': 21.13}, {'혈압': '85~90', '비율': 12.01}, {'혈압': '90~95', '비율': 5.49}, {'혈압': '95~100', '비율': 2.23}, {'혈압': '100이상', '비율': 2.58}]
iw_bp12=[{'혈압': '60미만', '비율': 2.01}, {'혈압': '60~65', '비율': 7.96}, {'혈압': '65~70', '비율': 8.94}, {'혈압': '70~75', '비율': 20.31}, {'혈압': '75~80', '비율': 16.69}, {'혈압': '80~85', '비율': 22.53}, {'혈압': '85~90', '비율': 11.65}, {'혈압': '90~95', '비율': 5.68}, {'혈압': '95~100', '비율': 2.06}, {'혈압': '100이상', '비율': 2.17}]
iw_bp13=[{'혈압': '60미만', '비율': 2.02}, {'혈압': '60~65', '비율': 7.53}, {'혈압': '65~70', '비율': 9.42}, {'혈압': '70~75', '비율': 20.61}, {'혈압': '75~80', '비율': 16.94}, {'혈압': '80~85', '비율': 22.91}, {'혈압': '85~90', '비율': 10.8}, {'혈압': '90~95', '비율': 5.88}, {'혈압': '95~100', '비율': 2.0}, {'혈압': '100이상', '비율': 1.9}]
iw_bp14=[{'혈압': '60미만', '비율': 2.27}, {'혈압': '60~65', '비율': 7.6}, {'혈압': '65~70', '비율': 9.84}, {'혈압': '70~75', '비율': 21.39}, {'혈압': '75~80', '비율': 16.72}, {'혈압': '80~85', '비율': 23.2}, {'혈압': '85~90', '비율': 9.75}, {'혈압': '90~95', '비율': 5.86}, {'혈압': '95~100', '비율': 1.75}, {'혈압': '100이상', '비율': 1.62}]
iw_bp15=[{'혈압': '60미만', '비율': 2.56}, {'혈압': '60~65', '비율': 8.26}, {'혈압': '65~70', '비율': 10.31}, {'혈압': '70~75', '비율': 21.9}, {'혈압': '75~80', '비율': 16.08}, {'혈압': '80~85', '비율': 22.92}, {'혈압': '85~90', '비율': 8.61}, {'혈압': '90~95', '비율': 6.01}, {'혈압': '95~100', '비율': 1.65}, {'혈압': '100이상', '비율': 1.68}]
iw_bp16=[{'혈압': '60미만', '비율': 2.93}, {'혈압': '60~65', '비율': 9.09}, {'혈압': '65~70', '비율': 10.52}, {'혈압': '70~75', '비율': 22.77}, {'혈압': '75~80', '비율': 14.97}, {'혈압': '80~85', '비율': 22.72}, {'혈압': '85~90', '비율': 7.53}, {'혈압': '90~95', '비율': 6.21}, {'혈압': '95~100', '비율': 1.46}, {'혈압': '100이상', '비율': 1.81}]
iw_bp17=[{'혈압': '60미만', '비율': 3.38}, {'혈압': '60~65', '비율': 9.84}, {'혈압': '65~70', '비율': 9.84}, {'혈압': '70~75', '비율': 22.7}, {'혈압': '75~80', '비율': 13.87}, {'혈압': '80~85', '비율': 22.99}, {'혈압': '85~90', '비율': 7.16}, {'혈압': '90~95', '비율': 6.44}, {'혈압': '95~100', '비율': 1.69}, {'혈압': '100이상', '비율': 2.09}]
iw_bp18=[{'혈압': '60미만', '비율': 4.46}, {'혈압': '60~65', '비율': 11.15}, {'혈압': '65~70', '비율': 8.84}, {'혈압': '70~75', '비율': 22.72}, {'혈압': '75~80', '비율': 12.85}, {'혈압': '80~85', '비율': 24.0}, {'혈압': '85~90', '비율': 5.97}, {'혈압': '90~95', '비율': 6.82}, {'혈압': '95~100', '비율': 1.28}, {'혈압': '100이상', '비율': 1.91}]
gbhd5=[{'혈당': '100미만', '비율': 86.73}, {'혈당': '100~126', '비율': 12.61}, {'혈당': '126이상', '비율': 0.66}]
gbhd6=[{'혈당': '100미만', '비율': 83.33}, {'혈당': '100~126', '비율': 15.83}, {'혈당': '126이상', '비율': 0.84}]
gbhd7=[{'혈당': '100미만', '비율': 77.34}, {'혈당': '100~126', '비율': 20.87}, {'혈당': '126이상', '비율': 1.79}]
gbhd8=[{'혈당': '100미만', '비율': 69.76}, {'혈당': '100~126', '비율': 27.03}, {'혈당': '126이상', '비율': 3.21}]
gbhd9=[{'혈당': '100미만', '비율': 66.65}, {'혈당': '100~126', '비율': 28.35}, {'혈당': '126이상', '비율': 5.0}]
gbhd10=[{'혈당': '100미만', '비율': 61.58}, {'혈당': '100~126', '비율': 31.56}, {'혈당': '126이상', '비율': 6.85}]
gbhd11=[{'혈당': '100미만', '비율': 56.74}, {'혈당': '100~126', '비율': 34.29}, {'혈당': '126이상', '비율': 8.97}]
gbhd12=[{'혈당': '100미만', '비율': 52.85}, {'혈당': '100~126', '비율': 36.12}, {'혈당': '126이상', '비율': 11.03}]
gbhd13=[{'혈당': '100미만', '비율': 50.71}, {'혈당': '100~126', '비율': 36.69}, {'혈당': '126이상', '비율': 12.6}]
gbhd14=[{'혈당': '100미만', '비율': 48.6}, {'혈당': '100~126', '비율': 37.48}, {'혈당': '126이상', '비율': 13.91}]
gbhd15=[{'혈당': '100미만', '비율': 47.64}, {'혈당': '100~126', '비율': 37.69}, {'혈당': '126이상', '비율': 14.67}]
gbhd16=[{'혈당': '100미만', '비율': 47.1}, {'혈당': '100~126', '비율': 38.06}, {'혈당': '126이상', '비율': 14.85}]
gbhd17=[{'혈당': '100미만', '비율': 47.7}, {'혈당': '100~126', '비율': 38.3}, {'혈당': '126이상', '비율': 14.0}]
gbhd18=[{'혈당': '100미만', '비율': 50.73}, {'혈당': '100~126', '비율': 35.41}, {'혈당': '126이상', '비율': 13.86}]
tg_list = [104, 128, 150, 164, 137, 141, 140, 137, 133, 128, 126, 126, 126, 121]
hdl_list = [57, 56, 54, 53, 58, 58, 58, 57, 56, 55, 54, 54, 53, 52]
ldl_list = [ 99, 108, 115, 118, 115, 117, 119, 119, 113, 107, 104, 102, 102, 102]
tdl_list = [176, 188, 196, 201, 199, 202, 203, 202, 195, 187, 184, 181, 181,178]
tgdict5 = [{'혈압': '150미만', '비율': 0.85}, {'혈압': '150~200', '비율': 0.09}, {'혈압': '200이상', '비율': 0.06}]
tgdict6 = [{'혈압': '150미만', '비율': 0.77}, {'혈압': '150~200', '비율': 0.12}, {'혈압': '200이상', '비율': 0.11}]
tgdict7 = [{'혈압': '150미만', '비율': 0.68}, {'혈압': '150~200', '비율': 0.15}, {'혈압': '200이상', '비율': 0.17}]
tgdict8 = [{'혈압': '150미만', '비율': 0.63}, {'혈압': '150~200', '비율': 0.17}, {'혈압': '200이상', '비율': 0.2}]
tgdict9 = [{'혈압': '150미만', '비율': 0.72}, {'혈압': '150~200', '비율': 0.13}, {'혈압': '200이상', '비율': 0.15}]
tgdict10 = [{'혈압': '150미만', '비율': 0.71}, {'혈압': '150~200', '비율': 0.14}, {'혈압': '200이상', '비율': 0.15}]
tgdict11 = [{'혈압': '150미만', '비율': 0.7}, {'혈압': '150~200', '비율': 0.15}, {'혈압': '200이상', '비율': 0.15}]
tgdict12 = [{'혈압': '150미만', '비율': 0.71}, {'혈압': '150~200', '비율': 0.15}, {'혈압': '200이상', '비율': 0.14}]
tgdict13 = [{'혈압': '150미만', '비율': 0.71}, {'혈압': '150~200', '비율': 0.15}, {'혈압': '200이상', '비율': 0.13}]
tgdict14 = [{'혈압': '150미만', '비율': 0.74}, {'혈압': '150~200', '비율': 0.15}, {'혈압': '200이상', '비율': 0.11}]
tgdict15 = [{'혈압': '150미만', '비율': 0.74}, {'혈압': '150~200', '비율': 0.15}, {'혈압': '200이상', '비율': 0.11}]
tgdict16 = [{'혈압': '150미만', '비율': 0.75}, {'혈압': '150~200', '비율': 0.15}, {'혈압': '200이상', '비율': 0.1}]
tgdict17 = [{'혈압': '150미만', '비율': 0.74}, {'혈압': '150~200', '비율': 0.16}, {'혈압': '200이상', '비율': 0.1}]
tgdict18 = [{'혈압': '150미만', '비율': 0.77}, {'혈압': '150~200', '비율': 0.15}, {'혈압': '200이상', '비율': 0.08}]
hdldict5 = [{'혈압': '40미만', '비율': 0.07}, {'혈압': '40~60', '비율': 0.56}, {'혈압': '60이상', '비율': 0.38}]
hdldict6 = [{'혈압': '40미만', '비율': 0.08}, {'혈압': '40~60', '비율': 0.57}, {'혈압': '60이상', '비율': 0.35}]
hdldict7 = [{'혈압': '40미만', '비율': 0.1}, {'혈압': '40~60', '비율': 0.6}, {'혈압': '60이상', '비율': 0.3}]
hdldict8 = [{'혈압': '40미만', '비율': 0.11}, {'혈압': '40~60', '비율': 0.62}, {'혈압': '60이상', '비율': 0.27}]
hdldict9 = [{'혈압': '40미만', '비율': 0.08}, {'혈압': '40~60', '비율': 0.5}, {'혈압': '60이상', '비율': 0.42}]
hdldict10 = [{'혈압': '40미만', '비율': 0.08}, {'혈압': '40~60', '비율': 0.51}, {'혈압': '60이상', '비율': 0.41}]
hdldict11 = [{'혈압': '40미만', '비율': 0.09}, {'혈압': '40~60', '비율': 0.51}, {'혈압': '60이상', '비율': 0.4}]
hdldict12 = [{'혈압': '40미만', '비율': 0.09}, {'혈압': '40~60', '비율': 0.52}, {'혈압': '60이상', '비율': 0.39}]
hdldict13 = [{'혈압': '40미만', '비율': 0.1}, {'혈압': '40~60', '비율': 0.54}, {'혈압': '60이상', '비율': 0.35}]
hdldict14 = [{'혈압': '40미만', '비율': 0.11}, {'혈압': '40~60', '비율': 0.56}, {'혈압': '60이상', '비율': 0.32}]
hdldict15 = [{'혈압': '40미만', '비율': 0.13}, {'혈압': '40~60', '비율': 0.56}, {'혈압': '60이상', '비율': 0.31}]
hdldict16 = [{'혈압': '40미만', '비율': 0.14}, {'혈압': '40~60', '비율': 0.57}, {'혈압': '60이상', '비율': 0.29}]
hdldict17 = [{'혈압': '40미만', '비율': 0.16}, {'혈압': '40~60', '비율': 0.56}, {'혈압': '60이상', '비율': 0.29}]
hdldict18 = [{'혈압': '40미만', '비율': 0.19}, {'혈압': '40~60', '비율': 0.54}, {'혈압': '60이상', '비율': 0.27}]
ldldict5 = [{'혈압': '130미만', '비율': 0.01}, {'혈압': '130~160', '비율': 0.06}, {'혈압': '160이상', '비율': 0.94}]
ldldict6 = [{'혈압': '130미만', '비율': 0.01}, {'혈압': '130~160', '비율': 0.04}, {'혈압': '160이상', '비율': 0.96}]
ldldict7 = [{'혈압': '130미만', '비율': 0.0}, {'혈압': '130~160', '비율': 0.02}, {'혈압': '160이상', '비율': 0.97}]
ldldict8 = [{'혈압': '130미만', '비율': 0.0}, {'혈압': '130~160', '비율': 0.02}, {'혈압': '160이상', '비율': 0.97}]
ldldict9 = [{'혈압': '130미만', '비율': 0.01}, {'혈압': '130~160', '비율': 0.03}, {'혈압': '160이상', '비율': 0.97}]
ldldict10 = [{'혈압': '130미만', '비율': 0.01}, {'혈압': '130~160', '비율': 0.03}, {'혈압': '160이상', '비율': 0.96}]
ldldict11 = [{'혈압': '130미만', '비율': 0.01}, {'혈압': '130~160', '비율': 0.03}, {'혈압': '160이상', '비율': 0.96}]
ldldict12 = [{'혈압': '130미만', '비율': 0.01}, {'혈압': '130~160', '비율': 0.04}, {'혈압': '160이상', '비율': 0.95}]
ldldict13 = [{'혈압': '130미만', '비율': 0.01}, {'혈압': '130~160', '비율': 0.05}, {'혈압': '160이상', '비율': 0.93}]
ldldict14 = [{'혈압': '130미만', '비율': 0.02}, {'혈압': '130~160', '비율': 0.07}, {'혈압': '160이상', '비율': 0.91}]
ldldict15 = [{'혈압': '130미만', '비율': 0.02}, {'혈압': '130~160', '비율': 0.08}, {'혈압': '160이상', '비율': 0.9}]
ldldict16 = [{'혈압': '130미만', '비율': 0.02}, {'혈압': '130~160', '비율': 0.09}, {'혈압': '160이상', '비율': 0.89}]
ldldict17 = [{'혈압': '130미만', '비율': 0.02}, {'혈압': '130~160', '비율': 0.09}, {'혈압': '160이상', '비율': 0.89}]
ldldict18 = [{'혈압': '130미만', '비율': 0.02}, {'혈압': '130~160', '비율': 0.09}, {'혈압': '160이상', '비율': 0.9}]
ttcdict5 = [{'혈압': '200미만', '비율': 0.8}, {'혈압': '200~240', '비율': 0.17}, {'혈압': '240이상', '비율': 0.03}]
ttcdict6 = [{'혈압': '200미만', '비율': 0.68}, {'혈압': '200~240', '비율': 0.26}, {'혈압': '240이상', '비율': 0.06}]
ttcdict7 = [{'혈압': '200미만', '비율': 0.58}, {'혈압': '200~240', '비율': 0.32}, {'혈압': '240이상', '비율': 0.1}]
ttcdict8 = [{'혈압': '200미만', '비율': 0.53}, {'혈압': '200~240', '비율': 0.34}, {'혈압': '240이상', '비율': 0.13}]
ttcdict9 = [{'혈압': '200미만', '비율': 0.55}, {'혈압': '200~240', '비율': 0.33}, {'혈압': '240이상', '비율': 0.12}]
ttcdict10 = [{'혈압': '200미만', '비율': 0.51}, {'혈압': '200~240', '비율': 0.35}, {'혈압': '240이상', '비율': 0.14}]
ttcdict11 = [{'혈압': '200미만', '비율': 0.48}, {'혈압': '200~240', '비율': 0.35}, {'혈압': '240이상', '비율': 0.17}]
ttcdict12 = [{'혈압': '200미만', '비율': 0.49}, {'혈압': '200~240', '비율': 0.34}, {'혈압': '240이상', '비율': 0.17}]
ttcdict13 = [{'혈압': '200미만', '비율': 0.56}, {'혈압': '200~240', '비율': 0.31}, {'혈압': '240이상', '비율': 0.13}]
ttcdict14 = [{'혈압': '200미만', '비율': 0.64}, {'혈압': '200~240', '비율': 0.27}, {'혈압': '240이상', '비율': 0.09}]
ttcdict15 = [{'혈압': '200미만', '비율': 0.68}, {'혈압': '200~240', '비율': 0.24}, {'혈압': '240이상', '비율': 0.09}]
ttcdict16 = [{'혈압': '200미만', '비율': 0.7}, {'혈압': '200~240', '비율': 0.22}, {'혈압': '240이상', '비율': 0.07}]
ttcdict17 = [{'혈압': '200미만', '비율': 0.71}, {'혈압': '200~240', '비율': 0.22}, {'혈압': '240이상', '비율': 0.08}]
ttcdict18 = [{'혈압': '200미만', '비율': 0.72}, {'혈압': '200~240', '비율': 0.2}, {'혈압': '240이상', '비율': 0.08}]
hgdict_male5 = [{'혈색': '13미만', '비율': 0.006}, {'혈색': '13~17.5', '비율': 0.969}, {'혈색': '17.5이상', '비율': 0.025}]
hgdict_male6 = [{'혈색': '13미만', '비율': 0.005}, {'혈색': '13~17.5', '비율': 0.97}, {'혈색': '17.5이상', '비율': 0.025}]
hgdict_male7 = [{'혈색': '13미만', '비율': 0.005}, {'혈색': '13~17.5', '비율': 0.969}, {'혈색': '17.5이상', '비율': 0.025}]
hgdict_male8 = [{'혈색': '13미만', '비율': 0.007}, {'혈색': '13~17.5', '비율': 0.966}, {'혈색': '17.5이상', '비율': 0.027}]
hgdict_male9 = [{'혈색': '13미만', '비율': 0.01}, {'혈색': '13~17.5', '비율': 0.961}, {'혈색': '17.5이상', '비율': 0.03}]
hgdict_male10 = [{'혈색': '13미만', '비율': 0.014}, {'혈색': '13~17.5', '비율': 0.96}, {'혈색': '17.5이상', '비율': 0.026}]
hgdict_male11 = [{'혈색': '13미만', '비율': 0.02}, {'혈색': '13~17.5', '비율': 0.955}, {'혈색': '17.5이상', '비율': 0.025}]
hgdict_male12 = [{'혈색': '13미만', '비율': 0.029}, {'혈색': '13~17.5', '비율': 0.951}, {'혈색': '17.5이상', '비율': 0.02}]
hgdict_male13 = [{'혈색': '13미만', '비율': 0.046}, {'혈색': '13~17.5', '비율': 0.936}, {'혈색': '17.5이상', '비율': 0.018}]
hgdict_male14 = [{'혈색': '13미만', '비율': 0.068}, {'혈색': '13~17.5', '비율': 0.917}, {'혈색': '17.5이상', '비율': 0.014}]
hgdict_male15 = [{'혈색': '13미만', '비율': 0.108}, {'혈색': '13~17.5', '비율': 0.881}, {'혈색': '17.5이상', '비율': 0.011}]
hgdict_male16 = [{'혈색': '13미만', '비율': 0.178}, {'혈색': '13~17.5', '비율': 0.814}, {'혈색': '17.5이상', '비율': 0.008}]
hgdict_male17 = [{'혈색': '13미만', '비율': 0.245}, {'혈색': '13~17.5', '비율': 0.75}, {'혈색': '17.5이상', '비율': 0.005}]
hgdict_male18 = [{'혈색': '13미만', '비율': 0.382}, {'혈색': '13~17.5', '비율': 0.614}, {'혈색': '17.5이상', '비율': 0.003}]
hgdict_female5 = [{'혈색': '12미만', '비율': 0.077}, {'혈색': '12~15.5', '비율': 0.915}, {'혈색': '15.5이상', '비율': 0.008}]
hgdict_female6 = [{'혈색': '12미만', '비율': 0.075}, {'혈색': '12~15.5', '비율': 0.917}, {'혈색': '15.5이상', '비율': 0.008}]
hgdict_female7 = [{'혈색': '12미만', '비율': 0.094}, {'혈색': '12~15.5', '비율': 0.897}, {'혈색': '15.5이상', '비율': 0.009}]
hgdict_female8 = [{'혈색': '12미만', '비율': 0.137}, {'혈색': '12~15.5', '비율': 0.856}, {'혈색': '15.5이상', '비율': 0.007}]
hgdict_female9 = [{'혈색': '12미만', '비율': 0.175}, {'혈색': '12~15.5', '비율': 0.816}, {'혈색': '15.5이상', '비율': 0.009}]
hgdict_female10 = [{'혈색': '12미만', '비율': 0.178}, {'혈색': '12~15.5', '비율': 0.812}, {'혈색': '15.5이상', '비율': 0.01}]
hgdict_female11 = [{'혈색': '12미만', '비율': 0.092}, {'혈색': '12~15.5', '비율': 0.891}, {'혈색': '15.5이상', '비율': 0.017}]
hgdict_female12 = [{'혈색': '12미만', '비율': 0.052}, {'혈색': '12~15.5', '비율': 0.932}, {'혈색': '15.5이상', '비율': 0.016}]
hgdict_female13 = [{'혈색': '12미만', '비율': 0.064}, {'혈색': '12~15.5', '비율': 0.918}, {'혈색': '15.5이상', '비율': 0.017}]
hgdict_female14 = [{'혈색': '12미만', '비율': 0.088}, {'혈색': '12~15.5', '비율': 0.897}, {'혈색': '15.5이상', '비율': 0.015}]
hgdict_female15 = [{'혈색': '12미만', '비율': 0.124}, {'혈색': '12~15.5', '비율': 0.862}, {'혈색': '15.5이상', '비율': 0.014}]
hgdict_female16 = [{'혈색': '12미만', '비율': 0.188}, {'혈색': '12~15.5', '비율': 0.801}, {'혈색': '15.5이상', '비율': 0.011}]
hgdict_female17 = [{'혈색': '12미만', '비율': 0.26}, {'혈색': '12~15.5', '비율': 0.729}, {'혈색': '15.5이상', '비율': 0.011}]
hgdict_female18 = [{'혈색': '12미만', '비율': 0.402}, {'혈색': '12~15.5', '비율': 0.589}, {'혈색': '15.5이상', '비율': 0.009}]
hg_male_list = [15.62, 15.62, 15.6 , 15.54, 15.51, 15.4 , 15.32, 15.16, 14.99,14.78, 14.52, 14.17, 13.84, 13.3 ]
hg_female_list = [13.26, 13.29, 13.21, 13.02, 12.9 , 12.91, 13.28, 13.42, 13.37,13.26, 13.13, 12.88, 12.66, 12.16]
ydbdict5 = [{'요단백': 1, '비율': 94}, {'요단백': 2, '비율': 3}, {'요단백': 3, '비율': 2}, {'요단백': 4, '비율': 0}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict6 = [{'요단백': 1, '비율': 94}, {'요단백': 2, '비율': 4}, {'요단백': 3, '비율': 2}, {'요단백': 4, '비율': 0}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict7 = [{'요단백': 1, '비율': 94}, {'요단백': 2, '비율': 4}, {'요단백': 3, '비율': 1}, {'요단백': 4, '비율': 0}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict8 = [{'요단백': 1, '비율': 94}, {'요단백': 2, '비율': 4}, {'요단백': 3, '비율': 1}, {'요단백': 4, '비율': 0}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict9 = [{'요단백': 1, '비율': 94}, {'요단백': 2, '비율': 4}, {'요단백': 3, '비율': 2}, {'요단백': 4, '비율': 1}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict10 = [{'요단백': 1, '비율': 94}, {'요단백': 2, '비율': 4}, {'요단백': 3, '비율': 2}, {'요단백': 4, '비율': 1}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict11 = [{'요단백': 1, '비율': 94}, {'요단백': 2, '비율': 3}, {'요단백': 3, '비율': 2}, {'요단백': 4, '비율': 1}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict12 = [{'요단백': 1, '비율': 95}, {'요단백': 2, '비율': 3}, {'요단백': 3, '비율': 2}, {'요단백': 4, '비율': 1}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict13 = [{'요단백': 1, '비율': 94}, {'요단백': 2, '비율': 3}, {'요단백': 3, '비율': 2}, {'요단백': 4, '비율': 1}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict14 = [{'요단백': 1, '비율': 94}, {'요단백': 2, '비율': 3}, {'요단백': 3, '비율': 2}, {'요단백': 4, '비율': 1}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict15 = [{'요단백': 1, '비율': 93}, {'요단백': 2, '비율': 3}, {'요단백': 3, '비율': 2}, {'요단백': 4, '비율': 1}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict16 = [{'요단백': 1, '비율': 92}, {'요단백': 2, '비율': 3}, {'요단백': 3, '비율': 3}, {'요단백': 4, '비율': 1}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydbdict17 = [{'요단백': 1, '비율': 91}, {'요단백': 2, '비율': 3}, {'요단백': 3, '비율': 3}, {'요단백': 4, '비율': 2}, {'요단백': 5, '비율': 1}, {'요단백': 6, '비율': 0}]
ydbdict18 = [{'요단백': 1, '비율': 92}, {'요단백': 2, '비율': 3}, {'요단백': 3, '비율': 3}, {'요단백': 4, '비율': 1}, {'요단백': 5, '비율': 0}, {'요단백': 6, '비율': 0}]
ydb_abnormal = [2.18, 2.03, 1.92, 1.92, 2.4 , 2.33, 2.39, 2.41, 2.91, 3.36, 3.96,4.67, 5.52, 5.08]
hcc5 = [{'혈청': '1.2이하', '비율': 99}, {'혈청': '1.2~1.7', '비율': 1}, {'혈청': '1.7초과', '비율': 0}]
hcc6 = [{'혈청': '1.2이하', '비율': 99}, {'혈청': '1.2~1.7', '비율': 1}, {'혈청': '1.7초과', '비율': 0}]
hcc7 = [{'혈청': '1.2이하', '비율': 99}, {'혈청': '1.2~1.7', '비율': 2}, {'혈청': '1.7초과', '비율': 0}]
hcc8 = [{'혈청': '1.2이하', '비율': 98}, {'혈청': '1.2~1.7', '비율': 2}, {'혈청': '1.7초과', '비율': 0}]
hcc9 = [{'혈청': '1.2이하', '비율': 99}, {'혈청': '1.2~1.7', '비율': 2}, {'혈청': '1.7초과', '비율': 0}]
hcc10 = [{'혈청': '1.2이하', '비율': 98}, {'혈청': '1.2~1.7', '비율': 2}, {'혈청': '1.7초과', '비율': 0}]
hcc11 = [{'혈청': '1.2이하', '비율': 98}, {'혈청': '1.2~1.7', '비율': 2}, {'혈청': '1.7초과', '비율': 0}]
hcc12 = [{'혈청': '1.2이하', '비율': 98}, {'혈청': '1.2~1.7', '비율': 2}, {'혈청': '1.7초과', '비율': 0}]
hcc13 = [{'혈청': '1.2이하', '비율': 97}, {'혈청': '1.2~1.7', '비율': 3}, {'혈청': '1.7초과', '비율': 0}]
hcc14 = [{'혈청': '1.2이하', '비율': 96}, {'혈청': '1.2~1.7', '비율': 4}, {'혈청': '1.7초과', '비율': 1}]
hcc15 = [{'혈청': '1.2이하', '비율': 95}, {'혈청': '1.2~1.7', '비율': 5}, {'혈청': '1.7초과', '비율': 1}]
hcc16 = [{'혈청': '1.2이하', '비율': 93}, {'혈청': '1.2~1.7', '비율': 7}, {'혈청': '1.7초과', '비율': 1}]
hcc17 = [{'혈청': '1.2이하', '비율': 90}, {'혈청': '1.2~1.7', '비율': 10}, {'혈청': '1.7초과', '비율': 2}]
hcc18 = [{'혈청': '1.2이하', '비율': 90}, {'혈청': '1.2~1.7', '비율': 12}, {'혈청': '1.7초과', '비율': 3}]
ast_aged = [21, 23, 25, 25, 26, 26, 27, 28, 28, 28, 28, 27, 26, 25]
alt_aged = [20, 24, 28, 30, 27, 26, 27, 27, 26, 25, 24, 22, 20, 17]
gtp_male_aged = [28, 37, 45, 50, 55, 56, 56, 54, 51, 46, 42, 38, 36, 35]
gtp_female_aged = [16, 17, 18, 20, 22, 23, 26, 27, 27, 26, 25, 25, 24, 24]
ast5 = [{'혈청': '40이하', '비율': 97}, {'혈청': '40초과', '비율': 3}]
ast6 = [{'혈청': '40이하', '비율': 95}, {'혈청': '40초과', '비율': 5}]
ast7 = [{'혈청': '40이하', '비율': 93}, {'혈청': '40초과', '비율': 7}]
ast8 = [{'혈청': '40이하', '비율': 92}, {'혈청': '40초과', '비율': 8}]
ast9 = [{'혈청': '40이하', '비율': 92}, {'혈청': '40초과', '비율': 8}]
ast10 = [{'혈청': '40이하', '비율': 93}, {'혈청': '40초과', '비율': 7}]
ast11 = [{'혈청': '40이하', '비율': 92}, {'혈청': '40초과', '비율': 8}]
ast12 = [{'혈청': '40이하', '비율': 91}, {'혈청': '40초과', '비율': 9}]
ast13 = [{'혈청': '40이하', '비율': 91}, {'혈청': '40초과', '비율': 9}]
ast14 = [{'혈청': '40이하', '비율': 91}, {'혈청': '40초과', '비율': 9}]
ast15 = [{'혈청': '40이하', '비율': 92}, {'혈청': '40초과', '비율': 8}]
ast16 = [{'혈청': '40이하', '비율': 93}, {'혈청': '40초과', '비율': 7}]
ast17 = [{'혈청': '40이하', '비율': 94}, {'혈청': '40초과', '비율': 6}]
ast18 = [{'혈청': '40이하', '비율': 95}, {'혈청': '40초과', '비율': 5}]
alt5 = [{'혈청': '40이하', '비율': 93}, {'혈청': '40초과', '비율': 7}]
alt6 = [{'혈청': '40이하', '비율': 88}, {'혈청': '40초과', '비율': 12}]
alt7 = [{'혈청': '40이하', '비율': 83}, {'혈청': '40초과', '비율': 17}]
alt8 = [{'혈청': '40이하', '비율': 81}, {'혈청': '40초과', '비율': 19}]
alt9 = [{'혈청': '40이하', '비율': 84}, {'혈청': '40초과', '비율': 16}]
alt10 = [{'혈청': '40이하', '비율': 86}, {'혈청': '40초과', '비율': 14}]
alt11 = [{'혈청': '40이하', '비율': 87}, {'혈청': '40초과', '비율': 13}]
alt12 = [{'혈청': '40이하', '비율': 87}, {'혈청': '40초과', '비율': 13}]
alt13 = [{'혈청': '40이하', '비율': 88}, {'혈청': '40초과', '비율': 12}]
alt14 = [{'혈청': '40이하', '비율': 90}, {'혈청': '40초과', '비율': 10}]
alt15 = [{'혈청': '40이하', '비율': 92}, {'혈청': '40초과', '비율': 8}]
alt16 = [{'혈청': '40이하', '비율': 94}, {'혈청': '40초과', '비율': 6}]
alt17 = [{'혈청': '40이하', '비율': 96}, {'혈청': '40초과', '비율': 4}]
alt18 = [{'혈청': '40이하', '비율': 97}, {'혈청': '40초과', '비율': 3}]
gtp_male5 = [{'혈청': '63이하', '비율': 95}, {'혈청': '63초과', '비율': 5}]
gtp_male6 = [{'혈청': '63이하', '비율': 89}, {'혈청': '63초과', '비율': 11}]
gtp_male7 = [{'혈청': '63이하', '비율': 82}, {'혈청': '63초과', '비율': 18}]
gtp_male8 = [{'혈청': '63이하', '비율': 78}, {'혈청': '63초과', '비율': 22}]
gtp_male9 = [{'혈청': '63이하', '비율': 75}, {'혈청': '63초과', '비율': 25}]
gtp_male10 = [{'혈청': '63이하', '비율': 75}, {'혈청': '63초과', '비율': 25}]
gtp_male11 = [{'혈청': '63이하', '비율': 77}, {'혈청': '63초과', '비율': 23}]
gtp_male12 = [{'혈청': '63이하', '비율': 79}, {'혈청': '63초과', '비율': 21}]
gtp_male13 = [{'혈청': '63이하', '비율': 81}, {'혈청': '63초과', '비율': 19}]
gtp_male14 = [{'혈청': '63이하', '비율': 85}, {'혈청': '63초과', '비율': 15}]
gtp_male15 = [{'혈청': '63이하', '비율': 88}, {'혈청': '63초과', '비율': 12}]
gtp_male16 = [{'혈청': '63이하', '비율': 90}, {'혈청': '63초과', '비율': 10}]
gtp_male17 = [{'혈청': '63이하', '비율': 91}, {'혈청': '63초과', '비율': 9}]
gtp_male18 = [{'혈청': '63이하', '비율': 92}, {'혈청': '63초과', '비율': 8}]
gtp_female5 = [{'혈청': '35이하', '비율': 97}, {'혈청': '35초과', '비율': 3}]
gtp_female6 = [{'혈청': '35이하', '비율': 95}, {'혈청': '35초과', '비율': 5}]
gtp_female7 = [{'혈청': '35이하', '비율': 94}, {'혈청': '35초과', '비율': 6}]
gtp_female8 = [{'혈청': '35이하', '비율': 92}, {'혈청': '35초과', '비율': 8}]
gtp_female9 = [{'혈청': '35이하', '비율': 90}, {'혈청': '35초과', '비율': 10}]
gtp_female10 = [{'혈청': '35이하', '비율': 89}, {'혈청': '35초과', '비율': 11}]
gtp_female11 = [{'혈청': '35이하', '비율': 84}, {'혈청': '35초과', '비율': 16}]
gtp_female12 = [{'혈청': '35이하', '비율': 84}, {'혈청': '35초과', '비율': 16}]
gtp_female13 = [{'혈청': '35이하', '비율': 84}, {'혈청': '35초과', '비율': 16}]
gtp_female14 = [{'혈청': '35이하', '비율': 85}, {'혈청': '35초과', '비율': 15}]
gtp_female15 = [{'혈청': '35이하', '비율': 86}, {'혈청': '35초과', '비율': 14}]
gtp_female16 = [{'혈청': '35이하', '비율': 87}, {'혈청': '35초과', '비율': 13}]
gtp_female17 = [{'혈청': '35이하', '비율': 88}, {'혈청': '35초과', '비율': 12}]
gtp_female18 = [{'혈청': '35이하', '비율': 89}, {'혈청': '35초과', '비율': 11}]
total = [{'0~5': '정상'}, {'6~11': '평균이하'}, {'12~17': '위험'}, {'18~22': '매우 위험'}]