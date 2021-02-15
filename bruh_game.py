import time

# Uygulamanın başlaması için gereken kodlar

oyunAdi = "Bruh Game"
sayac = 1
loading_element = "|"
game = 0

print(oyunAdi + "'e Hoşgeldin!")
time.sleep(2)


# Fonksiyonlar


# Oyunu Başlatma Fonksiyonu
def load_game():
    global sayac, game, load_game

    while sayac <= 3:

        if game == 1:
            break
        game = game + 1

        sayac = sayac + 1
        loading_element = "|"
        print("Loading... " + loading_element)
        time.sleep(0.3)
        loading_element = "/"
        print("Loading... " + loading_element)
        time.sleep(0.3)
        loading_element = "-"
        print("Loading... " + loading_element)
        time.sleep(0.3)
        loading_element = '\\'
        print("Loading... " + loading_element)
        time.sleep(0.3)
        print("\n")


        # Konuşma Fonksiyonu ve konuşmanın kendisi
        def start_talk():
            print("Sıkıcı bir hayatın var\n")
            time.sleep(2)
            print("Sabah uyan, hazırlan")
            time.sleep(2)
            print("Sevdiğin kıza yakınlaşmak için okula git")
            time.sleep(3)
            print("Dersler bitince eve geri gel")
            time.sleep(2.75)
            print("Bilgisayara geç, akşama kadar oyna")
            time.sleep(3)
            print("Her gün kendini tekrar eden günleri yaşıyorsun.")
            time.sleep(3.7)
            print("Tekrar okula gidiyorsun ama bu sefer sadece kız için değil sınıfça kampa gitmek için.\n")
            time.sleep(5)
            print("Akşam okul otobüsüyle kampa gittiniz. Grup kurup çadırlara yerlestiniz.")
            time.sleep(4.8)

            print("Bir ormanda uyandım")
            time.sleep(2)
            print("Çok gürültülüydü")
            time.sleep(2)
            print("Hiç birşey hatırlamıyorum")
            time.sleep(2)
            print("Neden burda olduğumu da")
            time.sleep(2)
            print("Bir yol farkettim")
            time.sleep(2)
            print("Yaklaştıktan sonra çok uzun yol olduğunu farkettim ve o yoldan gitmeye karar verdim")
            time.sleep(5)
            print('Yürürken "Nasıl bir anda herşeyi unutup ormanda uyanabilirim ki?" diye düşündüm')
            time.sleep(5)
            print("İsmimi bile hatırlamıyorum")
            time.sleep(2)
            print("Bu bir felaketti")
            time.sleep(2)
            print("Hiç şaşırmadım")
            time.sleep(2)
            print("Diğerlerin gibi oturup delirmedim")
            time.sleep(2)
            print("Kafamı parçalamadım")
            time.sleep(2)
            print("Hayatın boktan birşey olduğunu düşünmedim")
            time.sleep(3)
            print("Yürüdüm sadece")
            time.sleep(3)
            print("Sadece")
            time.sleep(4)
            print("Yürüdüm")
            time.sleep(5)

            print("\n<<Birkaç saat sonra>>\n")
            time.sleep(7)

            print("Birini gördüm")
            time.sleep(2)
            print("Yaklaştıktan sonra bir ihtiyar olduğunu farkettim")
            time.sleep(3)
            print("O da beni farketti")
            time.sleep(3)

            print("İhtiyar: Hey, bana uzun süre baktığını farkettim. Sorun nedir?")
            print("Ben: Ha, sorun yok. Sadece düşüncelerime daldım.")
            isim = input("\nİhtiyar: Bu arada senin ismin nedir?\n İsmim: ")    #İsim sorma
            time.sleep(2)
            print("İhtiyar: Hmm.. " + isim + " ne kadar güzel bir isim!")
            time.sleep(3)
            print("İhtiyar: Bu arada, biz neden burada duruyoruz?\nBenim eve gidelim, intihar edecekmişsin gibi görünüyorsun.")
            time.sleep(6)
            print('"Eve gelirsiniz."\n' + isim + ": " + '"Ev çok ürkütücü gözüküyor."')
            time.sleep(5)
            print("Bu evdeyken dikkat etmeliyim")
            time.sleep(2)
            print("<<Birkaç dakika evde durduktan sonra biraz acıkmaya başladım>>")
            time.sleep(4)
            secenek1 = input("1) Acıktığını söyle \n2) Adamın ismini sor\n(Seçmek için seçenek numarasını yazıp 'Enter'a tıkla)\n Seçenek ->  ")
            if secenek1 == str(1):
                time.sleep(2)
                print(isim + ": Şey.. ben biraz acıktım da... Yiyecek birşey var mı?")
                time.sleep(3)
                print("İhtiyar: Tabiki var, olmaz mı? İstediğini yiyebilirsin delikanlı")
                time.sleep(3)
            elif secenek1 == str(2):
                print(isim + ": Şey.. sizin adınız nedir?")
                time.sleep(2)
                print("İhtiyar: Adım Hüseyin, ama bana kısaca Hüsük diye seslenebilirsin")
                time.sleep(4)
            else:
                print("Var olmayan seçeneği seçtiniz")
                time.sleep(3)
                print("Oyun kapatılıyor...")
                time.sleep(3)



            print("<<OYUN MESAJI>>\nŞİMDİLİK BU KADAR DEVAMI YAKINDA GELİYOR")



            # SOHBETİN SONU


        start_talk()

# Oyunu Başlatma

oyun_baslatma_kararı = input("Oyuna devam etmek için 'Enter'a bas\n")
if oyun_baslatma_kararı == "":
    load_game()
else:
    print("Sadece 'Enter'a basmadığınız için oyun kapatılacaktır")

# Oyun Bitişi
