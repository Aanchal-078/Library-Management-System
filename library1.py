from tkinter import * 
import tkinter as tk
from tkinter import font, PhotoImage, ttk, simpledialog
import tkinter.messagebox as tm
import mysql.connector as c
conn = c.connect(user='root', password="", database='library')
from PIL import Image, ImageTk
import random
from tkinter import Label
import cv2
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

class LibraryMgmt:
    def __init__(self, parent):
        self.parent = parent
        self.front()

    def front(self):
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("Library Management System")
        self.parent.geometry("320x420")
        self.parent.configure(bg='black')
        self.custom1 = font.Font(family='Times New Roman', size=12)
        self.video_path = "D:/brilliko/python/Tkinter/main3.mp4" 
        self.cap = cv2.VideoCapture(self.video_path)
        self.label = Label(self.parent)
        self.label.pack()
        Button(self.parent, text='-> Next', bg='Black', font=self.custom1, fg='White', command=self.main).place(x=260, y=0)
        self.update3()
    def update3(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (320, 420))
            # Convert the frame to RGB (from BGR, which OpenCV uses)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to an ImageTk format to display it in Tkinter
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img  
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.parent.after(15, self.update3)


    def main(self):
        self.parent.destroy()
        self.parent = Tk()
        # Displaying the main page where user can choose to login or signup
        self.parent.title("Library Management System")
        self.parent.geometry("320x420")
        # Setting background to the screen
        self.video_path = "D:/brilliko/python/Tkinter/main2.mp4" 
        self.cap = cv2.VideoCapture(self.video_path)
        self.label = Label(self.parent)
        self.label.pack()
        self.update4()
        self.heading_font = font.Font(family='Palatino', size=34, weight="bold")
        self.custom_font = font.Font(family='Times New Roman', size=20)
        self.custom1 = font.Font(family='Times New Roman', size=12)
        #Displaying the labels and buttons on the screen
        Button(self.parent, text='<- Back', bg='Black', font=self.custom1, fg='White', command=self.front).place(x=0, y=0)
        Button(self.parent, text='New User', bg='#786b62',fg='white',width=13, font=self.custom_font, command=self.new_user).place(x=60, y=250)
        Button(self.parent, text='Existing User ', bg='#786b62', fg='White',width=13, font=self.custom_font, command=self.choose).place(x=60, y=330)

    def update4(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (320, 420))
            # Convert the frame to RGB (from BGR, which OpenCV uses)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to an ImageTk format to display it in Tkinter
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img  
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.parent.after(15, self.update4)

    def new_user(self):
        # Destroying previous screen and creating new screen
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("USER DETAILS FORM")
        self.parent.geometry("650x420")
        self.parent.configure(bg= '#cfc5ba')
        self.custom1 = font.Font(family='Times New Roman', size=12)
        self.custom_font1 = font.Font(family='Times New Roman', size=16)
        self.custom_font = font.Font(family='Times New Roman', size=14)

        self.video_path = "D:/brilliko/python/Tkinter/user_info1.mp4" 
        self.cap = cv2.VideoCapture(self.video_path)
        self.label = Label(self.parent)
        self.label.pack()
        self.update1()

        self.custom = font.Font(family='Gregorian', size=18, weight='bold')
        Button(self.parent, text='<- Back', bg='Black', font=self.custom1, fg='White', command=self.main).place(x=0, y=0)
        Label(self.parent, text='Name: ', font=self.custom, bg= '#cfc5ba').place(x=310, y=20)
        # Taking user input using Entry widget
        self.txts1 = Entry(self.parent, font=self.custom1, width=25)
        self.txts1.place(x=420, y=25)

        Label(self.parent, text='Age: ', font=self.custom , bg= '#cfc5ba').place(x=310, y=75)
        age_groups = ["0-12","13-19", "20-30", "31-42", "43-55","56-70" ,"71+"]
        self.selected_age_group = tk.StringVar()
        self.selected_age_group.set("Select your age group")  # Set the default option
        dropdown = tk.OptionMenu(self.parent, self.selected_age_group, *age_groups)
        dropdown.place(x=420, y=80, width=180, height=30)

        Label(self.parent, text='Gender: ', font=self.custom, bg= '#cfc5ba').place(x=310, y=130)
        self.selected_gender = tk.StringVar()
        self.selected_gender.set("Male")
        male_radio = tk.Radiobutton(self.parent, text="Male", variable=self.selected_gender, value="Male",font=self.custom_font, bg= '#cfc5ba')
        female_radio = tk.Radiobutton(self.parent, text="Female", variable=self.selected_gender, value="Female", font=self.custom_font, bg= '#cfc5ba')
        other_radio = tk.Radiobutton(self.parent, text="Other", variable=self.selected_gender, value="Other", font=self.custom_font, bg= '#cfc5ba')
        male_radio.place(x=420, y=135)
        female_radio.place(x=490, y=135)
        other_radio.place(x=575, y=135)

        Label(self.parent, text='Address: ', font=self.custom, bg= '#cfc5ba').place(x=308, y=185)
        self.txts3 = Entry(self.parent, font=self.custom1, width=25)
        self.txts3.place(x=420, y=190)

        Label(self.parent, text='E-Mail: ', font=self.custom , bg= '#cfc5ba').place(x=310, y=240)
        self.txts4 = Entry(self.parent, font=self.custom1, width=25)
        self.txts4.place(x=420, y=245)

        Label(self.parent, text='Mobile: ', font=self.custom, bg= '#cfc5ba').place(x=310, y=295)
        self.txts5 = Entry(self.parent, font=self.custom1, width=25)
        self.txts5.place(x=420, y=300)
        Button(self.parent, text='Submit', bg='black',width=23, font=self.custom_font1, fg='white', command=self.add_user).place(x=320, y=350)
    
    def update1(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (320, 420))
            # Convert the frame to RGB (from BGR, which OpenCV uses)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to an ImageTk format to display it in Tkinter
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img  
            self.label.place(relx=0, rely=0, relwidth=0.45, relheight=1)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.parent.after(5, self.update1)

    def show_user_id(self):
        name = self.txts1.get()
        tm.showinfo("User ID", f"Your User ID is: {self.user_id}")
        self.choose()
    
    def error_add_user(self):
        tm.showinfo("Error", "User with this mobile no. already exist!!!")
    def error_add_user1(self):
        tm.showinfo("Error", "Enter all Details")
    
    def add_user(self):
        name = self.txts1.get()
        age = self.selected_age_group.get()
        gender = self.selected_gender.get()
        address = self.txts3.get()
        email = self.txts4.get()
        mobile = self.txts5.get()
        sql = 'select mobile from user_info where mobile = %s'
        data=(mobile,)
        myc = conn.cursor()
        myc.execute(sql,data)
        res = myc.fetchall()
        result = ', '.join(str(i[0]) for i in res)
        if (mobile=="" or name=="" or age=="" or gender=="" or address=="" or email==""):
            self.error_add_user1()
        elif mobile in result:
            self.error_add_user()
        else:
            # If user doesn't exist it will insert data into database
            self.user_id = name[:3]+str(random.randint(10000,99999))
            sql = 'insert into user_info values(%s,%s,%s,%s,%s,%s,%s)'
            data=(self.user_id, name, age, gender, address, email, mobile)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
            self.show_user_id()

    def choose(self):
        self.parent.title("Choosing the Option")
        self.parent.geometry("715x420")
        self.custom1 = font.Font(family='Times New Roman', size=12)
        # Setting background to the screen
        self.image_path = Image.open("D:/brilliko/python/Tkinter/libray_choose.jpg")
        self.resized_image = self.image_path.resize((715, 420), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.resized_image)
        bg_label = Label(self.parent, image=self.bg_image)
        bg_label.place(relheight=1, relwidth=1)
        self.heading_font = font.Font(family='Palatino', size=34, weight="bold")
        self.custom_font = font.Font(family='Times New Roman', size=20)
        #Displaying the labels and buttons on the screen
        Button(self.parent, text='Borrow a book', bg='#5f4848',fg='white',width=13, font=self.custom_font, command=self.borrow_book).place(x=50, y=210)
        Button(self.parent, text='Return a book ', bg='#5f4848', fg='White',width=13, font=self.custom_font, command=self.return_book).place(x=300, y=210)
        Button(self.parent, text='Recommend a book ', bg='#5f4848', fg='White',width=15, font=self.custom_font, command=self.recommend_book).place(x=165, y=300)
        Button(self.parent, text='<- Back', bg='#5f4848', font=self.custom1, fg='White', command=self.main).place(x=0, y=0)

    def borrow_book(self):
        # Destroying previous screen and creating new screen
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("BOOK BORROW FORM")
        self.parent.geometry("650x420")
        self.parent.configure(bg='#bac6cf')
        self.custom_font1 = font.Font(family='Times New Roman', size=16)
        self.custom_font = font.Font(family='Times New Roman', size=14)
        
        self.video_path = "D:/brilliko/python/Tkinter/borrow_book.mp4" 
        self.cap = cv2.VideoCapture(self.video_path)
        self.label = Label(self.parent)
        self.label.pack()
        self.update2()

        self.custom = font.Font(family='Gregorian', size=16, weight='bold')
        self.custom1 = font.Font(family='Times New Roman', size=12)
        Button(self.parent, text='<- Back', bg='Black', font=self.custom1, fg='White', command=self.choose).place(x=0, y=0)
        Label(self.parent, text='User Id: ', bg='#bac6cf', font=self.custom).place(x=310, y=30)
        # Taking user input using Entry widget
        self.txtb1 = Entry(self.parent, font=self.custom1, width=25)
        self.txtb1.place(x=420, y=35)

        tk.Label(self.parent, text='Book Name: ', bg='#bac6cf', font=self.custom).place(x=310, y=90)
        self.selected_book_name = tk.StringVar()
        self.book_combobox = ttk.Combobox(self.parent, textvariable=self.selected_book_name, height=10)
        self.book_combobox.set("Select book name")
        self.book_combobox.place(x=450, y=95, width=180, height=30)
        self.book_combobox.bind("<<ComboboxSelected>>", self.on_book_selected)

        # Writer Name
        tk.Label(self.parent, text='Writer Name: ', bg='#bac6cf', font=self.custom).place(x=310, y=150)
        self.selected_writer_name = tk.StringVar()
        self.writer_combobox = ttk.Combobox(self.parent, textvariable=self.selected_writer_name, height=10)
        self.writer_combobox.set("Select writer name")
        self.writer_combobox.place(x=450, y=155, width=180, height=30)
        self.writer_combobox.bind("<<ComboboxSelected>>", self.on_writer_selected)

        # Populate initial dropdowns
        self.populate_comboboxes()
        
        Label(self.parent, text='Quantity: ', bg='#bac6cf', font=self.custom ).place(x=308, y=210)
        self.txtb2 = Entry(self.parent, font=self.custom1, width=25)
        self.txtb2.place(x=420, y=215)

        Label(self.parent, text='Duration: ' , bg='#bac6cf', font=self.custom ).place(x=310, y=270)
        self.txtb3 = Entry(self.parent, font=self.custom1, width=25)
        self.txtb3.place(x=420, y=275)

        Button(self.parent, text='Submit', bg='black',width=23, font=self.custom_font1, fg='white', command=self.add_book_issue).place(x=320, y=340)

    def update2(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (320, 420))
            # Convert the frame to RGB (from BGR, which OpenCV uses)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to an ImageTk format to display it in Tkinter
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img  
            self.label.place(relx=0, rely=0, relwidth=0.45, relheight=1)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.parent.after(5, self.update2)

    def populate_comboboxes(self):
        # Populate book names
        book_name = []
        sql = 'SELECT DISTINCT book_name FROM books_info'
        myc = conn.cursor()
        myc.execute(sql)
        res = myc.fetchall()
        for row in res:
            book_name.append(row[0])
        self.book_combobox['values'] = book_name
        writer_name = []
        sql = 'SELECT DISTINCT writer FROM books_info'
        myc.execute(sql)
        res = myc.fetchall()
        for row in res:
            writer_name.append(row[0])
        self.writer_combobox['values'] = writer_name

    def on_book_selected(self, event):
        selected_book = self.selected_book_name.get()
        writer_name = []
        sql = 'SELECT DISTINCT writer FROM books_info WHERE book_name = %s'
        myc = conn.cursor()
        myc.execute(sql, (selected_book,))
        res = myc.fetchall()
        for row in res:
            writer_name.append(row[0])
        self.writer_combobox['values'] = writer_name

    def on_writer_selected(self, event):
        selected_writer = self.selected_writer_name.get()
        book_name = []
        sql = 'SELECT DISTINCT book_name FROM books_info WHERE writer = %s'
        myc = conn.cursor()
        myc.execute(sql, (selected_writer,))
        res = myc.fetchall()
        for row in res:
            book_name.append(row[0])
        self.book_combobox['values'] = book_name

    def add_book_issue(self):
        user_id = self.txtb1.get()
        book_name = self.selected_book_name.get()
        writer_name = self.selected_writer_name.get()
        quantity = self.txtb2.get()
        duration = self.txtb3.get()
        sql = 'select id from user_info'
        myc = conn.cursor()
        myc.execute(sql)
        res = myc.fetchall()
        result = ', '.join(str(i[0]) for i in res)
        if user_id not in result:
            self.error_book_issue()
        elif (user_id=="" or book_name=="" or writer_name=="" or quantity=="" or duration==""):
            self.error_book_issue1()

        else:
            sql = 'insert into book_issue values(%s,%s,%s,%s,%s)'
            data=(user_id, book_name, writer_name, quantity, duration)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
            self.thankyou_borrow()
    def error_book_issue(self):
        tm.showinfo("Error", "User Id doesn't exist")
    def error_book_issue1(self):
        tm.showinfo("Error", "Enter all details")

    def thankyou_borrow(self):
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("THANK YOU")
        self.parent.geometry("450x420")
        self.parent.configure(bg='black')
        self.custom1 = font.Font(family='Times New Roman', size=12)
        self.video_path = "D:/brilliko/python/Tkinter/borrow.mp4" 
        self.cap = cv2.VideoCapture(self.video_path)
        self.label = Label(self.parent)
        self.label.pack()
        Button(self.parent, text='<- Back', bg='Black', font=self.custom1, fg='White', command=self.choose).place(x=0, y=0)
        Button(self.parent, text='Exit ->', bg='Black', font=self.custom1, fg='White', command=self.front).place(x=540, y=0)
        self.update()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (450, 420))
            # Convert the frame to RGB (from BGR, which OpenCV uses)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to an ImageTk format to display it in Tkinter
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img  
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.parent.after(5, self.update)

    def thankyou_return(self):
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("THANK YOU")
        self.parent.geometry("450x420")
        self.parent.configure(bg='black')
        self.custom1 = font.Font(family='Times New Roman', size=12)
        self.video_path = "D:/brilliko/python/Tkinter/return.mp4" 
        self.cap = cv2.VideoCapture(self.video_path)
        self.label = Label(self.parent)
        self.label.pack()
        Button(self.parent, text='<- Back', bg='Black', font=self.custom1, fg='White', command=self.choose).place(x=0, y=0)
        Button(self.parent, text='Exit ->', bg='Black', font=self.custom1, fg='White', command=self.front).place(x=540, y=0)
        self.update()

    def return_book(self):
        # Destroying previous screen and creating new screen
        self.parent.destroy()
        self.parent = Tk()
        self.parent.title("BOOK RETURN FORM")
        self.parent.geometry("650x420")
        self.parent.configure(bg='black')
        self.custom1 = font.Font(family='Times New Roman', size=12)
        self.custom_font1 = font.Font(family='Times New Roman', size=16)
        self.custom_font = font.Font(family='Times New Roman', size=14)
        
        self.video_path = "D:/brilliko/python/Tkinter/return_book.mp4" 
        self.cap = cv2.VideoCapture(self.video_path)
        self.label = Label(self.parent)
        self.label.pack()
        self.update_return()

        self.custom = font.Font(family='Gregorian', size=16, weight='bold')
        Button(self.parent, text='<- Back', bg='Black', font=self.custom1, fg='White', command=self.choose).place(x=0, y=0)
        Label(self.parent, text='User Id: ', bg='black', font=self.custom, fg='white').place(x=310, y=30)
        # Taking user input using Entry widget
        self.txtr1 = Entry(self.parent, font=self.custom1, width=25)
        self.txtr1.place(x=425, y=35)
        
        tk.Label(self.parent, text='Book Name: ', bg='black', font=self.custom, fg='white').place(x=310, y=90)
        self.selected_return_book_name = tk.StringVar()
        self.return_book_combobox = ttk.Combobox(self.parent, textvariable=self.selected_return_book_name, height=10)
        self.return_book_combobox.set("Select book name")
        self.return_book_combobox.place(x=450, y=95, width=180, height=30)
        self.return_book_combobox.bind("<<ComboboxSelected>>", self.on_return_book_selected)

        # Writer Name
        tk.Label(self.parent, text='Writer Name: ', bg='black', font=self.custom, fg='white').place(x=310, y=150)
        self.selected_return_writer_name = tk.StringVar()
        self.return_writer_combobox = ttk.Combobox(self.parent, textvariable=self.selected_return_writer_name, height=10)
        self.return_writer_combobox.set("Select writer name")
        self.return_writer_combobox.place(x=450, y=155, width=180, height=30)
        self.return_writer_combobox.bind("<<ComboboxSelected>>", self.on_return_writer_selected)

        # Populate initial dropdowns
        self.return_populate_comboboxes()
        Label(self.parent, text='Rating: ', bg='black', font=self.custom , fg='white').place(x=310, y=210)
        self.txtr2 = Entry(self.parent, font=self.custom1, width=25)
        self.txtr2.place(x=425, y=215)

        Label(self.parent, text='Feedback: ' , bg='black', font=self.custom, fg='white' ).place(x=310, y=270)
        self.txtr3 = Entry(self.parent, font=self.custom1, width=25)
        self.txtr3.place(x=425, y=275)

        Button(self.parent, text='Submit', bg='black',width=23, font=self.custom_font1, fg='white', command=self.add_book_return).place(x=320, y=340)

    def update_return(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (310, 420))
            # Convert the frame to RGB (from BGR, which OpenCV uses)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to an ImageTk format to display it in Tkinter
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img  
            self.label.place(relx=0, rely=0, relwidth=0.4, relheight=1)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.parent.after(5, self.update2)

    def return_populate_comboboxes(self):
        if not conn.is_connected():
            conn.reconnect()
        # Populate book names
        book_name = []
        sql = 'SELECT DISTINCT book_name FROM books_info'
        myc = conn.cursor()
        myc.execute(sql,)
        res = myc.fetchall()
        for row in res:
            book_name.append(row[0])
        self.return_book_combobox['values'] = book_name
        writer_name = []
        sql = 'SELECT DISTINCT writer FROM books_info'
        myc.execute(sql)
        res = myc.fetchall()
        for row in res:
            writer_name.append(row[0])
        self.return_writer_combobox['values'] = writer_name

    def on_return_book_selected(self, event):
        selected_book = self.selected_return_book_name.get()
        writer_name = []
        sql = 'SELECT DISTINCT writer FROM books_info WHERE book_name = %s'
        myc = conn.cursor()
        myc.execute(sql, (selected_book,))
        res = myc.fetchall()
        for row in res:
            writer_name.append(row[0])
        self.return_writer_combobox['values'] = writer_name

    def on_return_writer_selected(self, event):
        selected_writer = self.selected_return_writer_name.get()
        book_name = []
        sql = 'SELECT DISTINCT book_name FROM books_info WHERE writer = %s'
        myc = conn.cursor()
        myc.execute(sql, (selected_writer,))
        res = myc.fetchall()
        for row in res:
            book_name.append(row[0])
        self.return_book_combobox['values'] = book_name

    def add_book_return(self):
        id = self.txtr1.get()
        book_name = self.selected_return_book_name.get()
        writer_name = self.selected_return_writer_name.get()
        ratings = self.txtr2.get()
        feedback = self.txtr3.get()
        sql = 'select id, book_name, writer_name from book_issue where id=%s AND book_name = %s AND writer_name = %s'
        data = (id,book_name, writer_name)
        myc = conn.cursor()
        myc.execute(sql,data)
        res = myc.fetchall()
        if len(res) == 0:
            tm.showerror("Error", "ID, Book Name, or Writer Name do not match with Book Issued data.")
        else:
            sql = 'insert into book_return values(%s,%s,%s,%s,%s)'
            data=(id, book_name, writer_name, ratings, feedback)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
            self.thankyou_return()
     
    def recommend_book(self):
        user_id = simpledialog.askstring("User ID", "Please enter your user ID:")
        sql = 'SELECT id FROM user_info'
        myc = conn.cursor()
        myc.execute(sql)
        res = myc.fetchall()
    
    # Convert the result directly into a list of IDs
        user_ids = [str(i[0]) for i in res]
        if user_id not in user_ids:
            self.error_book_issue()
        else:
            self.parent.destroy()
            self.parent = Tk()
            self.parent.geometry("600x420")
            self.parent.title("Book Recommendations")
        # Background Image (for the left side)
            self.video_path = "D:/brilliko/python/Tkinter/recommend.mp4" 
            self.cap = cv2.VideoCapture(self.video_path)
            self.label = Label(self.parent)
            self.label.pack()
            self.update_recommend()  # Place the background image on half screen

        # Right Side for Book Recommendations
            self.book_list_frame = tk.Frame(self.parent, bg="#453a32")
            self.book_list_frame.place(relx=0.42, rely=0, relheight=1, relwidth=0.58)
            self.custom1 = font.Font(family='Times New Roman', size=12)
            Button(self.parent, text='<- Back', bg='Black', font=self.custom1, fg='White', command=self.choose).place(x=0, y=0)
            myc = conn.cursor()
        
            query = f"SELECT book_name FROM book_issue WHERE id = %s"
            data = (user_id,)
            myc.execute(query, data)
            issued_books = myc.fetchall()
            issued_books_df = pd.DataFrame(issued_books, columns=['book_name'])

        # Fetch full book data from the database
            book_data_query = "SELECT * FROM books_info"
            book_data = pd.read_sql(book_data_query, conn)

            if not issued_books_df.empty:
                book_name1 = issued_books_df['book_name'].values[0]
            else:
                random_books = book_data.sample(12)
                self.display_books(random_books['book_name'].tolist())
                return

        # Create combined features for recommendation
            selected_features = ['book_name', 'genre', 'writer', 'language']
            book_data['combined_features'] = book_data[selected_features].apply(lambda x: ' '.join(x), axis=1)

        # Apply TF-IDF Vectorizer
            vectorizer = TfidfVectorizer()
            feature_vector = vectorizer.fit_transform(book_data['combined_features'])

            similarity = cosine_similarity(feature_vector)

        # Find close matches
            list_of_all_titles = book_data['book_name'].tolist()
            find_close_match = difflib.get_close_matches(book_name1, list_of_all_titles)

            if find_close_match:
                close_match = find_close_match[0]
                index_of_book = book_data[book_data.book_name == close_match].index[0]
                similarity_score = list(enumerate(similarity[index_of_book]))
                sorted_similar_books = sorted(similarity_score, key=lambda x: x[1], reverse=True)

            # Get the top 15 recommended books
                recommended_books = []
                seen_books = set()  # To keep track of already added books

                for i, book in enumerate(sorted_similar_books[1:], 1):  # Skip the first one (itself)
                    index = book[0]
                    title_from_index = book_data.iloc[index]['book_name']

    # Only add if the book title is not already in the recommended list
                    if title_from_index not in seen_books:
                        recommended_books.append(title_from_index)
                        seen_books.add(title_from_index)
    
    # Stop when we have 15 distinct books
                    if len(recommended_books) == 15:
                        break

            
                self.display_books(recommended_books)
            else:
                tm.showinfo("No Match", "No close matches found for the issued book.")

    def update_recommend(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (275, 420))
            # Convert the frame to RGB (from BGR, which OpenCV uses)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to an ImageTk format to display it in Tkinter
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img  
            self.label.place(relx=0, rely=0, relwidth=0.42, relheight=1)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.parent.after(5, self.update_recommend)

    def display_books(self, books):
        label = tk.Label(self.book_list_frame, text="Recommended Books", font=("Algerian", 24), bg="#453a32", fg="White")
        label.place(x=5, y=10)  # Position the heading at the top center of the right frame
        y_position = 60
        for i, book in enumerate(books, 1):
            book_label = tk.Label(self.book_list_frame, text=f"{i}. {book}", font=("Arial", 12), bg="#453a32", fg="White")
        # Position each book label at a new line with some padding (spacing)
            book_label.place(x=10, y=y_position)
            y_position += 30  # Adjust the spacing as needed

if __name__ == "__main__":
    parent = Tk()
    app = LibraryMgmt(parent)
    parent.mainloop()
