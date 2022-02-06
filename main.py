import tkinter
from tkinter import *
import requests
# API Covid
response = requests.get(
    'https://data.covid19.go.id/public/api/update.json')

data = response.json()
print(data['update']['total'])
jumlahPositif = data['update']['total']['jumlah_positif']
jumlahDirawat = data['update']['total']['jumlah_dirawat']
jumlahSembuh = data['update']['total']['jumlah_sembuh']
jumlahMeninggal = data['update']['total']['jumlah_meninggal']

link1 = "Detect.py"
link2 = "detectInputVideo.py"
image = "/aset/emoji.png"

main_window = tkinter.Tk()

main_window.geometry("1280x720")
main_window.title('Covid Crowd Control')
main_window.iconbitmap('assets/img/logo.ico')


def event_tekan1():
    main_window.destroy()
    exec(compile(open(link1).read(), link1, 'exec'))


def event_tekan2():
    main_window.destroy()
    exec(compile(open(link2).read(), link2, 'exec'))


def event_keluar():
    main_window.destroy()


label1 = tkinter.Label(
    main_window, text="Open Your Camera \n CCC is a software to detect crowds during a pandemic ", border=16)
label1.place(relx=0.5, rely=0.3, anchor=CENTER)

label1 = tkinter.Label(
    main_window, text="Kasus Data Covid Indonesia \n Jumlah Positif = " + str(jumlahPositif) + " | Jumlah Dirawat = " + str(jumlahDirawat) + " | Jumlah Sembuh = " + str(jumlahSembuh) + " | Jumlah Meninggal = " + str(jumlahMeninggal) + " ", border=16)
label1.place(relx=0.5, rely=0.95, anchor=CENTER)

camera_button = tkinter.Button(main_window, text="Camera", foreground='white',
                               background='blue', height=2, width=8, border=16, command=event_tekan1)
camera_button.place(relx=0.4, rely=0.4, anchor=CENTER)

camera_button = tkinter.Button(main_window, text="Video", foreground='white',
                               background='blue', height=2, width=8, border=16, command=event_tekan2)
camera_button.place(relx=0.5, rely=0.4, anchor=CENTER)

keluar = tkinter.Button(main_window, text="Keluar", foreground='white',
                        background='blue', height=2, width=8, border=16, command=event_keluar)
keluar.place(relx=0.6, rely=0.4, anchor=CENTER)


# label1.pack()
# camera_button.pack()

main_window.mainloop()
