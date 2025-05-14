import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageChops

class Git_hup:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('520x520')
        self.root.config(bg='white')
        self.root.title('GitHub')

        self.set_up()

    def crop_white_border(self, image):
        bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
        diff = ImageChops.difference(image, bg)
        bbox = diff.getbbox()
        if bbox:
            return image.crop(bbox)
        return image

    def set_up(self):
        img = Image.open('icon.png')
        img = self.crop_white_border(img)
        img = img.resize((50, 50))
        gitHup_icon = ImageTk.PhotoImage(img)

        self.root.iconphoto(True, gitHup_icon)

        logo_label = tk.Label(self.root, image=gitHup_icon)
        logo_label.place(x=240, y=10)

        label = tk.Label(self.root, text='Sign in to GitHub', font=('arial', 15),bg='white')
        label.place(x=190, y=80)


        frame = tk.Frame(self.root,relief='raised',width=300,height=190)
        frame.place(x=120,y=120)

        label1 = tk.Label(frame,text='Username or email address',font=('Helvetica',11))
        label1.place(x=20,y=13)

        entry1 = tk.Entry(frame,width=44,bd=1)
        entry1.place(x=20,y=40)

        label2 = tk.Label(frame,text='Password',font=('arial',10))
        label2.place(x=20,y=75)

        entry2 = tk.Entry(frame,width=44,bd=1)
        entry2.place(x=20,y=100)

        label3 = tk.Label(frame,text='Forgot password?',fg='blue')
        label3.place(x=190,y=75)

        btn1 = tk.Button(frame,text='Sign in',width=26,bg='green',fg='white'
                         ,font=('arial',12,'bold'),relief='raised',
                         activebackground='green',activeforeground='white')
        btn1.place(x=19,y=140)

        
        frame2 = tk.Frame(self.root,relief='raised',width=300,height=65,bg='white',bd=2)
        frame2.place(x=120,y=330)

        label5 = tk.Label(frame2,text='Sign in with a passkey',
                          font=('arial',10),fg='blue',bg='white')
        label5.place(x=80,y=10)

        label6 = tk.Label(frame2,text='New to GitHub?',font=('arial',10),fg='black',bg='white')
        label6.place(x=40,y=30)

        label7 = tk.Label(frame2,text='Create an account',font=('arial',10),fg='blue',bg='white')
        label7.place(x=135,y=30)

        self.root.mainloop()

user = Git_hup()
