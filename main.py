#!/usr/bin/env python
"""Namecheap updater."""

from json import load
import urllib2
import time
import os
import datetime

# default "ip", will be changed
ip = 0
# ip service provider :)
api = "https://api.ipify.org/?format=json"
nc = "http://dynamicdns.park-your-domain.com"
my_ip = load(urllib2.urlopen(api))['ip']

while True:
    if ip == my_ip:
        time.sleep(600)  # sleep for n seconds before checking again
        ip = load(urllib2.urlopen(api))['ip']
    else:
        ip = load(urllib2.urlopen(api))['ip']
        my_ip = load(urllib2.urlopen(api))['ip']
        ti = time.time()
        ts = datetime.datetime.fromtimestamp(ti).strftime('%d-%m-%Y %H:%M:%S')
        print "%s IP changed to %s" % (ts, my_ip)   # timestamp + infolog

    url_at = "%s/update?host=%s&domain=%s&password=%s&ip=%s" % (
        nc, os.environ["host"], os.environ["domain"], os.environ["pw"], my_ip)
    url_wc = "%s/update?host=%s&domain=%s&password=%s&ip=%s" % (
        nc, os.environ["host2"], os.environ["domain"], os.environ["pw"], my_ip)
    urllib2.urlopen(url_at).read()  # update namecheap no.1
    urllib2.urlopen(url_wc).read()  # update namecheap no.2
