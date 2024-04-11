import tkinter
from tkinter import filedialog as fd
import customtkinter
from getPlaylist import getPlaylist

def open_folder_selection():
    global folder
    folder = fd.askdirectory()

def startDownload():
    getPlaylist(url_entry.get(), folder)
    root.destroy()

root = customtkinter.CTk()
root.geometry(f"{400}x{400}")
root.title("SPOTIFY PLAYLIST DOWNLOADER")

frame = customtkinter.CTkFrame(master=root, width=450, height=450, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label_1 = customtkinter.CTkLabel(master=frame, width=380, height=60, corner_radius=10, font=("", 20),
                                     fg_color=("gray70", "gray35"), text="Spotify Playlist Downloader")
label_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

url_entry = customtkinter.CTkEntry(master=frame, corner_radius=20, height=40, width=380, placeholder_text="Paste the playlist linke here...")
url_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

entry_2 = customtkinter.CTkButton(master=frame, text="Choose files", corner_radius=6, command=open_folder_selection, height=40, width=380)
entry_2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

button_login = customtkinter.CTkButton(master=frame, text="DOWNLOAD", corner_radius=6, command=startDownload, height=40, width=380)
button_login.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

root.mainloop()