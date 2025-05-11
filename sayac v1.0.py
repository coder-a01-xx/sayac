import time

while True:

    gün=int(input("Kaç gün : "))
    saat=int(input("Kaç saat : "))
    dk=int(input("Kaç dakika : "))
    sn=int(input("Kaç saniye : "))

    if sn>=60:
        eklencek=sn//60
        dk+=eklencek
        sn=sn%60

    
    if dk>=60:
        ek=dk//60
        saat+=ek
        dk=dk%60

    if saat>=24:
        ek1=saat//24
        gün+=ek1
        saat=saat%24

    while gün>=0:
        sn-=1

        if sn==-1:
            dk-=1
            sn+=60

        else:
            time.sleep(1)
            print(f"{gün} gün, {saat} saat, {dk} dakika, {sn} saniye kadlı.")


        if dk==-1:
            saat-=1
            dk+=60

        if saat==-1:
            gün-=1
            saat+=24

        if gün==0 and saat==0 and dk==0 and sn==0:
            print("Süre bitti")
            print("Uygulamamızı kullandığınız için teşekkür ederiz...")
            time.sleep(1)
            break