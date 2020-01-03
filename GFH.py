import sys
import requests
import argparse
import colorama

from re import search
from termcolor import colored
from frontend.strings import art1, art2, email, splitter

colorama.init()
print (colored(art1, 'green'), colored(art2+email+splitter, 'cyan'))

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='target endpoint{url/api}', dest='url')

args= parser.parse_args()
target = args.url
print(colored("Scanning Web-Headers for: ", 'green')+target)

r = requests.get(target)

headRaw = r.headers
print(headRaw)
