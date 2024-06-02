#常數必需使用大寫

PI = 3.1415926


#自訂的function
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


#建立實體的attribute(屬性)
class Person():
    def __init__(self,n:str): #自訂的init
        self.name = n

    def __repr__(self) -> str:
        return f'我的名字叫{self.name}'

#繼承-實體的method()
class Student(Person):
    def __init__(self,n:str,ch:int,en:int,ma:int):
        super().__init__(n) #執行父類別的init
        self.__chinese = ch
        self.__english = en
        self.__math = ma

    @property
    def chinese(self) -> int:
        return self.__chinese
    
    @property
    def english(self) -> int:
        return self.__english
    
    @property
    def math(self) -> int:
        return self.__math
    
    def __repr__(self) -> str:
        message:str = super().__repr__()
        message += "\n我是一個學生"
        return message
    
    def sum(self)->int: #實體的method
        return self.chinese + self.english + self.math
    
    def average(self)->float:#實體的method
        return round(self.sum() / 3.0,ndigits=2)
    
def get_student(name:str, chinese:int, english:int, math:int) -> Student:
    return Student(n=name,ch=chinese,en=english,ma=math)