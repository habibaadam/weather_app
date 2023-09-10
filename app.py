""" Importing library for creating GUI"""
import tkinter as tk

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
window.title("OUR WEATHER")
window.geometry("900x500+300+200")
window.resizable(True, True)


window.mainloop()
