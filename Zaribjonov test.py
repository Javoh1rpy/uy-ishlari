
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
#     ism=input(f"Talabaning ismini kiriting : ")
#     baho=float(input(f"{ism}ning bahosini kiriting: "))
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
# print(is_prime(39))
# print(is_prime(2))


####7-misol
# from datetime import datetime
# hozirgi_vaqt = datetime.now()
# format = hozirgi_vaqt.strftime("%d-%m-%Y %H:%M:%S")
# print(f"Hozirgi sana va vaqt:", format)