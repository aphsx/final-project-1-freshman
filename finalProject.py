import sqlite3
from tkinter import *
from tkinter import Frame, Entry, Button
import tkinter as tk
from tkinter import messagebox

print("hello word")

def connect_database():
    global connection, cursor
    connection = sqlite3.connect('db/school.db')
    cursor = connection.cursor()
    
def main():
    root = tk.Tk()
    root.title("Final Project By IG: _aphsx")
    
    # Get screen dimensions
    window_width = 1270
    window_height = 720
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    
    # Calculate position to center the window
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    
    # Set window geometry
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    
    # Configure menu bar
    menubar = Menu(root)
    root.config(bg="#A79277", menu=menubar)

    # Configure rows and columns
    root.rowconfigure((0,1) ,weight=1)
    root.columnconfigure(0,weight=1)
    

    # Create program menu
    program_menu = Menu(menubar, tearoff=0)
    program_menu.add_command(label='Open', command=open_home_page)  # เรียกใช้งาน open_home_page โดยระบุคำสั่งในเมนู
    program_menu.add_separator()
    program_menu.add_command(label='Exit', command=root.destroy)
    menubar.add_cascade(label="Program", menu=program_menu)

    # Create profile menu
    profile_menu = Menu(menubar, tearoff=0)
    profile_menu.add_command(label='Admin',command=login_page)
    profile_menu.add_command(label='Log In',command=login_page)
    profile_menu.add_command(label='Close Program', command=root.destroy)
    menubar.add_cascade(label="Modify", menu=profile_menu)
    
    return root

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(crosshairinfo.get())

def create_main_frame():
    global fr1
    fr1 = Frame(root)  # ลบพารามิเตอร์ bg ออก
    fr1.grid(row=0, column=0, columnspan=2, rowspan=2, sticky='news')
    fr1.config(bg='#FFF2E1')
    
    label_valorant = Label(root, text="Pro player Setting", font=("Calibri bold",36), bg="#FFF2E1", fg="#EAD8C0")
    label_valorant.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    return fr1

def login_click():
    global user_result
    
    user = username_var.get()
    pwd = password_var.get()
    if username_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning("Admin", "Please enter username first.")
        username_entry.focus_force()
    else:
        sql = "SELECT * FROM login WHERE user=?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()
        if result:
            sql = "SELECT * FROM login WHERE user=? AND pwd=?"
            cursor.execute(sql, [user, pwd])
            user_result = cursor.fetchone()
            if user_result:
                messagebox.showinfo("Admin", "Login Successful")
                print(user_result)
                username_var.set("")
                password_var.set("")
                admin_page()
            else:
                messagebox.showwarning("Admin", "Incorrect Username or Password.")
                password_entry.delete(0, END)
                password_entry.focus_force()
        else:
            messagebox.showerror("Admin", "Username not found. Please register before login.")
            username_entry.delete(0, END)
            username_entry.focus_force()

def login_page():
    global username_entry, password_entry,login_frame
    
    main_frame = Frame(root)
    main_frame.rowconfigure((0), weight=1)
    main_frame.columnconfigure((0,1,2), weight=3)
    main_frame.columnconfigure((3), weight=1)
    main_frame.place(relx=0.5,rely=0.5,anchor=CENTER,relheight=1,relwidth=1) 
    
    left_frame = Frame(main_frame, bg="#FFF2E1")
    left_frame.rowconfigure((0, 1), weight=1)
    left_frame.columnconfigure((0), weight=1)
    left_frame.grid(row=0,rowspan=2, column=0,columnspan=3,sticky="news")
    
    login_frame = Frame(main_frame, bg="#EAD8C0")
    login_frame.rowconfigure((0), weight=7)
    login_frame.rowconfigure(( 1,6,7), weight=4)
    login_frame.rowconfigure(( 2, 3, 4,5), weight=1)
    login_frame.columnconfigure((0), weight=1)
    login_frame.grid(row=0,rowspan=2, column=3,columnspan=2,sticky="news")

    lbl_imagelogin = Label(login_frame, image=img4,bg='#EAD8C0')
    lbl_imagelogin.grid(row=0, column=0,sticky="s")
    
    label_1 = Label(login_frame, text="Account Login", bg="#EAD8C0",font=("Calibri bold", 20),fg="black")
    label_1.grid(row=1, column=0,sticky="s")

    label_2 = Label(login_frame, text="Username", bg="#EAD8C0",font=("yu gothic ui", 14, "bold"),fg="black")
    label_2.grid(row=2, column=0, sticky="s")
    username_entry = Entry(login_frame, bg="#FFFFFF",font=("yu gothic ui", 14, "bold"), width=20, textvariable=username_var)
    username_entry.grid(row=3, column=0, sticky="n")

    label_3 = Label(login_frame, text="Password", bg="#EAD8C0",font=("yu gothic ui", 14, "bold"),fg="black")
    label_3.grid(row=4, column=0, sticky="s")
    password_entry = Entry(login_frame, bg="#FFFFFF",font=("yu gothic ui", 14, "bold"), width=20, textvariable=password_var, show="*")
    password_entry.grid(row=5, column=0, sticky="n")
    
    button_3 = Button(login_frame, text="Login", width=20, height=2, bg="#A79277",command=login_click)
    button_3.grid(row=6, column=0,sticky="s")
    
    button_1 = Button(login_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#EAD8C0"
                                    , borderwidth=0, background="#EAD8C0", cursor="hand2",command=register_page)
    button_1.grid(row=7, column=0, sticky="n")
    
    label_1 = Label(left_frame, text="VALORANT is a free-to-play first-person   \n hero shooter developed and published by Riot Games. It’s 5v5, \n competitive, and character-based.",
                                    bg="#FFF2E1",font=("Calibri bold", 20),fg="#A79277")
    label_1.grid(row=0, column=0,sticky="s")
    
def register_page():
    global registerusername_entry,registerpassword_entry,registername_entry,registerlastname_entry
    
    main_frame = Frame(root)
    main_frame.rowconfigure((0), weight=1)
    main_frame.columnconfigure((0,1,2), weight=3)
    main_frame.columnconfigure((3), weight=1)
    main_frame.place(relx=0.5,rely=0.5,anchor=CENTER,relheight=1,relwidth=1) 
    left_frameregister = Frame(main_frame, bg="#EAD8C0")
    
    left_frameregister.rowconfigure((0, 1,2,3,4,5), weight=1)
    left_frameregister.columnconfigure((0,1), weight=1)
    left_frameregister.grid(row=0,rowspan=2, column=0,columnspan=3,sticky="news")
    register_frame = Frame(main_frame, bg="#FFF2E1")
    register_frame.rowconfigure((0,1,2,3,4), weight=1)
    register_frame.columnconfigure((0), weight=1)
    register_frame.grid(row=0,rowspan=2, column=3,columnspan=2,sticky="news")

    Label(register_frame, image=img4,bg='#FFF2E1').grid(row=0, column=0,sticky="s")
    Label(register_frame, text="Register form", bg="#FFF2E1",font=("Calibri bold", 20),fg="black").grid(row=2, column=0,sticky="n")
    Button(register_frame, text="Submit", width=20, height=2, bg="#D1BB9E",command=register).grid(row=3, column=0,sticky="n")
    Button(register_frame, text="Back", width=20, height=2, bg="#D1BB9E",command=login_page).grid(row=4, column=0,sticky="n")
    
    Label(left_frameregister, text="Username : ",bg="#EAD8C0",fg="black",font=("Calibri bold", 20)).grid(row=1, column=0,sticky="e")
    Label(left_frameregister, text="Password : ",bg="#EAD8C0",fg="black",font=("Calibri bold", 20)).grid(row=2, column=0,sticky="e")
    Label(left_frameregister, text="First Name : ",bg="#EAD8C0",fg="black",font=("Calibri bold", 20)).grid(row=3, column=0,sticky="e")
    Label(left_frameregister, text="Last Name : ",bg="#EAD8C0",fg="black",font=("Calibri bold", 20)).grid(row=4, column=0,sticky="e")
    
    registerusername_entry = Entry(left_frameregister, bg="#FFFFFF",font=("yu gothic ui", 14, "bold"), width=20)
    registerusername_entry.grid(row=1, column=1, sticky="w")
    registerpassword_entry = Entry(left_frameregister, bg="#FFFFFF",font=("yu gothic ui", 14, "bold"), width=20)
    registerpassword_entry.grid(row=2, column=1, sticky="w")
    registername_entry = Entry(left_frameregister, bg="#FFFFFF",font=("yu gothic ui", 14, "bold"), width=20)
    registername_entry.grid(row=3, column=1, sticky="w")
    registerlastname_entry = Entry(left_frameregister, bg="#FFFFFF",font=("yu gothic ui", 14, "bold"), width=20)
    registerlastname_entry.grid(row=4, column=1, sticky="w")
    
def register():
    if registerusername_entry.get() == "":
        messagebox.showwarning("Admin", "Please enter student ID.")
        registerusername_entry.focus_force()
    elif registerpassword_entry.get() == "":
        messagebox.showwarning("Admin", "Please enter first name.")
        registerusername_entry.focus_force()
    elif registername_entry.get() == "":
        messagebox.showwarning("Admin", "Please enter first name.")
        registername_entry.focus_force()
    elif registerlastname_entry.get() == "":
        messagebox.showwarning("Admin", "Please enter first name.")
        registerlastname_entry.focus_force()
    else:
        # ทำการเช็คว่า username ซ้ำหรือไม่
        sql = "SELECT * FROM login WHERE user=? "
        cursor.execute(sql, [registerusername_entry.get()])
        result = cursor.fetchall()
        if result:
            messagebox.showwarning("Admin", "Username already exists.")
        else:
            try:
                # เพิ่มข้อมูลลงในฐานข้อมูล
                sql = """INSERT INTO login (user, pwd,fname,lname) 
                         VALUES (?, ?, ?, ?)"""
                params = (registerusername_entry.get(), registerpassword_entry.get(), registername_entry.get(),
                         registerlastname_entry.get())
                cursor.execute(sql, params)
                connection.commit()
                messagebox.showinfo("Admin", "Registration successful!")
                # เรียกฟังก์ชัน login_layout() เพื่อกลับสู่หน้า login
                login_page()
            except Exception as e:
                messagebox.showerror("Admin", "Error occurred while registering: " + str(e))

        
def admin_page():
    global name_search_entry,right_frame,entry_name,entry_realname,entry_birth,entry_team,entry_country,entry_dpi,entry_sen
    global entry_winsen,entry_eDPI,entry_scpoedsen,entry_ads_sen,entry_rawinput,entry_hz,entry_crosshair
    profile_page = Frame(root, bg="#B9E3EE")
    profile_page.rowconfigure((0), weight=1)
    profile_page.columnconfigure((1, 2,3), weight=3)
    profile_page.columnconfigure((0), weight=1)
    profile_page.place(relx=0.5,rely=0.5,anchor=CENTER,relheight=1,relwidth=1)
    
    adminlogin_frame = Frame(profile_page, bg="#EAD8C0")
    adminlogin_frame.rowconfigure((0), weight=7)
    adminlogin_frame.rowconfigure(( 1,6,7), weight=4)
    adminlogin_frame.rowconfigure(( 2, 3, 4,5), weight=1)
    adminlogin_frame.columnconfigure((0), weight=1)
    adminlogin_frame.grid(row=0,rowspan=2, column=0,sticky="news")
    
    right_frame = Frame(profile_page, bg="#FFF2E1")
    right_frame.rowconfigure((0), weight=3)
    right_frame.rowconfigure((1,2,3,4,5,6,7,8,9), weight=1)
    right_frame.columnconfigure((0,1,2,3), weight=1)
    right_frame.grid(row=0,rowspan=2, column=1,columnspan=3,sticky="news")
#adminprofile
    adminlbl_imagelogin = Label(adminlogin_frame, image=img4,bg='#EAD8C0')
    adminlbl_imagelogin.grid(row=0, column=0,sticky="s")
    adminlabel_1 = Label(adminlogin_frame, text="Account Admin", bg="#EAD8C0",font=("Calibri bold", 20),fg="black")
    adminlabel_1.grid(row=1, column=0,sticky="s")
    adminlabel_2 = Label(adminlogin_frame, text="User", bg="#EAD8C0",font=("yu gothic ui", 14, "bold"),fg="black")
    adminlabel_2.grid(row=2, column=0, sticky="s")
    adminusername = Label(adminlogin_frame, text=""+str(user_result[2]), bg="#EAD8C0",font=("yu gothic ui", 14, "bold"),fg="black")
    adminusername.grid(row=3, column=0, sticky="s")
    adminpassword = Label(adminlogin_frame, text=""+str(user_result[3]), bg="#EAD8C0",font=("yu gothic ui", 14, "bold"),fg="black")
    adminpassword.grid(row=4, column=0, sticky="n") 
    
    ##search bar
    label_search_name = Label(right_frame, text="Enter player name :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_search_name.grid(row=0, column=0, sticky="e")
    name_search_entry=Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=40)
    name_search_entry.grid(row=0, column=1,columnspan=2)
    search_button = Button(right_frame, text="Search", width=20, height=2, bg="#EAD8C0",command=find_ID)
    search_button.grid(row=0, column=3,sticky="w")
    
    ##result
    label_name = Label(right_frame, text="name :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_name.grid(row=1, column=0, sticky="e")
    label_realname = Label(right_frame, text="Realname :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_realname.grid(row=2, column=0, sticky="e")
    label_birth = Label(right_frame, text="Birth :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_birth.grid(row=3, column=0, sticky="e")
    label_team = Label(right_frame, text="Team :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_team.grid(row=4, column=0, sticky="e")
    label_country = Label(right_frame, text="Country :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_country.grid(row=5, column=0, sticky="e")
    label_dpi = Label(right_frame, text="DPI :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_dpi.grid(row=6, column=0, sticky="e")
    label_sen = Label(right_frame, text="Sen :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_sen.grid(row=6, column=0, sticky="e")
    
    label_winsen = Label(right_frame, text="Windows Sensitivity :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_winsen.grid(row=1, column=2, sticky="e")
    label_eDPI = Label(right_frame, text="eDPI :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_eDPI.grid(row=2, column=2, sticky="e")
    label_scpoedsen = Label(right_frame, text="Scoped Sensitivity :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_scpoedsen.grid(row=3, column=2, sticky="e")
    label_ads_sen = Label(right_frame, text="ADS Sensitivity :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_ads_sen.grid(row=4, column=2, sticky="e")
    label_rawinput = Label(right_frame, text="Raw Input Buffer :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_rawinput.grid(row=5, column=2, sticky="e")
    label_hz = Label(right_frame, text="Hz", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_hz.grid(row=6, column=2, sticky="e")
    
    entry_name=Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_name.grid(row=1, column=1, sticky="w")
    entry_realname = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_realname.grid(row=2, column=1, sticky="w")
    entry_birth = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_birth.grid(row=3, column=1, sticky="w")
    entry_team = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_team.grid(row=4, column=1, sticky="w")
    entry_country = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_country.grid(row=5, column=1, sticky="w")
    entry_dpi = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_dpi.grid(row=6, column=1, sticky="w")
    entry_sen = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_sen.grid(row=6, column=1, sticky="w")
    
    entry_winsen=Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_winsen.grid(row=1, column=3, sticky="w")
    entry_eDPI = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_eDPI.grid(row=2, column=3, sticky="w")
    entry_scpoedsen = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_scpoedsen.grid(row=3, column=3, sticky="w")
    entry_ads_sen = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_ads_sen.grid(row=4, column=3, sticky="w")
    entry_rawinput = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_rawinput.grid(row=5, column=3, sticky="w")
    entry_hz = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=20)
    entry_hz.grid(row=6, column=3, sticky="w")
    
    label_crosshair = Label(right_frame, text="Crosshair Code :", bg="#FFF2E1",font=("yu gothic ui", 14, "bold"),fg="black")
    label_crosshair.grid(row=7, column=1)
    entry_crosshair = Entry(right_frame, bg="#FFFFFF",font=("yu gothic ui", 12, "bold"), width=30)
    entry_crosshair.grid(row=7, column=2,columnspan=2, sticky="w")
    
    button_addinfo = Button(right_frame, text="Add player", width=20, height=2, bg="#EAD8C0",command=add_players)
    button_addinfo.grid(row=8, column=0)
    button_updateinfo = Button(right_frame, text="Update", width=20, height=2, bg="#EAD8C0",command=update_players)
    button_updateinfo.grid(row=8, column=1)
    button_backtohome = Button(right_frame, text="Back Home", width=20, height=2, bg="#EAD8C0",command=delete_players)
    button_backtohome.grid(row=8, column=2)
    button_clearinfo = Button(right_frame, text="Clear", width=20, height=2, bg="#EAD8C0",command=clearinfo)
    button_clearinfo.grid(row=8, column=3)
    
def find_ID():
    global student_info

    entry_name.delete(0, "end")
    entry_realname.delete(0, "end")
    entry_birth.delete(0, "end")
    entry_team.delete(0, "end")
    entry_country.delete(0, "end")
    entry_dpi.delete(0, "end")
    entry_sen.delete(0, "end")
    entry_winsen.delete(0, "end")
    entry_eDPI.delete(0, "end")
    entry_scpoedsen.delete(0, "end")
    entry_ads_sen.delete(0, "end")
    entry_rawinput.delete(0, "end")
    entry_hz.delete(0, "end")
    entry_crosshair.delete(0, "end")
    
    if name_search_entry.get() == "":
        messagebox.showwarning("Admin", "Please enter Student ID")
        name_search_entry.focus_force()
    else:
        sql = "SELECT * FROM players WHERE player_name=?"
        param = [name_search_entry.get()]
        cursor.execute(sql, param)
        student_info = cursor.fetchone()
        print(student_info)
        if student_info:
            entry_name.insert(0, student_info[0])
            entry_realname.insert(0, student_info[1])
            entry_birth.insert(0, student_info[2])
            entry_team.insert(0, student_info[3])
            entry_country.insert(0, student_info[4])
            entry_dpi.insert(0, student_info[5])
            entry_sen.insert(0, student_info[6])
        
            entry_winsen.insert(0, student_info[7])
            entry_eDPI.insert(0, student_info[8])
            entry_scpoedsen.insert(0, student_info[9])
            entry_ads_sen.insert(0, student_info[10])
            entry_rawinput.insert(0, student_info[11])
            entry_hz.insert(0, student_info[12])

            entry_crosshair.insert(0, student_info[13])
        else:
            messagebox.showwarning("Admin", "Not Found ID in DATABASE")
            
def add_players():
    sql = "INSERT INTO players (player_name, real_name, birth, team, country, dpi, sen, winsen, edpi, scopedsen, adssen, rawinput, hz, crosshair) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    params = (entry_name.get(), entry_realname.get(), entry_birth.get(), entry_team.get(), entry_country.get(), entry_dpi.get(), entry_sen.get(), entry_winsen.get(), entry_eDPI.get(), entry_scpoedsen.get(), entry_ads_sen.get(), entry_rawinput.get(), entry_hz.get(), entry_crosshair.get())
    cursor.execute(sql, params)
    connection.commit()
    messagebox.showinfo("Success", "Player added successfully.")
    
def update_players():
    sql = "UPDATE players SET player_name=?, real_name=?, birth=?, team=?, country=?, dpi=?, sen=?, winsen=?, edpi=?, scopedsen=?, adssen=?, rawinput=?, hz=?, crosshair=? WHERE player_name=?"
    cursor.execute(sql, (entry_name.get(), entry_realname.get(), entry_birth.get(), entry_team.get(), entry_country.get(), entry_dpi.get(), entry_sen.get(), entry_winsen.get(), entry_eDPI.get(), entry_scpoedsen.get(), entry_ads_sen.get(), entry_rawinput.get(), entry_hz.get(), entry_crosshair.get(), entry_name.get()))
    connection.commit()
    messagebox.showinfo("Admin", "Player information updated successfully!")
        
def clearinfo():
    entry_name.delete(0, "end")
    entry_realname.delete(0, "end")
    entry_birth.delete(0, "end")
    entry_team.delete(0, "end")
    entry_country.delete(0, "end")
    entry_dpi.delete(0, "end")
    entry_sen.delete(0, "end")
    entry_winsen.delete(0, "end")
    entry_eDPI.delete(0, "end")
    entry_scpoedsen.delete(0, "end")
    entry_ads_sen.delete(0, "end")
    entry_rawinput.delete(0, "end")
    entry_hz.delete(0, "end")
    entry_crosshair.delete(0, "end")
    
def open_home_page():
    global name_profile,playersearch_entry,nameinfo,teaminfo,birthinfo,country_info
    global dpiproinfo,seninfo,scopedinfo,adsinfo,edpiproinfo,hzinfo,winseninfo,ripinfo,crosshairinfo
    open_home_page = Frame(root)
    open_home_page.rowconfigure((0), weight=1)
    open_home_page.columnconfigure((1), weight=3)
    open_home_page.columnconfigure((0), weight=1)
    open_home_page.place(relx=0.5,rely=0.5,anchor=CENTER,relheight=1,relwidth=1)
    
    left_frame_profile  = Frame(open_home_page, bg="#EAD8C0")
    left_frame_profile .rowconfigure((0), weight=1)
    left_frame_profile .rowconfigure((1,2,3,4), weight=3)
    left_frame_profile .columnconfigure((0,1,2,3), weight=1)
    left_frame_profile .grid(row=0,column=0,sticky="news")
    right_frame_profile = Frame(open_home_page, bg="#FFF2E1")
    right_frame_profile.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)
    right_frame_profile.columnconfigure((0,1), weight=1)
    right_frame_profile.grid(row=0,column=1,columnspan=3,sticky="news")
    
    Label(left_frame_profile, text="Search",font=("Calibri bold",20),bg='#EAD8C0').grid(row=0,column=0)
    Entry(left_frame_profile,font=("yu gothic ui", 16, "bold"),bg="white",textvariable=playersearch_entry).grid(row=0,column=1,columnspan=2)
    Button(left_frame_profile, text="Search",bg="#D1BB9E",command=find_playername,width=7,height=2).grid(row=0, column=3)
    Label(left_frame_profile, image=img7,bg='#EAD8C0').grid(row=1,column=0,columnspan=4)
    Label(left_frame_profile, text="Name : ",font=("Calibri bold",18),bg='#EAD8C0').grid(row=3,column=0,sticky="e")
    Label(left_frame_profile, text="Team : ",font=("Calibri bold",18),bg='#EAD8C0').grid(row=3,column=2,sticky="e")
    Label(left_frame_profile, text="Birth : ",font=("Calibri bold",18),bg='#EAD8C0').grid(row=4,column=0,sticky="e")
    Label(left_frame_profile, text="Country : ",font=("Calibri bold",18),bg='#EAD8C0').grid(row=4,column=2,sticky="e")
    Label(right_frame_profile, text="Proplayer Valorant Setting",font=("Calibri bold",22),bg='#FFF2E1').grid(row=0,column=0,columnspan=2,sticky="news")
    Label(right_frame_profile, text="DPI :",font=("yu gothic ui", 16, "bold"),bg='#FFF2E1').grid(row=1,column=0,padx=10,pady=10,sticky="e")
    Label(right_frame_profile, text="Sentivity : ",font=("yu gothic ui", 16, "bold"),bg='#FFF2E1').grid(row=2,column=0,padx=10,pady=10,sticky="e")
    Label(right_frame_profile, text="Scoped Sentivity : ",font=("yu gothic ui", 16, "bold"),bg='#FFF2E1').grid(row=3,column=0,padx=10,pady=10,sticky="e")
    Label(right_frame_profile, text="ADS Sentivity : ",font=("yu gothic ui", 16, "bold"),bg='#FFF2E1').grid(row=4,column=0,padx=10,pady=10,sticky="e")
    Label(right_frame_profile, text="eDPI : ",font=("yu gothic ui", 16, "bold"),bg='#FFF2E1').grid(row=5,column=0,padx=10,pady=10,sticky="e")
    Label(right_frame_profile, text="Hz : ",font=("yu gothic ui", 16, "bold"),bg='#FFF2E1').grid(row=6,column=0,padx=10,pady=10,sticky="e")
    Label(right_frame_profile, text="Windows Sensitivity : ",font=("yu gothic ui", 16, "bold"),bg='#FFF2E1').grid(row=7,column=0,padx=10,pady=10,sticky="e")
    Label(right_frame_profile, text="Raw Input Buffer : ",font=("yu gothic ui", 16, "bold"),bg='#FFF2E1').grid(row=8,column=0,padx=10,pady=10,sticky="e")
    
    name_profile = Label(left_frame_profile, text="Proplayer",font=("Calibri bold",24),bg='#EAD8C0')
    name_profile.grid(row=2,column=0,columnspan=4)
    nameinfo = Label(left_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=10)
    nameinfo.grid(row=3,column=1,sticky="w")
    teaminfo = Label(left_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=10)
    teaminfo.grid(row=3,column=3,sticky="w")
    birthinfo = Label(left_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=10)
    birthinfo.grid(row=4,column=1,sticky="w")
    country_info = Label(left_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=10)
    country_info.grid(row=4,column=3,sticky="w")
    dpiproinfo = Label(right_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=20)
    dpiproinfo.grid(row=1,column=1,sticky="w")
    seninfo = Label(right_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=20)
    seninfo.grid(row=2,column=1,sticky="w")
    scopedinfo = Label(right_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=20)
    scopedinfo.grid(row=3,column=1,sticky="w")
    adsinfo = Label(right_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=20)
    adsinfo.grid(row=4,column=1,sticky="w")
    edpiproinfo = Label(right_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=20)
    edpiproinfo.grid(row=5,column=1,sticky="w")
    hzinfo = Label(right_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=20)
    hzinfo.grid(row=6,column=1,sticky="w")
    winseninfo = Label(right_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=20)
    winseninfo.grid(row=7,column=1,sticky="w")
    ripinfo = Label(right_frame_profile, text="",font=("yu gothic ui", 16, "bold"),bg='white',width=20)
    ripinfo.grid(row=8,column=1,sticky="w")
    
    crosshairinfo=Entry(right_frame_profile, bg="#FFFFFF",font=("yu gothic ui", 16, "bold"), width=20)
    crosshairinfo.grid(row=10,column=0)
    Button(right_frame_profile, text="Coppy Crosshair Code",bg="#D1BB9E",command=copy_text).grid(row=10, column=1)

def delete_players():
    player_name = entry_name.get()

    # ตรวจสอบว่าชื่อผู้เล่นไม่ว่างเปล่า
    if not player_name:
        messagebox.showerror("Error", "Please enter the player's name.")
        return
    # ลบข้อมูลผู้เล่นจากฐานข้อมูล
    sql = "DELETE FROM players WHERE player_name = ?"
    cursor.execute(sql, (player_name,))
    # ยืนยันการเปลี่ยนแปลงและปิดการเชื่อมต่อ
    connection.commit()
    messagebox.showinfo("Success", "Player data deleted successfully.")

    
def find_playername():
    if playersearch_entry.get() == "":
        messagebox.showwarning("Admin", "Please enter Student ID")
        playersearch_entry.focus_force()
    else:
        sql = "SELECT * FROM players WHERE player_name=?"
        param = [playersearch_entry.get()]
        cursor.execute(sql, param)
        player_info = cursor.fetchone()
        print(player_info)
        if player_info:
            name_profile.config(text="" + player_info[0])
            nameinfo.config(text="" + player_info[1])
            birthinfo.config(text="" + player_info[2])
            teaminfo.config(text="" + player_info[3])
            country_info.config(text="" + player_info[4])
            
            dpiproinfo.config(text="" + str (player_info[5]))
            seninfo.config(text="" + str (player_info[6]))
            scopedinfo.config(text="" +str (player_info[9]))
            adsinfo.config(text="" + str (player_info[10]))
            
            edpiproinfo.config(text="" + str (player_info[8]))
            hzinfo.config(text="" + str (player_info[12]))
            winseninfo.config(text="" + str (player_info[10]))
            ripinfo.config(text="" + player_info[11])
            crosshairinfo.insert(0, player_info[13])
        else:
            messagebox.showwarning("Admin", "Not Found ID in DATABASE")
root = main()

# เมื่อ root window ถูกสร้างขึ้นเรียบร้อยแล้วจึงทำคำสั่งอื่นๆ
connect_database()
username_var = StringVar()
password_var = StringVar()
adminusername_var = StringVar()
adminpassword_var = StringVar()
playersearch_entry= StringVar()
crosshairinfo= StringVar()
user_emails = ['user1@example.com', 'user2@example.com']
img1 = PhotoImage(file='image/boy.png').subsample(3,3)
img3 = PhotoImage(file='image/boy1.png').subsample(3,3)
img2 = PhotoImage(file='image/wa.png').subsample(8, 8)
img4 = PhotoImage(file='image/girl.png')
img5 = PhotoImage(file='image/jett.png').subsample(2, 2)
img6 = PhotoImage(file='image/logo.png').subsample(9, 9)
img7 = PhotoImage(file='image/valo.png').subsample(3, 3)
fr1=create_main_frame()

# เรียก main loop เพื่อแสดงหน้าต่าง GUI
root.mainloop()