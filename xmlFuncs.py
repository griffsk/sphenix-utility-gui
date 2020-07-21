#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from tkinter import messagebox

def xmlCalParse(xmlFileName):
	#run in a try loop in case invalid xml file given->error
	try:
		root = ET.parse(str(xmlFileName)).getroot()
	
		#get eta phi name for each bin, all parameters under tag dparams, all names are type string
		bins = []
		for i in root.findall('XmlKey/Object/PdbParameterMap/dparams/string'):
			name = i.get('v')
			bins.append(name)

		#get constant for each bin, all parameters under tag dparams, all conts are type Double_t
		consts = []	
		for i in root.findall('XmlKey/Object/PdbParameterMap/dparams/Double_t'):
			val = i.get('v')
			consts.append(eval(val))
	
	#invalid xml entered
	except:
		messagebox.showerror('Error', 'Invalid Calibration File')
		
	return bins, consts
	
def xmlADCwrite(binNamesList, ADClist, outDir):
	#create and formal xml file
	outFile = open(str(outDir) + 'ADC_ZS_vals.xml', 'w')
	outFile.write('<root>\n')
	outFile.write('  <ADCzsVals>\n')
	
	#write the bin names and values alternating, bin name first, value on next line
	for i in range(len(binNamesList)):
		outFile.write('    <string v=\"' + str(binNamesList[i]) + '\"/>\n')
		outFile.write('    <Double_t v=\"' + str(ADClist[i]) + '\"/>\n')
	
	#finish formatting and close xml	
	outFile.write('  </ADCzsVals>\n')
	outFile.write('</root>\n')
	outFile.close()
	
def xmlGeVwrite(binNamesList, GeVlist, outDir):
	#create and formal xml file
	outFile = open(str(outDir) + 'GeV_ZS_vals.xml', 'w')
	outFile.write('<root>\n')
	outFile.write('  <GeVzsVals>\n')
	
	#write the bin names and values alternating, bin name first, value on next line
	for i in range(len(binNamesList)):
		outFile.write('    <string v=\"' + str(binNamesList[i]) + '\"/>\n')
		outFile.write('    <Double_t v=\"' + str(GeVlist[i]) + '\"/>\n')
	
	#finish formatting and close xml	
	outFile.write('  </GeVzsVals>\n')
	outFile.write('</root>\n')
	outFile.close()
	
