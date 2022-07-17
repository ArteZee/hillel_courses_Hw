"""
exchanger is a file where we save:
value: dict - where save currency-courses - availability
course_value - function  get currency - return curse and availability in exchanger
exchange_value - function get currency and amount - return curse and exchange to another currency
"""
import exchanger

"""
in this program you can set: 
COURSE USD - out put curse and availability
COURSE UAH - out put curse and availability
EXCHANGE UAH 100 -exchange to another currency your amount (can be any number)  
EXCHANGE USD 100 -exchange to another currency your amount (can be any number)  
STOP - stop program 
Ps: It does not meter in witch register write
"""
# get from user operation
user_data: str = input("Put your operation or STOP to exit: \n").upper()

while True:
    # user put stop - break
    if user_data == "STOP":
        break
    # get function course_value from exchanger
    if "COURSE" in user_data:
        print(exchanger.course_value(user_data.split()[1]))
    # get function exchange_value from exchanger
    if "EXCHANGE" in user_data:
        print(exchanger.exchange_value(user_data.split()[1], int(user_data.split()[2])))

    user_data = input("Put your operation or STOP to exit: \n").upper()
