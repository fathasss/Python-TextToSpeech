# %%

#Google Kütüphaneleri
from gtts import gTTS
from google_trans_new import google_translator
import os

# %%

#Metin girişi
text = input("Metin giriniz.... ")

#Çeviri aracı
translator = google_translator()

#Girilen türkçe metnin çevirisni yap.
textTranslaterENG = translator.translate(text, lang_src='tr' ,lang_tgt='en')
textTranslaterFR = translator.translate(text, lang_src='tr' ,lang_tgt='fr')
textTranslaterGER = translator.translate(text, lang_src='tr' ,lang_tgt='de')

#Metni ses dönüştür.
speech_tr= gTTS(text=text, lang='tr', slow=False)
speech_en= gTTS(text=textTranslaterENG, lang='en', slow=False)
speech_de= gTTS(text=textTranslaterGER, lang='de', slow=False)
speech_fr= gTTS(text=textTranslaterFR, lang='fr', slow=False)

#Ses dosyalarını kaydet
speech_tr.save("mp3/tr.mp3")
speech_en.save("mp3/en.mp3")
speech_de.save("mp3/de.mp3")
speech_fr.save("mp3/fr.mp3")

#Desteklenen dilleri konsola yaz.
os.system("echo Listeden dil seciniz.")
os.system("echo 1.Turkish")
os.system("echo 2.English")
os.system("echo 3.French")
os.system("echo 4.German")

#Dil seçimi için veri al.
out = int(input("Secmek istediginiz dilin numarasi nedir ? ..... "))

#Girilen out değerine göre çalıştır.
if out==1:
    print("Türkçe")
    print(text)
    os.system("start mp3/tr.mp3")
if out==2:
    print("İngilizce")
    print(textTranslaterENG)
    os.system("start mp3/en.mp3")
if out==3:
    print("Fransızca")
    print(textTranslaterFR)
    os.system("start mp3/fr.mp3")
if out==4:
    print("Almanca")
    print(textTranslaterGER)
    os.system("start mp3/de.mp3")
# %%
