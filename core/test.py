import requests
from bs4 import BeautifulSoup

import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

url1="http://www.xvideos.com/video49114159/i_love_my_stepsister_-_she_loves_sex_in_the_family"
url2="https://www.baidu.com"
response = requests.get("https://www.baidu.com",verify=False)
print(response.text)