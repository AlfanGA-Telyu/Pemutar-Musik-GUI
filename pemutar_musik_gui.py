from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer

color1 = "#ffffff"  # putih
color2 = "#3C1DC6"  # ungu
color3 = "#333333"  # hitam
color4 = "#CFC7F8"  # ungu muda

root = Tk()
root.title("Pemutar Musik ALRPO")
root.geometry('400x300')

root.resizable(False, False)
root.configure(background=color1)

# frame kiri
frame_kiri = Frame(root,width=150,height=150, bg=color1)
frame_kiri.grid(row=0, column=0,sticky='nsew')
# frame kanan
frame_kanan = Frame(root,width=250,height=150, bg=color3)
frame_kanan.grid(row=0, column=1,sticky='nsew')
# frame bawah
frame_bawah = Frame(root,width=400,height=150, bg=color1)
frame_bawah.grid(row=1, column=0, columnspan=2,sticky='nsew')


# list lagu frame
listlagu = Listbox(frame_kanan, selectmode=SINGLE, font=("Arial 9 bold"),height=14, width=33, bg=color3, fg=color1)
listlagu.grid(row=0, column=0)
listlagu.insert(END, "Harap pilih folder musik Anda")

scrollbar = Scrollbar(frame_kanan)
scrollbar.grid(row=0, column=1, sticky='ns')

listlagu.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listlagu.yview)

# frame running song
running_song = Label(frame_bawah, text="Silahkan Pilih Lagu", font=("Ivy 10 bold"), width=44, height=1, bg=color1,
                     fg=color3, anchor=NW)
running_song.pack(fill='x', pady=3)

# event
def play_music():
    running = listlagu.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def browse():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        listlagu.delete(0, END)

        for i in songs:
            if i.endswith(".mp3"):
                listlagu.insert(END, i)


# foto/icon
img_1 = Image.open('asset_pemutar_musik_gui/logo.png')
img_1 = img_1.resize((150,250))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(frame_kiri, image=img_1, bg=color2)
app_image.place(x=0, y=0, width=150, height=250)

button_frame = Frame(frame_bawah, bg=color4)
button_frame.pack(expand=True, anchor=CENTER)

# icon tombol pause
img_5 = Image.open('asset_pemutar_musik_gui/pause.png')
img_5 = img_5.resize((20, 20))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(button_frame, width=20, height=20, image=img_5, padx=10, bg=color1, command=pause_music)
pause_button.pack(side=LEFT, padx=2)

# icon tombol play
img_3 = Image.open('asset_pemutar_musik_gui/play.png')
img_3 = img_3.resize((20, 20))
img_3 = ImageTk.PhotoImage(img_3)
play_button = Button(button_frame, width=20, height=20, image=img_3, padx=10, bg=color1, command=play_music)
play_button.pack(side=LEFT, padx=2)

# icon tombol stop
img_7 = Image.open('asset_pemutar_musik_gui/stop.png')
img_7 = img_7.resize((20, 20))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = Button(button_frame, width=20, height=20, image=img_7, padx=10, bg=color1, command=stop_music)
stop_button.pack(side=LEFT, padx=2)

# icon tombol continue
img_6 = Image.open('asset_pemutar_musik_gui/continue.png')
img_6 = img_6.resize((20, 20))
img_6 = ImageTk.PhotoImage(img_6)
continue_button = Button(button_frame, width=20, height=20, image=img_6, padx=10, bg=color1, command=continue_music)
continue_button.pack(side=LEFT, padx=2)

# icon browse lagu
img_8 = Image.open('asset_pemutar_musik_gui/browse.png')
img_8 = img_8.resize((20, 20))
img_8 = ImageTk.PhotoImage(img_8)
browse_button = Button(button_frame, width=20, height=20, image=img_8, padx=10, bg=color1, command=browse)
browse_button.pack(side=RIGHT, padx=2)

mixer.init()
root.mainloop()
