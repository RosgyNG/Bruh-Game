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
            print('Yürürken "Nasıl bir anda herşeyi unutup ormanda uyanabilirim ki?" diye düşünüyordum')
            time.sleep(5)
            print("İsmimi bile hatırlamıyorum")
            time.sleep(2)
            print("Bu resmen bir felaketti!")
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

            print("\nBirkaç saat sonra\n")
            time.sleep(5)

            print("Birini gördüm")
            time.sleep(2)
            print("Yaklaştıktan sonra ihtiyar olduğunu farkettim")
            time.sleep(3)
            print("Benim ona yaklaştığımı gördü")
            time.sleep(3)

            isim = input("\nİhtiyar: Bu arada senin ismin nedir?\n")
            time.sleep(2)
            print("İhtiyar: Hmm.. " + isim + " ne kadar güzel bir isim!")
            time.sleep(2)
            print("İhtiyar: Bu arada, biz neden burada duruyoruz?\nBenim eve gidelim, intihar edecekmişsin gibi görünüyorsun.")
            time.sleep(2)
            print('"Eve gelirsiniz."\n' + isim + ": " + '"Ev çok ürkütücü gözüküyor."')
            time.sleep(2)
            print("Bu evdeyken dikkat etmeliyim")
            time.sleep(2)
            #secenek = input("1) Adamın ismini sor. \n")
            #time.sleep(2)


            # SOHBETİN SONU
        start_talk()

# Oyunu Başlatma

oyun_baslatma_kararı = input("Oyuna devam etmek için 'Enter'a bas\n")
if oyun_baslatma_kararı == "":
    load_game()
else:
    print("Oyun kapatılacaktır") 

# Oyun Bitişi
