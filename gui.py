'''
@author : Krypton Byte
'''
import tkinter as tk
from tkinter import *
from zipfile import ZipFile
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from concurrent.futures import ThreadPoolExecutor
def progress():
    zi=ZipFile(fileZip)
    li=len(open(wordlis,"rb").read().splitlines())
    root = tk.Tk()
    root.geometry("300x300")
    pr=Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
    pr.pack(pady=100)
    for i in enumerate(open(wordlis,"rb").read().splitlines()):
        percent=100/(li/(i[0]+1))
        try:
            zi.extractall(pwd=i[1])
            Lab=Label(root, text="Password Ditemukan : %s"%i[1].decode())
            Lab.pack()
            root.update_idletasks()
            break
        except:
            Lab=Label(root, text="Cracking : %s%s  Percobaan: %s"%(round(percent, 1),"%", i[0]))
            Lab.pack()
        pr["value"] = percent
        root.update_idletasks()
        Lab.destroy()
    root.mainloop()

def zipFile():
    global fileZip
    fileZip = filedialog.askopenfilename(initialdir="./", title="File Manager", filetypes=(("Zip","*.zip"),("Files","*.*")))
    print(fileZip)
def wordlist():
    global wordlis
    wordlis = filedialog.askopenfilename(initialdir="./", title="File Manager", filetypes=(("Plain Text","*.txt"),("Files","*.*")))
    print(wordlis)
def main():
    win=tk.Tk()
    lbl=tk.Label(win, text="ZipFile : ")
    lbl.grid(column=0, row=0)
    btn=tk.Button(win, text="Open", command=zipFile)
    btn.grid(column=1, row=0)
    lbl=tk.Label(win, text="Wordlist : ")
    lbl.grid(column=0, row=1)
    btn=tk.Button(win, text="Open", command=wordlist)
    btn.grid(column=1, row=1)
    btn=tk.Button(win, text="Brute", command=progress)
    btn.grid(column=0, row=2)
    win.mainloop()
with ThreadPoolExecutor(max_workers=5) as execu:
    execu.submit(main)