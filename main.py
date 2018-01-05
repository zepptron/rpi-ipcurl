#!/usr/bin/env python
"""Namecheap updater."""

from json import load
import urllib2
import time
import os
import datetime

ip = 0
my_ip = load(urllib2.urlopen('https://api.ipify.org/?format=json'))['ip']

while True:
    if ip == my_ip:
        time.sleep(300)
        ip = load(urllib2.urlopen('https://api.ipify.org/?format=json'))['ip']
    else:
        url_at = "http://dynamicdns.park-your-domain.com/update?host=%s&domain=%s&password=%s&ip=%s" % (os.environ["host"], os.environ["domain"], os.environ["pass"], my_ip)
        url_wc = "http://dynamicdns.park-your-domain.com/update?host=%s&domain=%s&password=%s&ip=%s" % (os.environ["host2"], os.environ["domain"], os.environ["pass"], my_ip)
        urllib2.urlopen(url_at).read()
        urllib2.urlopen(url_wc).read()
        ip = load(urllib2.urlopen('https://api.ipify.org/?format=json'))['ip']
        my_ip = load(urllib2.urlopen('https://api.ipify.org/?format=json'))['ip']
        ti = time.time()
        ts = datetime.datetime.fromtimestamp(ti).strftime('%d-%m-%Y %H:%M:%S')
        print "%s IP changed to %s" % (ts, my_ip)
