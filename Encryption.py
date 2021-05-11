#  Python project to hide data in images (Steganography)
# Coded by Dharunraj.R
# Code for encrypting the data


from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog, Button
import cv2
import math
import numpy as np

global image_path


image_size = 300, 300


def valid_entry():
    uname = username.get()
    pword = password.get()
    if  uname == "Dharun" and pword == "admin1" :

        def ifClicked():

            global image_path

            image_path = filedialog.askopenfilename()
            image = Image.open(image_path)
            image.thumbnail(image_size)
            disp_image = ImageTk.PhotoImage(image)
            img = Label(window, image=disp_image)
            img.image = disp_image
            img.place(x=20, y=50)

        def encrypt_data():

            global image_path

            data = txt.get(1.0, "end-1c")
            data+="#$dlm$#"
            img = cv2.imread(image_path)
            data = [format(ord(i), '08b') for i in data]

            encrypted_name = txt1.get(1.0, "end-1c")
            encrypted_name += ".png"

            height, width, _ = img.shape


            PixReq = len(data) * 3
            RowReq = PixReq / width
            RowReq = math.ceil(RowReq)

            count = 0
            charCount = 0

            pixels = height * width

            if pixels * 3 > len(data):
                for i in range(RowReq + 1):

                    while count < width and charCount < len(data):

                        char = data[charCount]
                        charCount += 1

                        for index, k in enumerate(char):

                            if (k == '1' and img[i][count][index % 3] % 2 == 0) or (k == '0' and img[i][count][index % 3] % 2 == 1):
                                img[i][count][index % 3] -= 1

                            if index % 3 == 2:
                                count += 1

                            if index == 7:

                                if charCount * 3 < PixReq and img[i][count][2] % 2 == 1:
                                    img[i][count][2] -= 1

                                if charCount * 3 >= PixReq and img[i][count][2] % 2 == 0:
                                    img[i][count][2] -= 1

                                count += 1

                    count = 0
            else:
                print("Size of data exceeds the image size")
                window.destroy()

            cv2.imwrite(encrypted_name, img)
            encrypted=Label(window,text="Encrypted image:",bg='lavender',font=("Times New Roman",14))
            encrypted.place(x=0,y=380)
            encoded_image = Image.open(encrypted_name)
            encoded_image.thumbnail(image_size)
            disp_encoded_image = ImageTk.PhotoImage(encoded_image)
            enc_img = Label(window, image=disp_encoded_image)
            enc_img.image = disp_encoded_image
            enc_img.place(x=20, y=450)

            success = Label(window, text="Encryption Successful!", bg='lavender', font=("Times New Roman", 20))
            success.place(x=160, y=700)



        app.destroy()
        window = Tk()
        window.configure(background='lavender')
        window.title("Encryption")
        window.geometry('900x900')

        ifClicked_button = Button(window, text="Choose Image", bg='white', fg='black', command=ifClicked)
        ifClicked_button.place(x=250, y=10)

        txt = Text(window, wrap=WORD, width=30)
        txt.place(x=340, y=55, height=165)

        label = Label(window, text="Enter the name to be given to the encrypted image:", bg='white', fg='black')
        txt1 = Text(window, wrap=WORD, width=30)

        label.place(x=50, y=275)
        txt1.place(x=330, y=275, height=35)

        encrypt_button = Button(window, text="Encode", bg='white', fg='black', command=encrypt_data)
        encrypt_button.place(x=250, y=350)
        window.mainloop()

    else:
        app.destroy()
        print("Invalid Login")


app = Tk()
app.title("Login")
app.geometry("300x200")
username_label = Label(app, text="Username").place(x=10, y=10)
username = Entry(app)
username.place(x=140, y=10)
password_label = Label(app, text="Password").place(x=10, y=40)
password = Entry(app, show="*")
password.place(x=140, y=40)
Button(app, text="Login", command=valid_entry).place(x=125, y=100)
app.mainloop()
