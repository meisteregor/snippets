"""
This script is for testing zabbix version
by version of the docs on the logon page
"""

import urllib2
import re
from bs4 import BeautifulSoup

zab_page='http://by0-zabbix.iv/zabbix.php?action=dashboard.view'
page=urllib2.urlopen(zab_page)
soup = BeautifulSoup(page, 'html.parser')
for link in soup.findAll('a', attrs={'href': re.compile("documentation")}):
    version=link.get('href')

parts=re.split('/', version)

a=''.join (parts[4:5])
print "zabbix version is",a
