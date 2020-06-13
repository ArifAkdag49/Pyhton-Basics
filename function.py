
def slm():
    print("selam") 
    print("herkese")
    
slm()



def kareal(x):
    print(x**2)

    kareal(2)
kareal(8)    


# bilgi notu cikti üretmek

def kare_al(x):
    print("girilen sayinin karesi:"
          + str(x**2))
    
    
    kare_al(3)
            
    
    
    
def kare_al(x):
    print("girilen sayi:"+ 
          str(x)+
          " karesi:"+
          str(x**2))
    
    
    kare_al(3)



# iki argümanli fuction tanimlama



def carpma_yap(x, y):
    print(x*y)
    
 
carpma_yap(2,3)




#argümanlarin siralanmasi

cyrpma_yap(x=2,y=3)
crpma_yap(3,2)
#islemi yapar sirayi 
# unutmus oalbilirsin                    
    
    
# isi , nem , sarj 
#bir sehir sk. lamba verisi var 


40,25,90


def direk_hesap(isi, nem,sarj):
    print((isi + nem)/sarj)
    

direk_hesap(40,25,90)

#return  ciktiyi sonra kullanir.
#ciktiyi geri cagiri

def direk_hesap(isi, nem,sarj):
    return isi + nem/sarj


direk_hesap(40,25,90)
cikti=direk_hesap(40,25,90)

direk_hesap(40,25,90)*10



####   if #####

sinir=5000

if sinir>4500:
    print(sinir*9)


sinir=5000
gelir=6000
gelir=int(input())

if gelir>sinir:
    print("tebrikler")
    
elif gelir<sinir:
     print("daha cok calis")

else:
    print("takibe devam")


print(gelir)


,

















    
    
    
    


