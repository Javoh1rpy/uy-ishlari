# import lesson10_functions
#
#
# avto1 = lesson10_functions.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# lesson10_functions.info_print(avto1)
#########______________________
import calendar
# from math import pow
# from lesson10_functions import pow as pw

# import lesson10_functions as aim # avto_info_mod ni qisqa nom aim bilan chaqiramiz
# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_print(avto1)

#########______________________

# from lesson10_functions import avto_info, info_print
#
# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)
#########______________________
# from lesson10_functions import *
# from math import *
#
# qiymat=sin(90)
# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)
#########______________________
# import math
# print(math.pow(2,2))
#########______________________
# from math import *  ##hamma function chaqirish
# print(pow(2,3))


#########______________________
from math import fabs, ceil, floor, sin
# print((abs(-3.3)))
# print((fabs(-3.3)))
# print((ceil(3.4)))  ##ceil ozidan katta int gacha yaxlitlaydi
# print((floor(3.4)))  ##floot o'zidan kichik birinchi int gacha yaxlitlaydi
# print(sin(360))
#########______________________
# import random as r # random modulini r deb chaqirayapmiz
#
# son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
# print(son)
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz
#########______________________
# from datetime import datetime
# print(datetime.now())

# from datetime import datetime
# # print(datetime.now())
# date = datetime(2024, 12, 11, 15, 30, 45)
# print(date)
# print(type(date))

########_____________
# from datetime import datetime
# date = datetime(2024, 12, 11, 15, 30, 45)
# xx="2024-12-11 15:30:45"
# formatted = date.strftime("%Y-%m-%d %H:%M:%S")  #######datetime farmatdan str ga o'tgazish
# print(formatted)  # e.g., 2024-12-11 15:30:45
# print(type(formatted))  # e.g., 2024-12-11 15:30:45
########_____________
# from datetime import datetime
# now = datetime.now()
# date = datetime(2024, 12, 11, 15, 30, 45)
# #
# date_only = now.date()  # Get the date part
# time_only = now.time()  # Get the time part
# zonasi = now.timetz()  # Get the time part
# print(date_only,"    " ,time_only,"    ",zonasi)
######_______________
from datetime import datetime, timedelta
#
# hozigi_vaqt = datetime.now()
# yangi_vaqt = hozigi_vaqt + timedelta(days=2,hours=2)
# print(hozigi_vaqt)
# print(yangi_vaqt)

####uy ishi for ichida orqaga sanasin no boguncha.timedelta orqali yasang,fay oling soatni.

# date1 = datetime(2024, 11, 11)
# date2 = datetime(2024, 12, 25)
# delta = date2 - date1
# print(delta.days)  #

#####uy ishi necha kun yashaganini aniqlash.

# import calendar
# qiymat=calendar.SATURDAY
# print(qiymat)
# Hafta kunlari nomlarini olish (dushanbadan boshlanadi)
# weekdays = list(calendar.day_name)
# print(weekdays)  # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

########_________________
# import calendar
# yil=2024
# oy=2
# # print(calendar.month(yil,oy))
# print(calendar.month(2004,3))


#########__________________

# qiymat = lambda p, r : 2*p/22*r
# print(qiymat(3,10))
# print(qiymat(3,1000))
#######_________________
# product = lambda x, y : x ** y
# print(product(3, 2))

###________________
# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
        # yigindi += son
    # return yigindi
# print(summa(1,2,34,23,12,23454231,45342142,-12321))


# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
#
# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000,egasi="nomalum")
# print(avto1)
# print(avto2)







