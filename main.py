'''
# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from youtubesearchpython import VideosSearch
# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a function to show the popup message
def show_msg():


    videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)

    print(videosSearch.result())

# Add an optional Label widget
Label(win, text= "ThomasOXY", font= ('Aerial 17 bold')).pack(pady= 30)

# Create a Button to display the message
ttk.Button(win, text= "Najít", command=show_msg).pack(pady= 20)
win.mainloop()
'''
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from youtubesearchpython import VideosSearch
import json
 
 
window = tk.Tk()
 
window.title("OXY YOUTUBE SEARCH")
window.minsize(60,40)
 
def result():
    label.configure(text= 'Hledám videa s názvem:' + name.get())
    videosSearch = VideosSearch(name.get(), limit = 2)

    print(json.dumps(videosSearch.result(), indent=4, sort_keys=True))
 
label = ttk.Label(window, text = "Co chcete vyhledat?")
label.grid(column = 0, row = 0)
 
 
 
 
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)
 
 
button = ttk.Button(window, text = "Click Me", command = result)
button.grid(column= 0, row = 2)
 
window.mainloop()