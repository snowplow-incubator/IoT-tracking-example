from tkinter import messagebox
import snowplow_tracker
from snowplow_tracker import Tracker, Emitter
import tkinter as tk
import sys
from tkinter import * 
import webbrowser

# use docker run -p 9090:9090 snowplow/snowplow-micro:1.3.1

e = Emitter('localhost:9090') #some endpoint
t = Tracker( e,
            app_id="Bryan's App")

def onClosing():
    if messagebox.askyesno('Quit', 'Would you like to close the menu?')==1:
        root.destroy()
        sys.exit()

def action1():
    print('google')
    t.track_page_view('www.google.com')
    webbrowser.open('https://www.google.com',new=1)

def action2():
    print('snowplow')
    t.track_page_view('www.snowplow.com')
    webbrowser.open('https://www.snowplowanalytics.com',new=1)

def action3(url):
    url = 'https://'+url
    print('other')
    t.track_page_view(url)
    webbrowser.open(url,new=1)

root = Tk()
root.title('website loader')
root.geometry('600x600')

title_label = Label(root, text = "Welcome to Bryan's webiste loader")
title_label.config(font=('Courier', 25))
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

google_label = Label(root, text = 'Google')
google_label.grid(row=1, column=0, padx=10, pady=10)
google_button = Button(root, text = 'Open Google!', command=action1)
google_button.grid(row=1, column=1, padx=10, pady=10)

snpw_label = Label(root, text = 'Snowplow')
snpw_label.grid(row=2, column=0, padx=10, pady=10)
snpw_button = Button(root, text = 'Open Snowplow!', command=action2)
snpw_button.grid(row=2, column=1, padx=10, pady=10)

others_label = Label(root, text = 'Others?')
others_label.grid(row=3, column=0, padx=10, pady=10)
others_entry = Entry(root, text = 'Enter your link...')
others_entry.grid(row=3, column=1, padx=10, pady=10)
others_button = Button(root, text='Open your link!', command = lambda:action3(others_entry.get()))
others_button.grid(row=3, column=2, padx=10, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

root.protocol('WM_DELETE_WINDOW', onClosing)

root.mainloop()