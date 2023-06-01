import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.253.128/restconf/data/ietf-interfaces:interfaces"
headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }
basicauth = ("cisco", "cisco123!")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)
response_json = resp.json()
print(json.dumps(response_json, indent=4))

import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.253.128/restconf/data/ietfinterfaces:interfaces/interface=Loopback2"
headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }
basicauth = ("cisco", "cisco123!")
yangConfig = {
 "ietf-interfaces:interface": {
 "name": "Loopback2",
 "description": "My second RESTCONF loopback",
 "type": "iana-if-type:softwareLoopback",
 "enabled": True,
 "ietf-ip:ipv4": {
 "address": [
 {
 "ip": "10.1.1.100",
 "netmask": "255.255.255.0"
 }
 ]
 },
 "ietf-ip:ipv6": {}
 }
}
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth,
headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
 print("STATUS OK: {}".format(resp.status_code))
else:
 print('Error. Status Code: {} \nError message:
{}'.format(resp.status_code,resp.json()))
#end of file
