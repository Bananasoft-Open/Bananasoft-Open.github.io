while True:
    print("\n--- Veri Dönüştürücü ---")
    print("1 - Bit -> Byte")
    print("2 - Bit -> Kilobit")
    print("3 - Bit -> Kibibit")
    print("0 - Çıkış")

    secim = input("Dönüştürücü Seçin (0/1/2/3): ")

    if secim == "0":
        print("Programdan çıkılıyor...")
        break

    if secim in ["1", "2", "3", "4"]:
        try:
            bit = int(input("Bit Değeri Girin (Tam Sayı): "))

            if bit < 0:
                print("Hata: Bit değeri negatif olamaz!")
                continue

            if secim == "1":
                print(f"Sonuç: {bit / 8} Byte")
            elif secim == "2":
                print(f"Sonuç: {bit / 1000} Kilobit")
            elif secim == "3":
                print(f"Sonuç: {bit / 1024} Kibibit")

        except ValueError:
            print("Hata: Yarım bit olmaz! Lütfen tam sayı girin.")
    else:
        print("Hata: Geçersiz seçim yaptınız!")
