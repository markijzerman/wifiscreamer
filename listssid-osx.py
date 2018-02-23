from access_points import get_scanner
# from collections import defaultdict
wifi_scanner = get_scanner()


foundNetworks = dict((p["ssid"], p) for p in wifi_scanner.get_access_points())

foundSSIDs = list()
for i in foundNetworks.keys():
    foundSSIDs.append(i)

print(foundSSIDs)