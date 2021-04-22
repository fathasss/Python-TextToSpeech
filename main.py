#%% 
#Library Import
from tkinter import *
from gtts import gTTS
from google_trans_new import google_translator
import os

#%%
translator = google_translator()
app = Tk()

def transItem():
    transText = customEntry.get()
    
    #Girilen türkçe metnin çevirisni yap.
    textTranslaterENG = translator.translate(transText, lang_src='tr' ,lang_tgt='en')
    textTranslaterFR = translator.translate(transText, lang_src='tr' ,lang_tgt='fr')
    textTranslaterGER = translator.translate(transText, lang_src='tr' ,lang_tgt='de')
    textTranslaterRU = translator.translate(transText, lang_src='tr' ,lang_tgt='ru')
    
    #Metni ses dönüştür.
    speech_tr = gTTS(text=transText, lang='tr', slow=False)
    speech_en = gTTS(text=textTranslaterENG, lang='en', slow=False)
    speech_de = gTTS(text=textTranslaterGER, lang='de', slow=False)
    speech_fr = gTTS(text=textTranslaterFR, lang='fr', slow=False)
    speech_ru = gTTS(text=textTranslaterRU, lang='ru', slow=False)
    
    #Ses dosyalarını kaydet
    speech_tr.save("mp3/tr.mp3")
    speech_en.save("mp3/en.mp3")
    speech_fr.save("mp3/fr.mp3")
    speech_de.save("mp3/de.mp3")
    speech_ru.save("mp3/ru.mp3")

    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0):
        transLabel = Label(app,text=transText,font=('bold',14),pady=5)
        transLabel.grid(row=1,column=3, padx=(100, 10))
        os.system("start mp3/tr.mp3")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 0):
        transLabel = Label(app,text=textTranslaterENG,font=('bold',14),pady=5)
        transLabel.grid(row=1,column=3, padx=(100, 10))
        os.system("start mp3/en.mp3")
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1) & (var4.get() == 0) & (var5.get() == 0):
        transLabel = Label(app,text=textTranslaterFR,font=('bold',14),pady=5)
        transLabel.grid(row=1,column=3, padx=(100, 10))
        os.system("start mp3/fr.mp3")
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 1) & (var5.get() == 0):
        transLabel = Label(app,text=textTranslaterDE,font=('bold',14),pady=5)
        transLabel.grid(row=1,column=3, padx=(100, 10))
        os.system("start mp3/de.mp3")
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0) & (var4.get() == 0)& (var5.get() == 1):
        transLabel = Label(app,text=textTranslaterRU,font=('bold',14),pady=5)
        transLabel.grid(row=1,column=3, padx=(100, 10))
        os.system("start mp3/ru.mp3")
    else:
        transLabel = Label(app,text="Dil seçimi yapın.",font=('bold',14),pady=5)
        transLabel.grid(row=1,column=3, padx=(100, 10))

#CheckBox Column
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
labelDes = Label(app,text="Dili Seçin.",font=('bold',14),pady=5).grid(row=0,column=0,pady=1)
checkTR = Checkbutton(app, text="Turkish", variable=var1).grid(row=1,column=0,pady=5,sticky=W)
checkENG = Checkbutton(app, text='English',variable=var2).grid(row=2,column=0,pady=5,sticky=W)
checkFR = Checkbutton(app, text='French',variable=var3).grid(row=3,column=0,pady=5,sticky=W)
checkDE = Checkbutton(app, text='German',variable=var4).grid(row=4,column=0,pady=5,sticky=W)
checkRU = Checkbutton(app, text='Russian',variable=var5).grid(row=5,column=0,pady=5,sticky=W)

#Text input
customLabel = Label(app,text="Metni Girin.",font=('bold',14),pady=5)
customLabel.grid(row=0, column=2,sticky=W, padx=(100, 10))
customEntry = Entry(app)
customEntry.grid(row=1,column=2,padx=(100, 10))

#Translate Button
transButton = Button(app,text='Translate',width=17,command=transItem)
transButton.grid(row=2,column=2,padx=(100, 10))

#Text Output
textOutput = StringVar()
outputLabel = Label(app,text="Metnin Çevirisi",font=('bold',14),pady=5)
outputLabel.grid(row=0, column=3,padx=(100, 10))

#Application Setting
app.title('Fatih HAS-Python Çeviri Aracı')
app.geometry('700x250')
app.mainloop()
