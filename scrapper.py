import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import time
from bs4 import BeautifulSoup
import sys

if sys.version_info[0] < 3:
    print("Must be using Python 3")
    sys.exit()

url = input("URL : ")
BaliseParser = input("Balise a Scrap : ")

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser") 

def __init__Main__():
	simple_get()
	mainLoop()

def simple_get():
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def mainLoop():
	while True:
		try:
			print(soup.findAll(BaliseParser))
		except:
			soup.findAll('html')
		time.sleep(2)

__init__Main__()