agirlik = float( input("Lütfen ağırlığınızı giriniz (kg): ") )
#         ^ bir sayı olması gereken bir girdi alıyoruz.
boy = float( input("Lütfen boyunuzu giriniz (cm):") )
boy = boy / 100.0  # metreye çevirdik
bki = agirlik / (boy * boy)
print("BKİ değeri: ", bki)
if bki <18.5 or bki>25:
    yeni_kilo = (boy * boy * 23) - agirlik #sağlıklı olduğu aralıktan ideal bir kilo seçerek farkına bakıp kilo alması ya da vermesi gereken miktarı hesaplıyorum
if bki <18.5:
    print("Zayıfsınız")
    print("Sağlıklı biçimde kilo alabilirsiniz")
    print(yeni_kilo ,"kadar kilo almanız gerekiyor")
    if boy<1.40:
         # Belki de çocuk?
         print("Çocuklar için BKİ formülü farklıdır.")         
elif bki < 25:
    print("Sağlıklısınız")
elif bki <30:
    print("Az kilolusunuz")
    print(yeni_kilo * (-1) ,"kadar kilo vermeniz gerekiyor")
elif bki<35:
    print("Dikkat! 1. Obez")
    print(yeni_kilo * (-1),"kadar kilo vermeniz gerekiyor")
elif bki<40:
    print("Dikkat! 2. Obez")
    print(yeni_kilo * (-1),"kadar kilo vermeniz gerekiyor")
else:
    print("Dikkat 3. Obez")
    print(yeni_kilo * (-1),"kadar kilo vermeniz gerekiyor")