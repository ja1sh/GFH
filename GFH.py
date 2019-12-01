import sys
import requests
import argparse
import colorama

from termcolor import colored
from frontend.style import TITLE, ARTBLUE, ARTWARN, ARTGREEN, NOTHOT
from frontend.strings import art1, art2, email, splitter

colorama.init()
print (colored(art1, 'green'), colored(art2+email+splitter, 'cyan'))

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='target endpoint{url/api}', dest='target')


args= parser.parse_args()
print(args.accumulate())
