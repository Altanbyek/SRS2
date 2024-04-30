from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

mixer.init()

def addsongs():
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="song",
                                            filetypes=(("mp3 Files", "*.mp3"),))
    for s in temp_song:
        s = s.replace("C:\\Users\\user\\Downloads\\music", "")
        songs_list.insert(END, s)

def Play():
    song = songs_list.get(ACTIVE)
    song = song.replace("C:\\Users\\user\\Downloads\\music", "")
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Resume():
    mixer.music.unpause()


root = Tk()
root.title("Music Player")
root.geometry("500x300")

# create a listbox widget
songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), width=50)
songs_list.pack(fill=BOTH, expand=True)

play_button = Button(root, text="Play", width=14, command=Play)
play_button['font'] = font.Font(family='Helvetica')
play_button.pack(side=LEFT)

pause_button = Button(root, text="Pause", width=14, command=Pause)
pause_button['font'] = font.Font(family='Helvetica')
pause_button.pack(side=LEFT)

resume_button = Button(root, text="Resume", width=15, command=Resume)
resume_button['font'] = font.Font(family='Helvetica')
resume_button.pack(side=LEFT)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)

root.mainloop()
