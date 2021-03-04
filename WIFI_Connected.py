import urllib
from urllib.request import urlopen


def Is_Internet():
    try:
        urlopen('https://www.google.com',timeout=1)
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False

if Is_Internet():
    print("Internet is active")
else:
    print("Internet connection failed")
