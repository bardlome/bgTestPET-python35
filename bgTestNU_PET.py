# -*- coding: utf-8 -*-
#import statistics #downloaded
#import pydicom #downloaded
"""
try:
	import matplotlib
	matplotlib.use("TkAgg")
except ImportError:
	pass
"""
import matplotlib
matplotlib.use('WebAgg')#"Agg"    JRSAGDSASA A  PR#!$@%!%!@V  TEN MATL}PLOTLIB DAWAL BUGA PRZEZ 2 MIESIACE!!!!!!!!!!!!!!!!!!!
import matplotlib.pyplot as plt #downloaded
"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
"""
#import pylab #niedownloaded
import numpy as np #alreadydow
#import scipy #downloaded
#import math #from math import pow #
#from time import sleep #niedownloaded
#from sys import exit #niedownloaded
#from os import listdir #niedownloaded
from tkinter import filedialog as tkFileDialog #ponizej?
# sudo apt-get install python-tk
from tkinter import messagebox as tkMessageBox
import tkinter as tk
#from os import system #niedownloaded
#from tex import latex2pdf
#from tex import convert as texconvert
#import datetime
#import __future__
#import latex
#import matplotlib
#matplotlib.use('Agg')
#plt.ion()
#from time import sleep as uspij
#import multiprocessing
#import threading


#import bgTestNU_PET hehe
import tworzenieguzikow









class Apka(tk.Frame):
    #global chcemymulti
    chcemymulti=1 #2=nie chcemy multiprocessingu, 1=chcemy
    #global pixyniejednorodne3
    pixyniejednorodne3=2 #2=siatka ma rowne odleglosci-mniej niz cm

    sciezka=""
    probnanazwa=""
    listafolderu2=[]
    sciezkapoprzednia=""
    wynik1="Not performed"
    wynik2="Not performed"
    wynik3="Not performed"
    SLAJSY3=np.zeros((81,81,1))#shape=(81,81,6) #do poprawyyyy!
    #X=np.array(shape=(81,81,6)
    ax3=plt.plot()
    SLAJSY2=np.zeros((81,81,1))#shape=(81,81,6)
    ax2=plt.plot()

			

	
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        tworzenieguzikow.tworzenieguzikow(self)
        #self.geometry("500x300+500+200")
        #self.make_topmost()
	#root.protocol("WM_DELETE_WINDOW", self.quit)

        root.title("BGPetTest")
        root.resizable(width=False, height=False)
        #root.geometry("500x200")

        w = tk.Label(root, text="wersja 0.01")
        w.pack()



"""
def powrotzmartwych(listaa,aleluja):

	if __name__ == '__main__':
		root = tk.Tk()


		app = Apka(master=root)
		app.mainloop()
"""
"""
root.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
def doSomething():
    # check if saving
    # if not:
    root.destroy()
"""
if __name__ == '__main__':
	root = tk.Tk()


	app = Apka(master=root)
	app.mainloop()

"""
#freeze all az nie zamkne:
tkszukanie=tk.Toplevel()
root.wait_window(tkszukanie)
"""
