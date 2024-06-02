def cal_bmi(height:int, weight:int)->float:
    BMI = weight / (height / 100) ** 2
    return BMI

def get_status(bmi:float)->str:
    if bmi < 18.5:
        rate = "過輕"
    elif bmi < 24:
        rate = "正常"
    elif bmi < 27:
        rate = "過重"
    elif bmi < 30:
        rate = "輕度肥胖"
    elif bmi < 35:
        rate = "中度肥胖"
    else:
        rate = "重度肥胖"
    
    return rate