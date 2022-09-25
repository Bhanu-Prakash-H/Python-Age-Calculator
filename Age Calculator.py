# def AgeCalculator(y,m,d):
#     import datetime
#     today = datetime.datetime.now().date()
#     dob = datetime.date(y,m,d)
#     age = int((today-dob).days/365)
#     print(age)
# AgeCalculator(2000,7,25)

def Agecalculator(y,m,d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days/365)
    print(age)
Agecalculator(1999,2,2)
