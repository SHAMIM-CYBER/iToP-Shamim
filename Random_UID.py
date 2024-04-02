# -*- coding: utf-8
import os
try:
	import requests
except ImportError:
	print("\n [!] \033[0;91mmodule requests belum terinstall \033[0;97m")
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] \033[0;91mmodule futures belum terinstall\033[0;97m")
	os.system("pip install futures")
	os.system("pkg install figlet")

import os
import sys
import time
import calendar
import requests
import random
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from datetime import date 

def sangar():
        m = ["|","/","-","\\"]
        for b in range(2):
                for t in m:
                        sys.stdout.write("  \r\033[32m"+t)
                        #os.system("rm -rf login.txt")
                        sys.stdout.flush()
                        time.sleep(1)       
  
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		                                              
ct = datetime.now()
n = ct.month
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		self.ips = requests.get("https://anggakurniawan.my.id/myip/").text
		os.system("clear")
		jalan(" ••• please subscribe youtube author :) thank you")
		os.system("xdg-open https://youtube.com/channel/UCMxnS8H31SIU2Q7AwDpdBmw")
		time.sleep(4)
		os.system("clear")
		os.system("figlet HAMII")
		print("\n  ( Programmed By Hamid Meer )") 
		print("\n  ( Facebook : Hamid Meer'hamii )") 
		print("\n  ( WhatsApp +923155912839 )") 
		print(" ( https://github.com/Hamii-King-06 )\n") 
		
		print("         [ No Login Facebook ]")
		print(" -------------------------------------")

		print(" -------------------------------------")
		print("\n [01]. crack random id facebook new")
		print(" [02]. crack random id facebook young")
		print(" [03]. crack random id facebook old")
		print(" [04]. crack random email facebook")
		print(" [05]. report")
		tanya = input("\n [•] choose : ")
		if tanya in ["", " "]:
			Main()
		elif tanya in ["1", "01"]:
			self.fbbaru()
		elif tanya in ["2", "02"]:
			self.fbmuda()
		elif tanya in ["3", "03"]:
			self.fbtua()
		elif tanya in ["4", "04"]:
			self.email()
		elif tanya in ["5", "05"]:	
		    os.system(" xdg-open https://www.facebook.com/H4CK3R.H4M11")
		    time.sleep(3)		    		   
		    Main()
		else:
			Main()
