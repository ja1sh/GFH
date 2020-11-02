#!/usr/bin/python3
import sys
import requests
import os.path

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from frontend.strings import art1, art2, email, splitter
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print (art1+art2+email+splitter)

#User input
file_path=sys.argv[1]

#Function to run GET requests
def req(url):
    print(url)
    b = requests.get(url, verify=False)
    print("\nScanned: "+str(b.url))
    print("\nStatus Code: "+str(b.status_code))
    head = str(b.headers)
    if "Content-Security-Policy" not in head:
        print("\n Missing CSP Header")
    if "X-XSS-Protection" not in head:
        print("\n Missing X-XSS Header")
    if "Strict-Transport-Security" not in head:
        print("\n Missing HSTS Header")
    if "X-Frame-Options" not in head:
        print("\n Missing X-Frame Header")
    if "X-Content-Type-Options" not in head:
        print("\n Missing X-Content-Type Header")
req(file_path)
