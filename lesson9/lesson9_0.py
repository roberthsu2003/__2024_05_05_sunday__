#內建的變數__name__
import pyinputplus as pypi

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

def main()->None:
    name = pypi.inputStr("請輸入您的姓名: ")
    print(name)
    height = pypi.inputInt("請輸入您的身高(cm): ", min=50, max=250)
    print(height)
    weight = pypi.inputInt("請輸入您的體重(kg): ", min=0, max=200)
    print(weight)

    BMI = cal_bmi(height=height, weight=weight)
    rate = get_status(BMI)
    print(f"您的姓名為 {name}\n您的BMI值為 {BMI}\n您屬於 {rate} 範圍")


if __name__ == '__main__':
    '''
    print("我是被python執行的主程式")
    print(__name__)
    print(type(__name__))
    '''
    main()
    