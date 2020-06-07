9
9.2
'HELLO YAPAY ZEKA'
a='HELLO YAPAY ZEKA'
dt='HELLO YAPAY ZEKA'
len(dt)
# srtring metotlari -upper & lover
# duzenlemeler yapar
dt.upper()
dt.lower()
dt.upper()
dt.islower()


#strıng metotlar- replace 
#ıcerdekılerı duzeltir (e-a)
dt=('hello yapay zeka')
dt='hello yapay zeka'
dt.replace('e','a')


# strıng metotlar- strip
# streifen  bosluk vs. özel ıstek değısım

dt=' hello yapay zeka '

dt.strip()
dt='*hello yapay zeka*'
dt.strip('*')



# dir screiben dt ye uygulanacak butun ugulamalar cıkar
# dt. kan mann screiben zu erstehen(ortaya cıkar)
dir(dt)

dt.swapcase()
dt.title()


#SUBSTRING
#() ıcerdekılerden alt bırmı sorgula
 
dt='hello yapay zeka'

dt[0]

dt[5]
# bosluklarda sayılır
 
# 0-dan 3 e kadar 
dt[0:3]
dt[3:7]
# 3 den baslar 7 e kadar

# degıskenler
a=9

# type - dönüşümlerı
#ınput kullanıcıdn bılgı alır

tplm1=10
tplm2=20

tplm1 + tplm2

11.2
int(11.0)
# vırgulden son sını atar

11
float(11)

type(str(12))
#ınt.- str ye dönüstrdü

# prınt
dt='hello yapay zeka'
print(dt)
print('hello yapay zeka')
print('hello deutsch')
print('hello','deutsch', sep='_')

print()
#parantezı yazarken nasıl ıslemler yapar kısmı gelır 
#gelmesse
#?print   calıstır 
?print
# öyellıklerı sol altta yazar




# verı yapılari

#lısteler 
#degıstırıleılır,sıralı,kapsayıcı

notlar=[50,60,70,90]
type(notlar)

liste=['a',1.2,30]
len(liste)


type(liste[0])
type(liste[1])
type(liste[2])

tumliste=[liste,notlar]
#ıkı lısteyı bırlestırdı


#sılme ıslemı
#del liste (calıstır de sılınmıs olur)

#Liste ve elaman islemlerı

liste=[10,20,30,40,50]

liste[0]
liste[5]
#hata verdı (o,1,2,3,4) eleman sayısı bukadar

liste[:3]
# 3 e kadar

liste[2:]
# 2 den son a kadar

yeniliste=['a',10,[20,30,40,50]]

# 30 a nasıl ulaırsın?

yeniliste[2]
yeniliste[2][1]


#liste degisimi

liste=["ali","veli","berkcan","ayse"]


liste[0:3]="alinin_babasi","velinin_babasi","bercan_abasi"

liste


liste=["ali","veli","berkcan","ayse"]
 
#listeye ekleme yaplmasi

liste=liste+["kemal"]
liste

#lsteden silme

del liste[4]

liste



#liste metotlari

dir(liste)
  
#sagda liste metotlari cikti

#append



liste=["ali","veli","berkcan","ayse"]

liste.append("sefa")

#append sefayi listeye ekledi


liste
 
#remove

liste.remove("sefa")
liste
 #sefayi sildi
