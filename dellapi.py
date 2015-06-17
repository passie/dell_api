#! /usr/bin/env python

import urllib2
import json
import sys
from operator import itemgetter 

for arg in sys.argv:
    tag = arg 
url = 'https://sandbox.apidp.dell.com/support/assetinfo/v4/getassetwarranty/'  

dell_url = url+tag

txdata = None

txheaders = {
	'apikey': 'b209ab6266c7395e041f9630eefe0614'
}

req = urllib2.Request(dell_url, txdata, txheaders)
u = urllib2.urlopen(req)
headers = u.info()
data = u.read()
data = json.loads(data)

try: 
    for assetWarranty in data['AssetWarrantyResponse']:
        AssetEntitlement = sorted(
            assetWarranty['AssetEntitlementData'],
            key=itemgetter('EndDate'),
            reverse=True
        )[0]
	WarrantyDate = (AssetEntitlement['EndDate'])
except:
    sys.stderr.write("Kan nieuwste waarde niet bepalen")

print WarrantyDate



