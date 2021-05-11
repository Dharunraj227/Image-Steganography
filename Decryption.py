#  Python project to hide data in images (Steganography)
# Coded by Srivatsan.R
# Code for decrypting the data


import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog,Button,Label,Tk,Entry,ttk
import cv2
import numpy as np


image_display_size = 300,300
message=[]


def valid_entry():
    uname = username.get()
    pword = password.get()
    if (uname == "Srivatsan" and pword == "admin2") :

        def decrypt():
            global message
           
            path = filedialog.askopenfilename()

            image = Image.open(path)
            image.thumbnail(image_display_size)
            disp_image = ImageTk.PhotoImage(image)
            img = Label(app, image=disp_image)
            img.image = disp_image
            img.place(x=100, y=50)

          
            img = cv2.imread(path)
            data = []
            stop = False
            for index_i, i in enumerate(img):

                i.tolist()
                for index_j, j in enumerate(i):
                
                    if ((index_j) % 3 == 2):
                    
                        data.append(bin(j[0])[-1])
                      
                        data.append(bin(j[1])[-1])
                     
                        if (bin(j[2])[-1] == '1'):
                            stop = True
                            break
                    else:
                     
                        data.append(bin(j[0])[-1])
                
                        data.append(bin(j[1])[-1])
            
                        data.append(bin(j[2])[-1])
                if (stop):
                    break
            
            for i in range(int((len(data) + 1) / 8)):
                message.append(data[i * 8:(i * 8 + 8)])
            message = [chr(int(''.join(i), 2)) for i in message]
            message = ''.join(message)

            def display():
                global message
                if(message[-7:] == "#$dlm$#"):
                    message=message[0:len(message)-7]
                    message_label = Label(app, text=message, bg='lavender', font=(style.get(), 16))
                    message_label.place(x=30, y=500)
                else:
                    message_label = Label(app, text="Error:The given Image is not encoded", bg='lavender', font=(style.get(), 16))
                    message_label.place(x=30, y=500)
                    
            style=tk.StringVar()
            font_style=ttk.Combobox(app, width=27, textvariable = style)
            font_style['values'] = ('Times New Roman','Segoe UI','Blackadder ITC','Roboto Slab')
            font_style.place(x=10,y=300)
            select=Button(app,text="Select ",command=display).place(x=250,y=300)
            
            

        
        window.destroy()
        app = Tk()
        app.configure(background='Orange')
        app.title("Decrypt")
        app.geometry('600x600')
        # Add the button to call the function decrypt.
        main_button = Button(app, text="Start Program", bg='white', fg='black', command=decrypt)
        main_button.place(x=250, y=10)
        app.mainloop()


    else:
        window.destroy()
        print("Invalid Login")

window=Tk()
window.title("Login")
window.geometry("300x200")
username_label = Label(window,text="Username").place(x=10,y=10)
username = Entry(window)
username.place(x=140,y=10)
password_label = Label(window,text="Password").place(x=10,y=40)
password = Entry(window,show="*")
password.place(x=140,y=40)
Button(window,text="Login",command=valid_entry).place(x=125,y=100)
window.mainloop()
