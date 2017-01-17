<pre>
___|   _ \\ \   / |   | |   |  \  |___  |___ /   _ \  
 __ \  |   |\   /  |   | |   |   \ |    /   _ \  |   | 
   ) | ___/    |   ___ | |   | |\  |   /     ) | __ <  
____/ _|      _|  _|  _|\___/ _| \_| _/   ____/ _| \_\ 

</pre>


# autoanon
AutoAnon is a python2 script that automates the anonymization process. AutoAnon has been tested on
both Arch and Debian based distributions using Network Manager, so this should work on Ubuntu, Mint 
and Kali. Your VPN servers should also be imported into Network Manager.

![](http://www.enlightenment.org/ss/e-587df0b3e68151.81641784.jpg)

## Dependencies
Install **_figlet_**:
<pre>sudo apt-get install figlet</pre>

Install **_Surf_**:
<pre>sudo apt-get install surf</pre>

Install **_elinks_**
<pre>sudo apt-get install elinks</pre>

Install **_xsltproc_**:
<pre>sudo apt-get install xsltproc</pre>

Install **_SpeedTest_**:
<pre>sudo apt-get install speedtest-cli</pre>

Install **_Nmap_**:
(**NOTE**: Kali Linux 2.0 has nmap installed out of the box. All other distros will need this installed.)
<pre>sudo apt-get install nmap</pre>

## Usage
<pre>cd autoanon</pre>
<pre>sudo chmod +x autoanon.py</pre>
<pre>./autoanon.py</pre>

### Activating your VPN
[![autoanon](https://asciinema.org/a/4ccd1v7qjh16mqqg2ubmytcw5.png)](https://asciinema.org/a/4ccd1v7qjh16mqqg2ubmytcw5)

### Checking Your VPN Connection Speed
[![autoanon](https://asciinema.org/a/eq8cx6x7wm4imncti0pjdkfpp.png)](https://asciinema.org/a/eq8cx6x7wm4imncti0pjdkfpp)
