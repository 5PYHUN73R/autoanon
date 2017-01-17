#!/usr/bin/python2

import subprocess
import time
import sys



def menu():
    while True:
        print '\r\n\r\n'
        subprocess.call(['figlet', '-cf', 'shadow', 'AutoAnon'])
        print """      
              ---------------------------------------------------\r\n
                [1] Show your current IP info
	       [1p] Show your current IP info through Tor
                [2] Show your available connections.
	        [3] Activate VPN
	        [4] Activate Tor
	        [5] Activate VPN + Tor
	        [6] Deactivate VPN
                [7] Check ipleak.net in FireFox
	       [7p] Check ipleak.net in Firefox through Tor
	        [8] Let Nmap scan your system
               [8n] Let Nmap scan your network
	        [9] Check your connection speed
               [9p] Check your Tor connection speed
               [10] Anonymously search The Pirate Bay
               [11] Edit your torrc file
               [12] Edit proxychains.conf
               [13[ View the Hidden Wiki in Elinks
	       [14] Reboot
	        [0] Exit
            """

        op = raw_input('Pick an option:')
        if op == '1':
            print 'Getting your IP info...'
            time.sleep(3)
            subprocess.call(['curl', 'ipinfo.io'])
            con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '1p':
            print 'Getting your Tor IP...'
            time.sleep(3)
            ip = subprocess.call(['proxychains', 'curl', 'ifconfig.io'])
            #subprocess.call(['curl', 'ipinfo.io/%s' % ip])
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '2':
            print 'Listing available connections...'
	    time.sleep(3)
            subprocess.call(['nmcli', 'con'])
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '3':
	    subprocess.call(['nmcli', 'con'])
	    v = raw_input('Choose a server: ')
            print 'Activating VPN...'
            time.sleep(2)
            subprocess.call(['nmcli', 'con', 'up', '%s' % v])
	    subprocess.call(['curl', 'ipinfo.io'])
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '4':
            print 'Activating Tor...'
            subprocess.call(['tor'])
	    time.sleep(5)
	    subprocess.call(['proxychains', 'curl', 'ipinfo.io'])
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '5':
	    print 'Activating VPN + Tor...'
	    time.sleep(3)
            subprocess.call(['nmcli', 'con'])
            v = raw_input("Choose a server:")
            subprocess.call(['nmcli', 'con', 'up', '%s' % v])
            time.sleep(3)
	    print 'Establishing Tor connection...'
            subprocess.call(['tor'])
            print '\n'
            time.sleep(3)
	    print 'Your VPN IP info is:'
            subprocess.call(['curl', 'ipinfo.io'])
	    print '\r\n'
	    print 'Your Tor IP info is:'
            subprocess.call(['proxychains', 'curl', 'ipinfo.io' ])
            time.sleep(5)
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '6':
	    subprocess.call(['nmcli', 'con'])
	    v = raw_input('Which server: ')
            print 'Deactivating VPN...'
            time.sleep(2)
            subprocess.call(['nmcli', 'con', 'down', '%s' % v])
            subprocess.call(['curl', 'ipinfo.io'])
	    time.sleep(3)
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '7':
            print 'Opening ipleak.net...'
            subprocess.call(['firefox', 'ipleak.net'])
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '7p':
            print 'Opening ipleak.net...'
            subprocess.call(['proxychains', 'firefox', 'ipleak.net'])
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '8':
            print 'Scanning for open ports....'
	    subprocess.call(['nmap', '-v', '-A', '-p-', '-oX', 'atnmapscan.xml', '127.0.0.1'])
            subprocess.call(['xsltproc', '-o', 'atnmapscan.html', 'atnmapscan.xml'])
            subprocess.call(['surf', '-F', 'atnmapscan.html'])
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '8n':
            print 'Scanning your local network...'
            subprocess.call(['nmap', '-v', '-T4', '-oX', 'atnmaplan.xml', '192.168.0.1/24'])
            subprocess.call(['xsltproc', '-o', 'atnmaplan.html', 'atnmaplan.xml'])
            subprocess.call(['surf', '-F', 'atnmaplan.html'])
            con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '9':
            print 'Checking connection speed....'
	    subprocess.call(['speedtest'])
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '9p':
            print 'Checking Tor connection speed....'
            subprocess.call(['proxychains', 'speedtest'])
	    con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '10':
            query = raw_input("What would you like to search: ")
            print "Searching TPB for %s..." % query
            subprocess.call(['proxychains', 'pirate-get', '%s' % query])
            con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '11':
            print 'Opening torrc...'
            subprocess.call(['sudo', 'nano', '/etc/tor/torrc'])
            con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
	elif op == '12':
            print 'Opening proxychains.conf...'
            subprocess.call(['sudo', 'nano', '/etc/proxychains.conf'])
            con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '13':
            print 'Connecting to the DarkNet...'
            time.sleep(3)
            subprocess.call(['proxychains', 'elinks', 'http://jh32yv5zgayyyts3.onion/'])
            con = raw_input('Continue?(y or n): ')
            if con == 'y':
                continue
            elif con == 'n':
                sys.exit(0)
        elif op == '14':
	    print 'Rebooting....'
	    subprocess.call(['reboot'])
        elif op == '0':
	    sys.exit(0)
        else:
            print 'Please select an option:'
        
        

    
if __name__ == '__main__':
    menu()


