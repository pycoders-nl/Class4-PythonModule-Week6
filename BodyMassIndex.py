

name=input("Adinizi giriniz? : ")
print("Boy Kilo Endeksi programina HOSGELDIN "+ name)
lenght=int(input(" Lutfen boyunuzu cm cinsinden yaziniz? : "))                 # Kullanicidan boy ve agirligini
if lenght > 230:                                                               # istiyoruz ve aldigimiz bilgilerle
    print("Boyunuz 230 cm den uzun olamaz!")                                   # benden kitle endeksini olusturuyoruz.
    lenght = int(input(" Lutfen boyunuzu cm cinsinden yaziniz? : "))           #if elif else kosullari ile de
weight=int(input("Lutfen kilonuzu yaziniz? : "))                               # kisinin hangi endekste oldugunu
body_mass_index= float(weight/((lenght/100)**2))                               # ekrana yazdiriyoruz.

if body_mass_index <= 25 :
    print("{} Boy Kilo Endeksin = {} \n -------- NORMAL ---------".format(name,body_mass_index))

elif 25 < body_mass_index <= 30 :
    print("{} Boy Kilo Endeksin = {} \n -------- FAZLA KILOLU ---------".format(name, body_mass_index))

elif 30 < body_mass_index <= 40:
    print("{} Boy Kilo Endeksin = {} \n -------- OBEZ ---------".format(name, body_mass_index))

else:
    print("{} Boy Kilo Endeksin = {} \n -------- ASIRI OBEZ ---------".format(name, body_mass_index))
