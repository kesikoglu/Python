from statistics import mean


sayilar = [1,-1,45,2,12,3,0,874, 458,35]    #liste oluşturduk
siralisayilar = [a for a in range(15)]      # listedeki sayılar belli bir kurala göre ise mesela sıralı, 2 şer 2 şer gibi liste hesaplanarak oluşturulur
kareleri = [b**2 for b in range(25)]         # listedeki sayılar 0-15 arasında ve karelerinde oluşuyor
kupleri = [c**3 for c in range(4, 19, 2)]    # listedeki sayılar 4 den başlar 19 a kadar, 2 şer artarak giden sayıların küplerinden oluşuyor, 4-6-8... 64-216-512
hesapli = [d/2+d*d for d in range(15)]       # istenilen formül ile 
print("Sirali sayilar = ", siralisayilar)
print("Kareleri = ",kareleri)
print("Kupleri = ",kupleri)
print("Hesaplama = ", hesapli)

print()
print("Numbers are:")
for sayi in sayilar:    #döngü ile her bir listedeki sayıyı yazdırdık
    print(sayi, end=" / ")          #, end= olmaz ise sayılar alt alta yazılır. , end=" " içindeki ayırıcı ile boşluk, çizgi vs ile yan yana dizilir
print()
print("Sum=",sum(sayilar))      
print("Minimum=",min(sayilar))   
print("Maximum=",max(sayilar))
print("Mean=",mean(sayilar))

sayilar.append(99)          #append ile listenin sonuna sayı ekledik
sayilar.insert(3, 145)      # insert ile 3. sıraya sayı ekledik (ilk sıra 0, ikinci 1)
print(sayilar)
sayilar.pop(3)              # pop ile 3. indeksteki sayıyı sildik
print(sayilar)
sayilar.remove(-1)      # remove ile istenilen veri (değer) listeden silinir
print(sayilar)
sayilar.pop()       #pop default olarak son veriyi siler
print(sayilar)