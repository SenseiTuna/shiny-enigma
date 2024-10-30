sayi1=1
sayi2=1

kactane=int(input("Kaça tane fibonacci sayısı bulmak istiyorsunuz?\n"))

i=0
if kactane>2:
    print("\n1\n1")
    while i<kactane-2:
        print(sayi1+sayi2)
        sayi1=sayi1+sayi2
        i+=1
        if i==kactane-2:
            break
        print(sayi1+sayi2)    
        sayi2=sayi1+sayi2
        i+=1
else:
    print("2'den küçük bir değer girmeyiniz!")