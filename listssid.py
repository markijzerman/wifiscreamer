#!/usr/bin/env python

import wifi

wifilist = []
prefixes = ('FRITZ', 'UPC', 'TP')

cells = wifi.Cell.all('wlan0')

for cell in cells:
	wifilist.append(cell.ssid)

for word in wifilist[:]:
	if word.startswith(prefixes):
		wifilist.remove(word)

print(wifilist)