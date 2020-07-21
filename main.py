#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import xmlFuncs

#initialize a window for the program
win = tk.Tk()
win.title('Zero Suppression Utility')

#generate and place cal file input dialogue
frame1 = tk.Frame()
frame1.pack(fill=tk.X)
constsfile_label = tk.Label(frame1, text='Calibration File')
constsfile_label.pack()
constsfile_entry = tk.Entry(frame1, width=60)
constsfile_entry.pack()

#generate and place output file directory dialogue
frame2 = tk.Frame()
frame2.pack(fill=tk.X)
outDir_label = tk.Label(frame2, text='Output Directory (include trailing slash)')
outDir_label.pack()
outDir_entry = tk.Entry(frame2, width=60)
outDir_entry.pack()

#generate and place pedestal input
frame3 = tk.Frame()
frame3.pack(fill=tk.X)
ped_label = tk.Label(frame3, text='Pedestal (ADC)')
ped_label.pack()
ped_entry = tk.Entry(frame3, width=10)
ped_entry.pack()

#generate and place input for the GeV Per ADC setting
frame4 = tk.Frame()
frame4.pack(fill=tk.X)
GeVPerADC_label = tk.Label(frame4, text='GeV Per ADC')
GeVPerADC_label.pack()
GeVPerADC_entry = tk.Entry(frame4, width=10)
GeVPerADC_entry.pack()

#generate and place input for the desired GeV ZS threshold
frame5 = tk.Frame()
frame5.pack(fill=tk.X)
GeVZS_label = tk.Label(frame5, text='Desired ZS GeV')
GeVZS_label.pack()
GeVZS_entry = tk.Entry(frame5, width=10)
GeVZS_entry.pack()

#generate and place input for the desired GeV ZS threshold
frame6 = tk.Frame()
frame6.pack(fill=tk.X)
ADCZS_label = tk.Label(frame6, text='Desired ZS ADC')
ADCZS_label.pack()
ADCZS_entry = tk.Entry(frame6, width=10)
ADCZS_entry.pack()

def evaluate():
	#get inputs
	constFile = str(constsfile_entry.get())
	ped = float(ped_entry.get())
	GeVPerADC = float(GeVPerADC_entry.get())
	outDirectory = str(outDir_entry.get())
	
	#fill bin name and cal constants lists from xml file
	bins, consts = xmlFuncs.xmlCalParse(constFile)
	
	#user enters a GeVZS value, calculate ADC thresholds
	if GeVZS_entry.get() and not ADCZS_entry.get():
		GeVZS = float(GeVZS_entry.get())
	
		#make a list of all the zs adc values
		ADC_zs_vals = []
		for i in range(len(consts)):
			ADC_zs_vals.append((GeVZS/(GeVPerADC * consts[i])) + ped)
	
		#write bins and adc values to xml file
		xmlFuncs.xmlADCwrite(bins, ADC_zs_vals, outDirectory)
		
	#user enters an ADC threshold, calculate noise
	elif ADCZS_entry.get() and not GeVZS_entry.get():
		ADCZS = float(ADCZS_entry.get())
		
		GeV_ZS_vals = []
		for i in range(len(consts)):
			GeV_ZS_vals.append((ADCZS - ped) * GeVPerADC * consts[i])
		
		xmlFuncs.xmlGeVwrite(bins, GeV_ZS_vals, outDirectory)
	
	#error, user enters both ADC threshold and GeVZS value
	elif ADCZS_entry.get() and GeVZS_entry.get():
		print('Only enter ADC or GeV value, not both')
		messagebox.showerror('Value Error', 'Only enter ADC or GeV value, not both')
	
	#error, user doesn't enter GeVZS value or ADC threshold
	elif not ADCZS_entry.get() and not GeVZS_entry.get():
		print('Must enter ADC or GeV value')
		messagebox.showerror('Value Error', 'Must enter ADC or GeV value')

#button to run program
compute = tk.Button(win, text='Calculate', command=evaluate)
compute.pack()

#display instructions on opening
messagebox.showinfo('Instructions', 'Enter a calibration constants file, pedestal value, and GeV per ADC.\nEnter ZS GeV to calculate ADC thresholds.\nEnter a ZS ADC to calculate GeV noise.\nLeave output directory blank for program directory.')
		
win.mainloop()
