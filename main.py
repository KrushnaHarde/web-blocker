import tkinter as tk
from tkinter import messagebox
import sys
import ctypes
import os
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, r"C:\Users\Admin\Downloads\mine.py", None, 1)
    sys.exit()
print("This code has been given the administrator permissions!")

def block():
    website_list = website_entry.get()
    Website = list(website_list.split(","))
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in Website:
            if website.strip() not in content:
                file.write(redirect + " " + website.strip() + "\n")
                messagebox.showinfo("Website Blocker", "Website has been blocked!")
            else:
                messagebox.showinfo("Website Blocker", "Website has already been blocked!")

def unblock():
    website_list = website_entry.get()
    Website = list(website_list.split(","))
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in Website):
                file.write(line)
        file.truncate()
        messagebox.showinfo("Website Blocker", "Website has been unblocked!")

def close_window():
    myroot.destroy()

myroot = tk.Tk()
myroot.title("Website Blocker")
myroot.geometry('650x400')
myroot.maxsize(750,600)
myroot.minsize(650,300)

tk.Label(myroot,text='Website Blocker',font=('bold',45),fg='cyan', bg="gray10").pack()

myroot.configure(bg="gray10")

website_label = tk.Label(myroot, text="Enter URL of the website to be blocked:", bg="gray10", font=("bold, 15"), fg="green1")
website_label.pack()

website_entry = tk.Entry(myroot, width=40)
website_entry.pack()

block_button = tk.Button(myroot, text="Block Website", command=block, font=("bold, 15"), fg="red")
block_button.pack()

unblock_button = tk.Button(myroot, text="Unblock Website", command=unblock, font=("bold, 15"), fg="blue")
unblock_button.pack()

exit_button = tk.Button(myroot, text="Exit", command=close_window, font=("bold, 15"), fg="red")
exit_button.pack()
tk.Label(myroot,text="It is recommended to close the browser when website blocker is running.",font=('bold',15),fg='white', bg="gray10").pack()
tk.Label(myroot,text="You can access the brower once website has been blocked/unblocked.", font=('bold',15),fg='white', bg="gray10").pack()

myroot.mainloop()