# Import
from tkinter import *
from tkinter import messagebox
import os
import qrcode
from PIL import ImageTk, Image
from tkinter import filedialog
from pyzbar.pyzbar import decode

way = os.path.abspath(os.curdir) + '\\img'
title = ''
type = 'text'
save_path = os.path.abspath(os.curdir) + '\\img\\'
open_path = ''

# Window
root = Tk()
root.title('Create your own QR code')
root.geometry('600x600')
root['bg'] = '#5762ff'
root.iconbitmap('icon.ico')
root.resizable(width=False, height=False)


# Functions

def forget():
    l1.place_forget()
    l2.place_forget()
    cr_b.place_forget()
    sc_b.place_forget()
    text_b.place_forget()
    im_b.place_forget()
    ur_b.place_forget()
    l3.place_forget()
    fr1.place_forget()
    l4.place_forget()
    en1.place_forget()
    gen_b.place_forget()
    l5.place_forget()
    home_b.place_forget()
    op.place_forget()
    en2.place_forget()
    path.place_forget()
    l6.place_forget()
    opd.place_forget()
    l7.place_forget()
    er.place_forget()
    l8.place_forget()
    l9.place_forget()
    op1.place_forget()
    all_l.place_forget()
    sc_b.place_forget()
    all_l.place_forget()
    dec.place_forget()
    scan_b.place_forget()


def text():
    global type
    forget()
    type = 'text'
    text_b.place(x=0, y=0)
    im_b.place(x=200, y=0)
    ur_b.place(x=400, y=0)
    l3['text'] = 'Here write the text that will be encrypted in QR code:'
    l3.place(x=2, y=60)
    fr1.place(x=5, y=80)
    scroll.pack(side=RIGHT, fill=Y)
    t1.pack(side=LEFT)
    l4.place(x=180, y=410)
    en1.place(x=110, y=450)
    gen_b.place(x=200, y=500)
    scroll.config(command=t1.yview)


def img():
    global type, r
    forget()
    type = 'img'
    r = 1
    text_b.place(x=0, y=0)
    im_b.place(x=200, y=0)
    ur_b.place(x=400, y=0)
    l3['text'] = 'Here select the image\n that will be encrypted in QR code:'
    l3.place(x=100, y=60)
    l6.place(x=50, y=140)
    path.place(x=50, y=170)
    op.place(x=400, y=140)
    er.place(x=20, y=200)
    l4.place(x=155, y=300)
    en1.place(x=100, y=350)
    gen_b.place(x=200, y=460)


def url():
    global type
    forget()
    type = 'url'
    text_b.place(x=0, y=0)
    im_b.place(x=200, y=0)
    ur_b.place(x=400, y=0)
    l3['text'] = 'Here write the URL that will be encrypted in QR code:'
    l3.place(x=6, y=60)
    l5.place(x=40, y=150)
    en2.place(x=100, y=200)
    l4.place(x=180, y=310)
    en1.place(x=100, y=350)
    gen_b.place(x=200, y=400)
    op.place_forget()


def create():
    forget()
    text()


def gen():
    global title, r
    if type == 'text':
        messagebox.showinfo('Select directory', 'All QR codes will be saved in: ' + os.path.abspath(
            os.curdir) + '\\img. ' + 'You can change it in Settings')
        title = en1.get()
        img = qrcode.make(t1.get('1.0', END))
        img.save(save_path + title + '.png')
    elif type == 'url':
        messagebox.showinfo('Select directory', 'All QR codes will be saved in: ' + os.path.abspath(
            os.curdir) + '\\img. ' + 'You can change it in Settings')
        title = en1.get()
        img = qrcode.make(en2.get())
        img.save(save_path + title + '.png')
    elif type == 'img':
        messagebox.showinfo('Select directory', 'All QR codes will be saved in: ' + os.path.abspath(
            os.curdir) + '\\img. ' + 'You can change it in Settings')
        title = en1.get()
        img = qrcode.make(root.filename)
        img.save(save_path + title + '.png')
    messagebox.showinfo('Successfully', 'Your qr code successfully generated')
    home_b.place(x=450, y=550)
    opd.place(x=50, y=540)


def scan():
    forget()
    l7.place(x=55, y=20)
    l8.place(x=55, y=120)
    l9.place(x=75, y=150)
    op1.place(x=525, y=125)
    scan_b.place(x=200, y=500)
    home_b.place(x=500, y=550)


def home():
    forget()
    l1.place(x=25, y=40)
    l2.place(x=500, y=570)
    cr_b.place(x=55, y=170)
    sc_b.place(x=85, y=350)


def open_dir():
    os.startfile(os.path.realpath(save_path))


def open_file():
    try:
        root.filename = filedialog.askopenfilename(initialdir='D://', title='Open image', filetypes=(
            ('png files', '*.png'), ('JPEG files', '*.jpg'), ('All files', '*.*')))
        path['text'] = root.filename
        if isinstance():
            path['text'] = root.filename
    except:
        path


def openQR():
    global open_path
    root.filename = filedialog.askopenfilename(initialdir=save_path, title='Open QR', filetypes=(
        ('PNG files', '*.png'), ('All files', '*.*')))
    if len(root.filename) == 0:
        l9['text'] = os.path.abspath(os.curdir) + '\\img\\'
    else:
        open_path = root.filename
        l9['text'] = root.filename


def scaning():
    try:
        d = decode(Image.open(open_path))
        all_l['text'] = d[0].data.decode()
        all_l.place(x=75, y=250)

    except:
        messagebox.showerror('Select', 'Please, select QR code')


# Objects

# Frame
fr1 = Frame(root)  # Frame of textbox and scroll
# Label
l1 = Label(root, text='Create your QR code', font=('Miriam Fixed', 48, 'bold'),
           bg='#5762ff')  # Mail label with program title
l2 = Label(root, text='Official version 1.0', font='Arial 8', bg='#5762ff')  # Official label
l3 = Label(root, text='Here write the text that will be encrypted in QR code:', font=('Miriam Fixed', 12, 'bold'),
           bg='#5762ff')  # Pointed label
l4 = Label(root, text='Here write title of file:', font=('Miriam Fixed', 12, 'bold'),
           bg='#5762ff')  # Creating title of OR
l5 = Label(root, text='Here place your url with https:// or with www.', font=('Miriam Fixed', 12, 'bold'),
           bg='#5762ff')  # URL label
path = Label(root, text='D:\\', font=('Miriam Fixed', 8, 'bold'), bg='white')  # Path of image
er = Label(root, text='* You can encrypted only path to file', font=('Miriam Fixed', 8, 'bold'),
           bg='#5762ff')  # Error label
l6 = Label(root, text='The path to the file: ', font=('Miriam Fixed', 12, 'bold'), bg='#5762ff')  # Label of path
l7 = Label(root, text='Scan your QR', font=('Miriam Fixed', 48, 'bold'), bg='#5762ff')  # Scan label
l8 = Label(root, text='Path to the file: ', font=('Miriam Fixed', 8, 'bold'), bg='#5762ff')
l9 = Label(root, text=save_path, font=('Miriam Fixed', 8, 'bold'), bg='white')
dec = Label(root, text='Decoding:', font=('Miriam Fixed', 18, 'bold'), bg='#5762ff')
all_l = Label(root, font=('Miriam Fixed', 18, 'bold'), bg='#5762ff')

# Text
scroll = Scrollbar(fr1)
t1 = Text(fr1, width=30, height=10, font=('Miriam Fixed', 24), yscrollcommand=scroll.set)  # Text box for text
en1 = Entry(root, font=('Miriam Fixed', 24))  # Entry for name file
en2 = Entry(root, font=('Miriam Fixed', 24))  # Entry for url
# Button
image1 = ImageTk.PhotoImage(Image.open('open.jpg'))

cr_b = Button(root, text='Create QR code', font=('Miriam Fixed', 38, 'bold'), bg='#9db2ff', activebackground='#cffbff',
              command=create)  # Create QR button
sc_b = Button(root, text='Scan QR code', font=('Miriam Fixed', 38, 'bold'), bg='#9db2ff', activebackground='#cffbff',
              command=scan)  # Scan QR button
text_b = Button(root, text='Text', width=10, font=('Miriam Fixed', 24), bg='#9db2ff', activebackground='#cffbff',
                command=text)  # Create text QR button
im_b = Button(root, text='Image', width=10, font=('Miriam Fixed', 24), bg='#9db2ff', activebackground='#cffbff',
              command=img)  # Create image QR button
ur_b = Button(root, text='URL', width=10, font=('Miriam Fixed', 24), bg='#9db2ff', activebackground='#cffbff',
              command=url)  # Create URL QR button
gen_b = Button(root, text='Generate', width=10, font=('Miriam Fixed', 24), bg='#9db2ff', activebackground='#cffbff',
               command=gen)  # Generate QR button
home_b = Button(root, text='Home', font=('Miriam Fixed', 12), bg='#9db2ff', activebackground='#cffbff',
                command=home)  # Back to main menu
opd = Button(root, text='Open\n directory', bg='#9db2ff', font=('Miriam Fixed', 12), activebackground='#cffbff',
             command=open_dir)  # Open dir width file
op = Button(root, width=50, height=50, image=image1, command=open_file, bg='#5762ff',
            activebackground='#cffbff')  # Open file button
op1 = Button(root, width=50, height=50, image=image1, bg='#5762ff',
             activebackground='#cffbff', command=openQR)  # Open file button
scan_b = Button(root, text='Scan', width=10, font=('Miriam Fixed', 24), bg='#9db2ff', activebackground='#cffbff',
                command=scaning)
# Place
home()

# Mainloop
root.mainloop()