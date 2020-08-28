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


# Konuşma Fonksiyonu
        def start_talk():
            print("")
            isim = input("Biri: Bu arada senin ismin nedir?\n")
            time.sleep(1)
            print("Biri: Hmm.. " + isim + " ne kadar güzel bir isim!")
            time.sleep(2)
            print("Biri: Bu arada, neden burada duruyoruz?\nBenim eve gidelim, berbat görünüyorsun.")
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
