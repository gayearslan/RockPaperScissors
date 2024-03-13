import random
can=3
puan=0
secenekler=["tas","kagit","makas"]
while(can!=0):
    bilgHamle=random.choice(secenekler)
    x=input("tas,kagit,makas?\n")
    if(bilgHamle==x):
        print("bilgisayar hamlesi:"+bilgHamle)
        print("berabere")
    elif(x=='tas'):
        if(bilgHamle=='kagit'):
            print("bilgisayar hamlesi:"+bilgHamle)
            print("kaybettiniz!")
            can-=1
        elif(bilgHamle=='makas'):
            print("bilgisayar hamlesi:"+bilgHamle)
            print("kazandiniz!")
            puan+=10
    elif(x=='kagit'):
        if(bilgHamle=='tas'):
            print("bilgisayar hamlesi:"+bilgHamle)
            print("kaybettiniz!")
            can-=1
        elif(bilgHamle=='makas'):
            print("bilgisayar hamlesi:"+bilgHamle)
            print("kazandiniz!")
            puan+=10
    elif(x=='makas'):
        if(bilgHamle=='tas'):
            print("bilgisayar hamlesi:"+bilgHamle)
            print("kaybettiniz!")
            can-=1
        elif(bilgHamle=='kagit'):
            print("bilgisayar hamlesi:"+bilgHamle)
            print("kazandiniz!")
            puan+=10
    else:
        print("lutfen gecerli bir secim yapiniz.")

