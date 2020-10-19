'''
@author : Krypton Byte
@Masih Belum Selesai
'''
import tkinter as tk
from tkinter import *
from zipfile import ZipFile
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter.ttk import Progressbar
def progress():
    zi=ZipFile(fileZip)
    li=len(open(wordlis,"rb").read().splitlines())
    root = tk.Tk()
    root.geometry("300x300")
    pr=Progressbar(root, orient=HORIZONTAL, length=1000, mode="determinate")
    pr.pack(pady=li)
    root.mainloop()
    for i in enumerate(open(wordlis,"rb").read().splitlines()):
        try:
            zi.extractall(pwd=i[1])
            print("sukses")
            break
        except:
            print("gagal")
        percent=100/(li/i[0])
        root.update_idletasks()
        pr["value"] = i[1]

def zipFile():
    global fileZip
    fileZip = filedialog.askopenfilename(initialdir="/home", title="File Manager", filetypes=(("Zip","*.zip"),("Files","*.*")))
    print(fileZip)
def wordlist():
    global wordlis
    wordlis = filedialog.askopenfilename(initialdir="/home", title="File Manager", filetypes=(("Plain Text","*.txt"),("Files","*.*")))
    print(wordlis)
def main():
    win=tk.Tk()
    lbl=tk.Label(win, text="ZipFile : ")
    lbl.grid(column=0, row=0)
    btn=tk.Button(win, text="Open", command=zipFile)
    btn.grid(column=1, row=0)
    lbl=tk.Label(win, text="Wordlist")
    lbl.grid(column=0, row=1)
    btn=tk.Button(win, text="Open", command=wordlist)
    btn.grid(column=1, row=1)
    btn=tk.Button(win, text="Brute", command=progress)
    btn.grid(column=0, row=2)
    win.mainloop()
main()