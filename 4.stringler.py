text=" Hello, World! "

#? in
print("ello" in text) #* String text'in içinde varsa True yoksa False döner

#? not in
print("ello" not in text) #* String text'in içinde yoksa True yoksa False döner

#? [Başlangıçindeksi,Bitişindeksi]
print(text[2:7])
#? [-Bitişindeksi,-Başlangıçindeksi]
print(text[-4:-1])

#? -------------STRİNG METOTLAR-------------

#? len
print(len(text)) #* Uzunluk döner

#? upper()
print(text.upper()) #* Büyük harfe dönüştürür

#? lower()
print(text.lower()) #* Küçük harfe dönüştürür

#? strip()
print(text.strip()) #* Sağdan soldan boşlukları kaldırır

#? replace()
print(text.replace("l","v")) #* l stringini v stringi ile değiştirir

#? split()
print(text.split(",")) #* ,'den böler(liste(dizi) döner)

#? capitalize()
print("hdslfh".capitalize()) #* stringin ilk harfini büyük harfe dönüştürür

#? casefold()
print(text.casefold()) #* Küçük harfe dönüştürür, lower'den farkı yok sadece daha fazla harfe dönüştürür ve daha yavaş çalışır

#? title()
print("sELAM DÜNYA".title()) #* Stringin baş harfleri büyük diğer harfleri küçük yazar veya rakamdan sonraki harfi de büyük harfle yazar

#? swapcase()
print("Selam Dünya".swapcase()) #* Stringin baş harfleri küçük diğer harfleri büyük yazar

#? islower()
print("result".islower()) #* tüm string küçükse True yoksa False döner

#? isupper
print("RESULT".isupper()) #* tüm string büyükse True yoksa False döner

#? center(StringinToplamUzunluk,SağaVeSolaNeGelecek)
print("Hello World!".center(20,"*"))
