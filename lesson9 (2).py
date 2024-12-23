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


