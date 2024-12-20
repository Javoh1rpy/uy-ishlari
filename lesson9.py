# def salom_ber():
#     """Salom beruvchi funksiya"""
#         #description bu
#     print("Assalomu alaykum!")
#
# def salom_berma():
#     print("bermiymAAN SALOM")
#
# while True:
#     salom_berma()
import datetime

######__________________________________
#
# def salom_ber(ism):
#     if not isinstance(ism,str):
#         print("xato !!")
#     else:
#         print(f"Assalomu alaykum, hurmatli {ism.title()}!")
#
# salom_ber('alisher')  # argument ketyapti
####__________________________________
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
#
# toliq_ism(familiya='axmadov',ism='alisher')

# _______________
# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda")
#
# yosh_hisobla(2002,'ali')
####___________________
# def yosh_hisobla(tugilgan_yil, joriy_yil=2024): # joriy yil uchun st.qiymat 2020
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#
# yosh_hisobla(2002)
# yosh_hisobla(2002,2025)

###______________________
# def yosh_hisobla(tugilgan_yil, joriy_yil=2024):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")
#
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# # print(type(tyil))
# yosh_hisobla(tyil)

#####________________________________
# def bizzi_summa_funksiyamiz(x,y,z):
#     print(x+y+z)
#
# son1=int(input('sonni kiriting:  '))
# son2=int(input('sonni kiriting:  '))
# son3=int(input('sonni kiriting:  '))
#
# bizzi_summa_funksiyamiz(100,son2,son3)
# bizzi_summa_funksiyamiz(100,z=son2,y=son3)
###########_________________________
# def bizzi_summa_funksiyamiz(x, y, z):
#     summm = x + y + z
#     return summm  #return bu funksiyani javobi
#
# qiymat = bizzi_summa_funksiyamiz(4, 3, 1)
# print(qiymat)
###########_________________________
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'company':kompaniya,
#             'model':model,
#             'color':rangi,
#             'korobka':korobka,
#             'year':yili,
#             'price':narhi}
#     return avto
#
# # avto_dict=avto_info('GYM','cobalt','oq','mexanika',2025,)
# avto_dict=avto_info('GYM','cobalt','oq','mexanika',2025,narhi=12000)
# print(avto_dict)
#######_____________________

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'company':kompaniya,
#             'model':model,
#             'color':rangi,
#             'korobka':korobka,
#             'year':yili,
#             'price':narhi}
#     return avto
#
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#
#     # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
#     # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
#
# print(avtolar)
#######_____________________

# def bahola(ismlar):
#     baholar = {}
#
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#
#     return baholar
#
# talabalar_ismlari = ['ali', 'vali', 'hasan', 'Husan']
# xx = bahola(ismlar=talabalar_ismlari)
# print(xx)
####__________________

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
#
# ismlar = ["ali", "vali", "hasan", "husan"]
# katta_harf(ismlar)
# print(ismlar)


# def tugilgan_yil_hisoblash():
#     ism = input("Ismingizni kiriting: ")
#     yosh = int(input("Yoshingizni kiriting: "))
#     tugilgan_yil = 2024 - yosh
#     print(f"{ism} sizning tug'ilgan yilingiz: {tugilgan_yil}")
# tugilgan_yil_hisoblash()


# def kvadrat_kub():
#     son = int(input("istalgan sonni kiriting: "))
#     kub=son**3
#     kvadrat=son**2
#     print(f"{son} ning kubi {kub} kvadrati {kvadrat}")
# kvadrat_kub()

# def toq_juftligi():
#     son=int(input("Istalgan sonni kiriting: "))
#     if son%2==0:
#         print(f"{son} juft son!")
#     else:
#         print(f"{son} toq son!")
# toq_juftligi()


# def kotta_kichik():
#     son1=int(input("1-sonni kiriting: "))
#     son2=int(input("2-sonni kiriting: "))
#     if son2>son1:
#         print(f"{son2} {son1} dan katta!")
#     elif son1>son2:
#         print(f"{son1} {son2} dan katta!")
#     else:
#         print("BU sonlar teng")
# kotta_kichik()


# def daraja():
#     x=int(input("x sonini kiriting: "))
#     y=int(input("y sonini kiriting: "))
#     kub=x**y
#     print(f"{x} ning {y} darajasi {kub} ga teng")
#
# daraja()



# def bolinish(son):
#     for i in range(2, 11):
#         if son % i == 0:
#             print(f"{son} {i} ga bo'linadi.")
#         else:
#             print(f"{son} {i} ga bo'linmaydi.")
#
# son1 = int(input("Sonni kiriting: "))
# bolinish(son1)


#
# def javohir(ismim, familiyam, tugilgan_yil, tugilgan_joy,  email=None, telefon=None):
#     yosh=2024-tugilgan_yil
#     return { "Ismim": ismim,"Familiyam": familiyam, "Tug'ilgan yili": tugilgan_yil,
#         "Tug'ilgan joyi": tugilgan_joy,"Yosh": yosh,"Email": email,"Telefon": telefon }
# malumotlar = javohir(ismim="Javohir", familiyam="Zaribjonov", tugilgan_yil=2004,tugilgan_joy="QOQON", email="javoX@gmail.com")
# print(malumotlar)

# while True:
#
#       def javohir(ismim, familiyam, tugilgan_yil, tugilgan_joy,  email=None, telefon=None):
#        yosh=2024-tugilgan_yil
#        return { "Ismim": ismim,"Familiyam": familiyam, "Tug'ilgan yili": tugilgan_yil,
#         "Tug'ilgan joyi": tugilgan_joy,"Yosh": yosh,"Email": email,"Telefon": telefon }
#       malumotlar = javohir(ismim="Javohir", familiyam="Zaribjonov", tugilgan_yil=2004,tugilgan_joy="QOQON", email="javoX@gmail.com")
#       print(malumotlar)
#       mijoz=[]
#       mijoz.append(malumotlar)
#       print(f"mijoz={mijoz}")



# def kottasi():
#     my_list=[]
#     a=int(input("1-sonni kirit: "))
#     my_list.append(a)
#     b=int(input("2-sonni kirit: "))
#     my_list.append(b)
#     c=int(input("3-sonni kirit: "))
#     my_list.append(c)
#     maxx_son=my_list[0]
#     for i in range(len(my_list)):
#         if(my_list[i]>maxx_son):
#             maxx_son=my_list[i]
#     print(f"{maxx_son} eng katta son")
# kottasi()


# def kattasi():
#     a = int(input("1-sonni kirit: "))
#     b = int(input("2-sonni kirit: "))
#     c = int(input("3-sonni kirit: "))
#     if a>b>c and a>c>b:
#         print(a)
#     elif  b>a>c and b>c>a:
#         print(b)
#     else:
#         print(c)
#
#
# kattasi()

# def kopaytma(number):
#     while True:
#      if (number>=0):
#         sum=1
#         sum*=number
#     print (sum)
# a=int(input("son kiriting; "))
# print(kopaytma(a))

# def kopaytma():
#     Kopaytma = 1
#     while True:
#         son = int(input("Sonni kiriting (to'xtatish uchun 0 kiriting ): "))
#         if son!=0:
#             Kopaytma *= son
#         else:
#             break
#     return Kopaytma
# print(kopaytma())


# def kopaytma():
#     Kopaytma = 1
#     while True:
#         son = (input("Sonni kiriting (to'xtatish uchun 'exit' kiriting ): "))
#         if  son==str('exit') :
#             Kopaytma *= son
#             break
#     return Kopaytma
# kopaytma()



#### Uyga vazifa



# import datetime
#
# from lesson10 import students

# from datetime import datetime
# now = datetime.now()
# print(f"Hozirgi vaqt : {now}")
# x=int(input("Tugulgan yilingizni kiriting: "))
# y=int(input("Tugulgan oyingizni  kiriting: "))
# c=int(input("Tugulgan kuningizni kiriting: "))
# date1 = datetime.now()
# date2 = datetime(x, y, c)
# delta = date1 - date2
# print(f"Siz {delta.days} kun yashagansiz")



# from datetime import datetime, timedelta
# now = datetime.now()
# minus = timedelta(hours=1)
# while now > datetime.min:
#     print(now)
#     now -= minus
# if now <= datetime.min:
#     print("Tugadi !")


# x, y, z = "Olma", "Banan", "Nok"
# print(x)
# print(y)
# print(z)


#
# a = """ 1
#  1  2
#  1  2  3
#  1  2  3  4
#  1  2  3  4  5"""
# b = ''' A
#  B  B
#  C  C  C
#  D  D  D  D
#  E  E  E  E  E'''
# print(a)
# print(b)


# a = "Bor"
# b = "Markaziy Osiyo"
# print (a.replace("r", "y"))
# print (b.replace("Markaziy", "O'rta"))
#
# txt = "Olmaxon yerdagi olmani olib ketdi"
# x = "ol" in txt
# print(x)
#
# yosh = 21
# matn = "Mening yoshim {} da"
# print(matn.format(yosh) )

# narx = 30
# satr = "Mahsulot narxi {} so'm"
# print(satr.format(narx))

####1-misol


# matn = input("Biror matn kiriting: ")
# belgilar_soni = len(matn)
# katta_matn = matn.upper()
# print(f"Belgilar soni: {belgilar_soni}")
# print(f"Katta harflarda matn: {katta_matn}")




###2-misol
# yosh=int(input("Yoshingizni kiriting: "))
# if yosh >= 18:
#     print("Siz ovoz berishingiz mumkin!")
# else:
#     print("Siz hali ovoz bera olmaysiz.")


####3-misol
# royxat = list(range(1, 11))
# tuple_royxat = tuple(royxat)
# yigindi = sum(tuple_royxat)
# print("Tuple:", tuple_royxat)
# print("Yigindisi:", yigindi)

####4-misol
# def sonlar_kvadrati(sonlar):
#     return [son ** 2 for son in sonlar]
# son1=[12,56,1.25]
# print(sonlar_kvadrati(son1))


###5-misol
# student = {}
# for  i in range(3):
#     ism=input(f"Talabaning ismini kiriting {i+1}: ")
#     baho=float(input(f"{ism} talabaning bahosini kiriting: "))
#     student[ism]=baho
# yuqori_baho=max(student, key=student.get)
# print(f"Eng yuqori baho : {yuqori_baho} {student[yuqori_baho]}")






####6-misol
# def is_prime(n):
#     if n<=1:
#         return False
#     if n<=3:
#         return True
#     if n%2==0 or n%3==0:
#         return False
#     i=5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
# print(is_prime(39))
# print(is_prime(2))



####7-misol
# from datetime import datetime
# hozirgi_vaqt = datetime.now()
# format = hozirgi_vaqt.strftime("%d-%m-%Y %H:%M:%S")
# print("Hozirgi sana va vaqt:", format)

#
# kun_raqami = int(input("Haftaning kun raqamini kiriting (1-7): "))
# kunlar = {
#     1: "Dushanba",
#     2: "Seshanba",
#     3: "Chorshanba",
#     4: "Payshanba",
#     5: "Juma",
#     6: "Shanba",
#     7: "Yakshanba"
# }
# if 1 <= kun_raqami <= 7:
#     print(f"{kun_raqami} - {kunlar[kun_raqami]}")
# else:
#     print("Iltimos, 1 dan 7 gacha bo'lgan raqam kiriting!")


# def DigitCountSum(n):
#     raqamlar_soni = len(str(n))
#     raqamlar_yigindisi = sum(int(raqam) for raqam in str(n))
#     return raqamlar_soni, raqamlar_yigindisi
# natural_son = int(input("Natural sonni kiriting: "))
# soni, yigindisi = DigitCountSum(natural_son)
#
# print(f"Raqamlar soni: {soni}")
# print(f"Raqamlar yig'indisi: {yigindisi}")


# a = float(input("Birinchi tomon uzunligini kiriting: "))
# b = float(input("Ikkinchi tomon uzunligini kiriting: "))
# c = float(input("Uchinchi tomon uzunligini kiriting: "))
# if a == b == c:
#     print("Uchburchak teng tomonli.")
# elif a == b or a == c or b == c:
#     print("Uchburchak teng yonli.")
# else:
#     print("Uchburchak turli tomonli.")


# def raqamlar_yigindisi(n):
#     if n == 0:
#         return 0
#     return n % 10 + raqamlar_yigindisi(n // 10)
# son = 7564532
# natija = raqamlar_yigindisi(son)
# print(f"{son} sonining raqamlar yig'indisi: {natija}")

#
# sozlar=['soz','yangi','kotta']
# check =list( map(lambda x: x.upper(), sozlar))
# print(check)


# sozlar = ["salom", "dunyo", "Python", "filter", "misol"]
# axarfi = list(filter(lambda x: "a" in x  , sozlar))
# print(axarfi)



# sonlar = list(map(lambda x: x, range(10, 21)))
# print(sonlar)



#
# def yangi_mahsulot():
#     mahsulotlar = {}
#     while True:
#         product = input("Mahsulot (yoki 'stop'): ")
#         if product == 'stop':
#             break
#         mahsulotlar[product] = input(f"{product} narxi: ")
#     print(mahsulotlar)
# yangi_mahsulot()


# e_bozor = {
#     "olma": 10000,
#     "banan": 15000,
#     "uzum": 20000,
#     "apelsin": 18000,
# }
# buyurtma = ["olma", "banan", "anor", "apelsin"]
# for mahsulot in buyurtma:
#     if mahsulot in e_bozor:
#         print(f"{mahsulot}: {e_bozor[mahsulot]} so'm")
#     else:
#         print(f"{mahsulot}: Bizda bu mahsulot yo'q")
#


#
# for i in range(1, 100):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# for i in range(1,10):
#     print((chr(64 + i) + " ") * i)













