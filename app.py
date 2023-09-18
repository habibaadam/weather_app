""" Importing library for creating GUI"""
from tkinter import *
import tkinter as tk

""" Import PIL for image handling"""
from PIL import Image, ImageTk 

"""Library for converting address to longitude and latitude"""
from geopy.geocoders import Nominatim

"""Importing module for finding timezone for locations"""
from timezonefinder import TimezoneFinder

"""Importing library for manipulating datetime objects"""
import pytz

"""Importing module for working with dates and times"""
from datetime import datetime

"""Importing  module for making HTTP requests and getting responses"""
import requests

"""Importing module for creating dialogue boxes in GUI"""
from tkinter import ttk, messagebox

"""Setting up the main window for our app"""

window = tk.Tk()
window.configure(bg="black")
window.title("OUR WEATHER")
window.geometry("900x500+300+200")

"""Trying to set background image"""

background_image = Image.open("/Users/macbookair/Desktop/w_m/bbgcool.jpeg")
background_photo = ImageTk.PhotoImage(background_image)

"""Create a label to display the background image"""
background_label = tk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)  # Making the label cover the entire window

window.resizable(True, True)

"""Seach box"""
Box_image=PhotoImage(file="/Users/macbookair/Desktop/w_m/search.png")
ourimage=Label(image=Box_image)
ourimage.place(x=20,y=20)

textfield=tk.Entry(window,justify="center", width=17,font=("poppins",25,"bold"), bg="#FFA500", border=0, fg="white")
textfield.place(x=50,y=40)
textfield.focus()

"""seach icon"""
icon_image=tk.PhotoImage(file="/Users/macbookair/Desktop/w_m/search_icon.png")
our_icon_image=Button(image=icon_image, borderwidth=0, cursor="hand2", bg="#FF8C00")
resized_icon_image = icon_image.subsample(1)
our_icon_image.place(x=400,y=34)

window.mainloop()
