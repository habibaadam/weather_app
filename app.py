""" Importing library for creating GUI"""
from tkinter import *
import tkinter as tk

""" Import PIL for image handling"""
from PIL import Image, ImageTk 

"""Library for converting address to longitude and latitude"""
import geopy
from geopy.geocoders import Nominatim

"""Importing module for finding timezone for locations"""
from timezonefinder import TimezoneFinder

"""Importing library for manipulating datetime objects"""
import pytz

"""Importing module for working with dates and times"""
from datetime import datetime, time

"""Importing  module for making HTTP requests and getting responses"""
import requests

"""Importing module for creating dialogue boxes in GUI"""
from tkinter import ttk, messagebox

"""Setting up the main window for our app"""

window = tk.Tk()
window.title("OUR WEATHER")
window.geometry("900x500+300+200")

"""Trying to set background image"""

#background_image = Image.open("/Users/macbookair/Desktop/w_m/bbgcool.jpeg")
#background_photo = ImageTk.PhotoImage(background_image)

"""Create a label to display the background image"""
#background_label = tk.Label(window, image=background_photo)
#background_label.place(relwidth=1, relheight=1) #Making the label cover the entire window

window.resizable(False, False)


def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    print(result)


"""Seach box"""
Box_image=PhotoImage(file="/Users/macbookair/Desktop/w_m/search.png")
ourimage=Label(image=Box_image)
ourimage.place(x=20,y=20)

textfield=tk.Entry(window,justify="center", width=17,font=("poppins",25,"bold"), bg="#404040", border=0, fg="#ADD8E6")
textfield.place(x=50,y=40)
textfield.focus()

"""seach icon"""
icon_image=tk.PhotoImage(file="/Users/macbookair/Desktop/w_m/search_icon.png")
our_icon_image=Button(image=icon_image, borderwidth=0, cursor="hand2", bg="#323232", command=getWeather)
our_icon_image.place(x=400,y=34)

"""Logo"""
logo_image = PhotoImage(file="/Users/macbookair/Desktop/w_m/Copy of logo.png")
logolabel = Label(image=logo_image)
logolabel.place(x=150, y=100)

"""WeatherInfoBox"""
weather_box=PhotoImage(file="/Users/macbookair/Desktop/w_m/Copy of box.png")
weather_boxlabel = Label(image=weather_box)
weather_boxlabel.pack(padx=5,pady=5,side=BOTTOM)

"""Labelling of contents in weather info"""
windlabel = Label(window, text="WIND", font=("Helvetica",17, "bold"), fg="orange",bg="#41a1da")
windlabel.place(x=120,y=400)

humiditylabel = Label(window, text="HUMIDITY", font=("Helvetica",17, "bold"), fg="orange", bg="#41a1da")
humiditylabel.place(x=250,y=400)

descriptionlabel = Label(window, text="DESCRIPTION", font=("Helvetica",17, "bold"), fg="orange", bg="#41a1da")
descriptionlabel.place(x=430, y=400)

pressurelabel = Label(window, text="PRESSURE", font=("Helvetica",17, "bold"), fg="orange", bg="#41a1da")
pressurelabel.place(x=650, y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial", 15, "bold"))
c.place(x=400,y=250)

w=Label(text="...", font=("arial", 23, "bold"), bg="#41a1da", fg="orange")
w.place(x=120,y=430)
h=Label(text="...", font=("arial", 23, "bold"), bg="#41a1da", fg="orange")
h.place(x=280,y=430)
d=Label(text="...", font=("arial", 23, "bold"), bg="#41a1da", fg="orange")
d.place(x=450,y=430)
p=Label(text="...", font=("arial", 23, "bold"), bg="#41a1da", fg="orange")
p.place(x=670,y=430)

"""Time"""
timelabel=Label(window, font=("arial",15, "bold"))
timelabel.place(x=30,y=100)
clock=Label(window, font=("Helvetica",20))
clock.place(x=30,y=100)

window.mainloop()
