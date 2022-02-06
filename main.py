import tkinter
from tkinter import *


link = "Detect.py"
image = "/aset/emoji.png"

main_window = tkinter.Tk()

main_window.geometry("1280x720")
main_window.title('Covid Crowd Control')
main_window.iconbitmap('assets/img/logo.ico')


def event_tekan():
    main_window.destroy()
    exec(compile(open(link).read(), link, 'exec'))


def event_keluar():
    main_window.destroy()


judul = tkinter.Label(main_window, text="CCC", border=24)
judul.place(relx=0, rely=0)

label1 = tkinter.Label(
    main_window, text="Open Your Camera \n CCC is a software to detect crowds during a pandemic ", border=16)
label1.place(relx=0.5, rely=0.3, anchor=CENTER)

camera_button = tkinter.Button(main_window, text="Camera", foreground='white',
                               background='blue', height=2, width=8, border=16, command=event_tekan)
camera_button.place(relx=0.4, rely=0.4, anchor=CENTER)

keluar = tkinter.Button(main_window, text="Keluar", foreground='white',
                        background='blue', height=2, width=8, border=16, command=event_keluar)
keluar.place(relx=0.6, rely=0.4, anchor=CENTER)


# label1.pack()
# camera_button.pack()

main_window.mainloop()
