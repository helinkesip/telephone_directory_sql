import sqlite3

def Ad_ID(Ad, Soyad):
    cur.execute("SELECT KisiID FROM Kisiler WHERE Ad = ? AND Soyad = ?", (Ad, Soyad))
    return cur.fetchone()
    
def Tel_ID(Numara):
    cur.execute("SELECT KisiID FROM Numaralar WHERE Numara = ?", (Numara,))
    return cur.fetchone()
    
def Kisi_Ara(Numara):
    cur.execute("SELECT Ad, Soyad FROM Kisiler WHERE KisiID = ?", Tel_ID(Numara))
    return cur.fetchone()

def Tel_Ara(Ad, Soyad):
    cur.execute("SELECT Numara FROM Numaralar WHERE KisiID = ?", Ad_ID(Ad, Soyad))
    return cur.fetchall()
    
def Kisi_Ekle(Ad, Soyad):
    cur.execute("INSERT INTO Kisiler(Ad,Soyad) VALUES(?,?)", (Ad, Soyad))
    print(Ad,Soyad,"Kişisi tabloya başarıyla eklendi.")

def Tel_Ekle(Ad, Soyad, Numara):
    cur.execute("INSERT INTO Numaralar VALUES(?,?)", (Ad_ID(Ad, Soyad)[0], Numara))
    print(Ad,Soyad,"Kişisine",Numara,"numarası başarıyla eklendi.")

def Tel_Sil(Numara):
    cur.execute("DELETE FROM Numaralar WHERE Numara=?", (Numara,) )
    print(Numara,"numarası var ise başarıyla silindi.")

def Kisi_Sil(Ad, Soyad):
    cur.execute("DELETE FROM Kisiler WHERE KisiID=? " ,Ad_ID(Ad,Soyad))
    cur.execute("DELETE FROM Kisiler WHERE Ad=? AND Soyad=?",(Ad,Soyad))

def Tel_güncelle(Eski_No, Yeni_No):
    cur.execute("UPDATE Numaralar SET Numara=? WHERE Numara=?", (Yeni_No,Eski_No))
    print(Eski_No, "numarası", Yeni_No, "numarası ile değiştirildi.")

def Kisi_güncelle(Eski_ad,Yeni_ad,Eski_soyad,Yeni_soyad):
    cur.execute("UPDATE Kisiler SET Ad= ? AND Soyad=? WHERE Ad=? AND Soyad=?",(Yeni_ad,Yeni_soyad,Eski_ad,Eski_soyad))
    print(Eski_ad ,Eski_soyad , "kişisi" , Yeni_ad, Yeni_soyad, "kişisine güncellendi." )

con=sqlite3.connect("rehber.db", isolation_level=None)
cur= con.cursor()
cur.execute("CREATE TABLE IF NOT EXIST Kisiler(KisiID INTEGER PRIMARY KEY, Ad, Soyad)")
cur.execute("CREATE TABLE IF NOT EXIST Numaralar(KisiID INTEGER, Numara )")


while True:
    print("""
 Telefon Numaraları Veri Tabanı
  1) Arama
  2) Ekleme			
  3) Silme
  4) Güncelleme
  5) Çıkış
    """)

    islem_secim= input("Seçmek istediğiniz işlemin numarasını giriniz: ")

    if islem_secim == "1":
        print("Numaraya göre kişi aramak için 1, isme göre numara aramak için 2'ye basınız.")
        tur_secim = input()
        
        if tur_secim == "1":
            numara = input("Arayacağınız kişinin telefonunu giriniz: ")
            try: 
                ad, soyad = Kisi_Ara(numara)
                print(numara,"numarası",ad,soyad,"kişisine aittir.")
            except:
                print("Böyle bir numara yoktur.")
            
        elif tur_secim == "2":
            ad_soyad = input("Arayacağınız kişinin adını ve soyadını giriniz: ").split()
            try:
                numaralar = Tel_Ara(ad_soyad[0],ad_soyad[1])
                print(' '.join(ad_soyad),"kişisinin numaraları şunlardır:")
                for numara in numaralar:
                    print("\t"+numara[0])
            except:
                print("Böyle bir kişi yoktur.")
            
    elif islem_secim == "2":
        print("Yeni numara eklemek için 1, yeni kişi eklemek için 2'ye basınız.")
        tur_secim = input()
        
        if tur_secim == "1":
            numara = input("Ekleyeceğiniz numarayı giriniz: ")
            ad_soyad = input("Numaranın sahibi kişinin adını ve soyadını giriniz: ").split()
            try: Tel_Ekle(ad_soyad[0],ad_soyad[1],numara)
            except: print("Böyle bir kişi yoktur.")
            
        elif tur_secim == "2":
            ad_soyad = input("Ekleyeceğiniz kişinin adını ve soyadını giriniz: ").split()
            try: Kisi_Ekle(ad_soyad[0],ad_soyad[1])
            except: print("Kişi eklenememiştir. Lütfen ad ve soyad arasında bir boşluk bırakınız.")
            
    elif islem_secim == "3":
        print("Numara silmek için 1, kişi silmek için 2'ye basınız.")
        tur_secim = input()
        
        if tur_secim == "1":
            numara = input("Sileceğiniz numarayı giriniz: ")
            try: Tel_Sil(numara)
            except: print("Böyle bir numara yoktur.")
            
        elif tur_secim == "2":
            ad_soyad = input("Sileceğiniz kişinin adını ve soyadını giriniz: ").split()
            try: Kisi_Sil(ad_soyad[0],ad_soyad[1])
            except: print("Böyle bir kişi yoktur.")
        
    elif islem_secim == "4":
        print("Numara güncellemek için 1, kişi güncellemek için 2'ye basınız.")
        tur_secim = input()
        
        if tur_secim == "1":
            numara = input("Güncelleyeceğiniz numarayı giriniz: ")
            yeni_numara = input("Numaranın yeni değerini giriniz: ")
            try: Tel_Guncel(numara,yeni_numara)
            except: print("Böyle bir numara yoktur.")
    
        elif tur_secim == "2":
            ad_soyad = input("Güncelleyeceğiniz kişinin adını ve soyadını giriniz: ").split()
            yeni_ad_soyad = input("Kişinin yeni adını ve soyadını giriniz: ").split()
            try: Kisi_Guncel(ad_soyad[0],ad_soyad[1],yeni_ad_soyad[0],yeni_ad_soyad[1])
            except: print("Böyle bir kişi yoktur.")
            
    elif islem_secim == "5":
        print("Veritabanından çıkılıyor...")
        break



