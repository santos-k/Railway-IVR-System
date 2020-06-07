from tkinter import *
from gtts import gTTS
from playsound import playsound
import time

root = Tk()
root.title("Railway Announcement by Santosh")
root.geometry("900x400")
root.minsize(900,400)
root.maxsize(900,400)
root.configure(background="gray")
root.wm_iconbitmap("icon.ico")

#language text varialbles
hindi_audio_file = ""
eng_audio_file = ""
#global variables
tnoget = ""
tnameget = ""
tfromget = ""
ttoget = ""
tvia1get = ""
tvia2get = ""
tvia3get = ""
plateformget = "" 
hrtimeget = ""
mintimeget = ""
#get all entry widget and dropdown input
def inputdata():
    global tnoget, tnameget,tfromget,ttoget,tvia1get,tvia2get,tvia3get,plateformget,hrtimeget,mintimeget
    tnoget = tno.get()
    tnameget = tname.get()
    tfromget = tfrom.get()
    ttoget = tto.get()
    tvia1get = tvia1.get()
    tvia2get = tvia2.get()
    tvia3get = tvia3.get()
    plateformget = var0.get()
    hrtimeget = var1.get()
    mintimeget = var2.get()
    # Reset all values
    entry = [tno,tname,tfrom,tto,tvia1,tvia2,tvia3]
    for i in entry:
        i.delete(0,END)
    var0.set(plateformlist[0])
    var1.set(hrtime[0])
    var2.set(mintime[0])
# convert text to audio mp3 file
def mainfunc(hi_text, eng_text):
    global hindi_audio_file, eng_audio_file
    Announcement_text_hi = hi_text
    Announcement_text_en =  eng_text   
    print("Audio Generating.......")
    gnrt_audio = gTTS(text=Announcement_text_hi, lang='hi', slow=False)
    hindi_audio_file = (f"{tnoget}_hi.mp3")
    gnrt_audio.save(hindi_audio_file)
    print("One file generated, Generating last  file.......")
    gnrt_audio2 = gTTS(text=Announcement_text_en, lang='en', slow=False)
    eng_audio_file = (f"{tnoget}_en.mp3")
    gnrt_audio2.save(eng_audio_file)
    Label(root,text="Both Audio Generated.\nReady to Announce.").place(x=350,y=275)
    return hindi_audio_file, eng_audio_file

def arrival():	# will generate arriaval announcement
    inputdata()
    hi_text = f"यात्रिगन क्रिप्या ध्यान दिजिये गाडी संख्या {tnoget}, {tnameget}, {tfromget} से चलकर {tvia1get},{tvia2get},{tvia3get} के रास्ते {ttoget} को जाने वाली प्लेटफार्म संख्या {plateformget} पर आ रहि हैं"
    eng_text = f"May I have your attention please. train number {tnoget}, {tnameget}, from {tfromget} to {ttoget} via {tvia1get}, {tvia2get}, {tvia3get} is arriving shortly on Platform number {plateformget}."
    mainfunc(hi_text, eng_text)
    
def departur():	# will generate deparure announcement
    inputdata()
    hi_text = f"यात्रिगन क्रिप्या ध्यान दिजिय, गाडी संख्या, {tnoget}, {tnameget}, {tfromget} से चलकर {tvia1get},{tvia2get},{tvia3get} के रास्ते {ttoget} को जाने वाली कुछ ही समय में प्लेटफार्म संख्या {plateformget} से रवाना होने वालि हैं "
    eng_text = f"May I have your attention please, train number, {tnoget}, {tnameget}, from {tfromget} to {ttoget} via {tvia1get}, {tvia2get}, {tvia3get} will depart shortly from Platform number {plateformget}."
    mainfunc(hi_text, eng_text)

def delayed():	# will generate delayed announcement
    inputdata()
    hi_text = f"यात्रिगन क्रिप्या ध्यान दिजिय, गाडी संख्या, {tnoget}, {tnameget}, {tfromget} से चलकर {tvia1get},{tvia2get},{tvia3get} के रास्ते {ttoget} को जाने वाली अपने नैर्धारित समय से {hrtimeget} घंटे {mintimeget} मिनट कि  देरी से आयेगि, असाहता के लिए खेद है  "
    eng_text = f"May I have your attention please, train number, {tnoget}, {tnameget}, from {tfromget} to {ttoget} via {tvia1get}, {tvia2get}, {tvia3get} is delayed by {hrtimeget} hours {mintimeget} minutes. The inconvenience caused is deeply regretted."
    mainfunc(hi_text, eng_text)

def play():	# Will play generated audio
	playsound("railway_msg.mp3")
	playsound(hindi_audio_file)
	playsound("railway_msg.mp3")
	playsound(eng_audio_file)
	
font1 = "Arial 15 italic bold"
title1 = "Railway Announcement IVR Software"
Label(root, text = title1, font = "Arial 30 bold",bg ="#9F3CEC", fg= "black",relief=RIDGE).grid(columnspan=20,ipadx=99,row=0, column=0)
Label(root,text = "Train No.: ",font = font1, bg= "#DDA613", relief=GROOVE).grid(row = 1, column =1,pady = 5,padx=10, sticky = W)
Label(root,text = "Train Name.: ",font = font1, bg= "#DDA613", relief=GROOVE).grid(row = 1, column =3,pady = 5,padx=10, sticky = W)
Label(root,text = "Arrival Station: ",font = font1, bg= "#DDA613", relief=GROOVE).grid(row = 3, column =1,pady = 5,padx=10, sticky = W)
Label(root,text = "Final Destination: ",font = font1, bg= "#DDA613", relief=GROOVE).grid(row = 3, column =3,pady = 5,padx=10, sticky = W)
Label(root,text = "Via Stations: ",font = font1, bg= "#DDA613", relief=GROOVE).grid(row = 5, column =1,pady = 5,padx=10, sticky = W)
Label(root,text = "Platform Number: ",font = font1, bg= "#DDA613", relief=GROOVE).grid(row = 6, column =1,pady = 5, padx=10,sticky = W)
Label(root,text = "Delay Timing: ",font = font1, bg= "#DDA613", relief=GROOVE).grid(row = 6, column =3,pady = 5, padx=10,sticky = W)
#Entry widgets
tno = Entry(root,font =font1, relief = SUNKEN,border = 2, width = 8)
tname = Entry(root, font =font1, relief = SUNKEN,border = 2,width = 25)
tfrom = Entry(root, font =font1, relief = SUNKEN,border = 2, width = 15)
tto = Entry(root, font =font1, relief = SUNKEN,border = 2, width = 15)
tvia1 = Entry(root, font =font1, relief = SUNKEN,border = 2, width = 15)
tvia2 = Entry(root, font =font1, relief = SUNKEN,border = 2, width = 15)
tvia3 = Entry(root, font =font1, relief = SUNKEN,border = 2, width = 15)
#plateform Numbers
plateformlist = ["Select Platform"]
hrtime = ["Select Hrs"]
mintime = ['Select Mins']
var0 = StringVar(root)
var1 = StringVar(root)
var2 = StringVar(root)
# Plateform Number List dropdown
for i in range(1,21):
    plateformlist.append(i)
var0.set(plateformlist[0]) 
tplateform = OptionMenu(root, var0, *plateformlist)
tplateform.config(width=12)
# Hours List dropdown
for i in range(1,13):
    hrtime.append(i)
var1.set(hrtime[0])
hrt = OptionMenu(root, var1, *hrtime)
hrt.config(width=9)  
# Minutes List dropdown
for i in range(0,60):
    if i % 5 ==0 and i >0:
        mintime.append(i)
var2.set(mintime[0])
mint = OptionMenu(root, var2, *mintime)
mint.config(width=9)
#packing entry and dropdwon widgets
tno.grid(row = 1, column = 2, sticky = W)
tname.grid(row = 1, column = 4, sticky = W,columnspan=2)
tfrom.grid(row = 3, column = 2, sticky = W)
tto.grid(row = 3, column = 4, sticky = W)
tvia1.grid(row = 5, column = 2, sticky = W)
tvia2.grid(row = 5, column = 3, padx=10, sticky = W)
tvia3.grid(row = 5, column = 4, sticky = W)
tplateform.grid(row = 6, column = 2, sticky = W)
hrt.grid(row = 6, column = 4, sticky = W)
mint.grid(row = 6, column = 4, sticky = E)
#Buttons 
sub_but = Button(root, text = "Start Announcement",font = font1, relief=RAISED, width=20,border=3,bg="#73DAE8",command=play).place(x=320, y=325)
playbutton = Button(root, text = "Gnrt Arrival Ancmt",font = font1, relief=RAISED, width=20,border=3,bg="#53C92D",command=arrival).place(x=30, y=220)
playbutton = Button(root, text = "Gnrt Departure Ancmt",font = font1, relief=RAISED, width=22,border=3,bg="#C0AA2F",command=departur).place(x=300, y=220)
playbutton = Button(root, text = "Gnrt Delay Ancmt",font = font1, relief=RAISED, width=20,border=3,bg="#F16559",command=delayed).place(x=590, y=220)
Label(root, text = "Developed By Santosh",font = "Arial 10 italic bold",bg="gray").place(x=350, y =370)

root.mainloop()