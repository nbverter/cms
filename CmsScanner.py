import colorama
import os
import random
import requests
import sys
import time
from multiprocessing import Pool
from colorama import *
colorama.init()


CLEAR_SCREEN = "\033[2J"
RED = "\033[31m"   # mode 31 = red forground
RESET = "\033[0m"  # mode 0  = reset
BLUE  = "\033[34m"
YELLOW = "\033[1;33m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD    = "\033[m"
REVERSE = "\033[m"
WHITE = "\033[1;37m"

xlogo = """
\033[34m
 $$$$$$\  $$\      $$\  $$$$$$\         $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
$$  __$$\ $$$\    $$$ |$$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |
$$ /  \__|$$$$\  $$$$ |$$ /  \__|      $$ /  \__|$$ /  \__|$$ /  $$ |$$$$\ $$ |
$$ |      $$\$$\$$ $$ |\$$$$$$\        \$$$$$$\  $$ |      $$$$$$$$ |$$ $$\$$ |
$$ |      $$ \$$$  $$ | \____$$\        \____$$\ $$ |      $$  __$$ |$$ \$$$$ |
$$ |  $$\ $$ |\$  /$$ |$$\   $$ |      $$\   $$ |$$ |  $$\ $$ |  $$ |$$ |\$$$ |
\$$$$$$  |$$ | \_/ $$ |\$$$$$$  |      \$$$$$$  |\$$$$$$  |$$ |  $$ |$$ | \$$ |
 \______/ \__|     \__| \______/        \______/  \______/ \__|  \__|\__|  \__|
 
                                \033[31mT.me/spamworldpro\033[31m
                                            
"""

if not os.path.exists("Cms"):
    os.mkdir("Cms", 0755)

print(xlogo)


def cms(url):
    try:
        url = url.replace('\n', '').replace('\r', '')
        if url.startswith('http://'):
            url = url.replace('http://', '')
        elif url.startswith("https://"):
            url = url.replace('https://', '')
        else:
            pass

        r = requests.get('http://'+url,timeout=10)
        p = requests.get('http://'+url,timeout=5, allow_redirects = False)
        
        
        # 1. CMS WORDPRESS
        if "/wp-login.php" in r.text or "/wp-admin" in r.text or "/wp-config.php" in r.text:
            print "[+] Wordpress CMS http://"+url + GREEN + '\n'
            open("Cms/wordpress.txt", "a").write('http://'+url + '\n')
        elif "/license.txt" in p.text:
            print "[+] Wordpress CMS http://"+url + GREEN + '\n'
            open("Cms/wordpress", "a").write('http://'+url + '\n')
            
        # 2. CMS LARAVEL
        elif "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php" in r.text:
            print  "[+] Laravel CMS http://"+url + CYAN + '\n'
            open("Cms/Laravel.txt", "a").write('http://'+url + '\n')
        elif "/.env'" in p.text:
            print  "[+] Laravel CMS http://"+url + CYAN + '\n'
            open("Cms/Laravel Env.txt", "a").write('http://'+url + '\n')
        elif "/.env'" in r.text:
            print  "[+] Laravel CMS http://"+url + CYAN + '\n'
            open("Cms/Laravel Env.txt", "a").write('http://'+url + '\n')
            
        # 3. CMS OPENCART
        elif "/index.php?route=common/home" in r.text:
            print  "[+] Opencart CMS http://"+url + YELLOW + '\n'
            open("Cms/Opencart.txt", "a").write('http://'+url + '\n')
        elif "/config.php" in r.text:
            print  "[+] Opencart CMS http://"+url + YELLOW + '\n'
            open("Cms/Opencart.txt", "a").write('http://'+url + '\n')
            
        #4. CMS JOOMLA
        elif "/Joomla!" in r.text or "/index.php?option=com_" in r.text or "/administrator/index.php" in r.text or "/administrator/" in r.text or "/administrator/manifests/files/joomla.xml" in r.text or "/<version>(.*?)<\/version>" in r.text or "/language/en-GB/en-GB.xml" in r.text or "<version>(.*?)<\/version>" in r.text:
            print  "[+] JOOMLA CMS http://"+url + BLUE + '\n'
            open("Cms/Joomla.txt", "a").write('http://'+url + '\n')

        #4. CMS Drupal
        elif "/drupal/" in r.text:
            print  "[+] DRUPAL CMS http://"+url + WHITE + '\n'
            open("Cms/Drupal.txt", "a").write('http://'+url + '\n')

        else:
            print '[-]< Cms Not Found >[-] http://'+url + BOLD + '\n'
            open("Cms/Unknown.txt", "a").write('http://'+url + '\n')

    except:	
	    print ('[*x*] DEAD SITE [*x*] http://'+url + RED + '\n')
	    open("Cms/Dead.txt", "a").write('http://'+url + '\n')
            pass


x = sys.argv[1]
lists = open(x, 'r')
make = lists.readlines()
yes = []
i = 0
for i in range(len(make)):
    yes.append(make[i].strip('\n'))
count = 0
try:
    pp = Pool(processes=50)
    pr = pp.map(cms, [site.rstrip() for site in yes])
except:
    pass
