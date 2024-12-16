# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 23:14:42 2024

@author: rabia
"""

def main():
    max_ürün_sayısı=100
    ürünler=[]
    fiyatlar=[]
    
    while True:
        print("/n Market Otomaasyonu menüsü:")
        print("1. Ürün Ekle")
        print("2.Ürün Sat")
        print("3. Fiyat Güncelle")
        print("4.Fiyat Hesapla")
        print("5. Çıkış")
        secim=input("Seçiminizi yapın(1-5):")
        
        if secim=="1":
            if len (ürünler)>=max_ürün_sayısı:
                print("Maksimum ürün sayısına ulaşıldı.")
                continue
            
            ürün_adı=input("Ürün adı girin:")
            fiyat_str=input("Ürün fiyatını girin:")
            
            while True:
                try:
                    ürün_fiyatı=float(fiyat_str)
                    break
                except ValueError:
                    print("lütfen geçerli bir fiyat girin:")
                    fiyat_str=input("Ürün fiyatını girin:")
            
            ürünler.append(ürün_adı)
            fiyatlar.append(ürün_fiyatı)
            print("Ürün eklendi.")
            
        elif secim=="2":
            ürün_adı=input("Satmak istediğiniz ürünün adını girin:")
            bulundu=False
            
            for i in range(len(ürünler)):
                if ürünler[i].lower()==ürün_adı.lower():
                    print(f"{ürün_adı} satıldı,fiyat:{fiyatlar[i]} TL")
                    bulundu=True
            if  not bulundu:
                print("Ürün bulunamadı.")
            
        elif secim=="3":
            ürün_adı=input("Güncellemek iatediğiniz ürünü adımı giriniz:")
            bulundu=False
            
            for i in range(len(ürünler)):
                if ürünler[i].lower()== ürün_adı.lower():
                    yeni_fiyat_str=input("Yeni fiyat girin:")
                    
                    while True:
                        try:
                            yeni_fiyat=float(yeni_fiyat_str)
                            break
                        except ValueError:
                            print("Lütfen geçerli bir fiyat giriniz.")
                            yeni_fiyat_str=input("Yeni fiyatı giriniz:")
                    
                    fiyatlar[i]=yeni_fiyat
                    bulundu=True
                    print("Fiyat güncellendi.")
                    
            if not bulundu:
                print("Ürün bulunamadı.")
            
        elif secim=="4":
            toplam_tutar=0
            print("Fatura hesaplamak için satılan ürünlerin isimlerini girin(çıkmak için 'q' girin):")
            
            while True:
                ürün_adı=input()
                if ürün_adı=="q":
                    break
                
                bulundu=False
                for i in range(len(ürünler)):
                    if ürünler[i].lower()==ürün_adı.lower():
                        toplam_tutar +=fiyatlar[i]
                        bulundu=True
                if not bulundu:
                    print("Ürün bulunamadı.")
                    
                print(f"Toplam Fatura tutarı:{toplam_tutar} TL")
                
        elif secim=="5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")
if __name__=="__main__":
    main()
            