# %%
from gtts import gTTS
from google_trans_new import google_translator
import os
# %%
text = input("Metin giriniz.... ")

translator = google_translator()

textTranslaterENG = translator.translate(text, lang_src='tr' ,lang_tgt='en')
textTranslaterFR = translator.translate(text, lang_src='tr' ,lang_tgt='fr')
textTranslaterGER = translator.translate(text, lang_src='tr' ,lang_tgt='de')

speech_tr= gTTS(text=text, lang='tr', slow=False)
speech_en= gTTS(text=textTranslaterENG, lang='en', slow=False)
speech_de= gTTS(text=textTranslaterGER, lang='de', slow=False)
speech_fr= gTTS(text=textTranslaterFR, lang='fr', slow=False)

speech_tr.save("tr.mp3")
speech_en.save("en.mp3")
speech_de.save("de.mp3")
speech_fr.save("fr.mp3")

os.system("echo Listeden dil seciniz.")
os.system("echo 1.Turkish")
os.system("echo 2.English")
os.system("echo 3.French")
os.system("echo 4.German")

out = int(input("Secmek istediginiz dilin numarasi nedir ? ..... "))

if out==1:
    os.system("start tr.mp3")
if out==2:
    os.system("start en.mp3")
if out==3:
    os.system("start fr.mp3")
if out==4:
    os.system("start de.mp3")    
# %%
