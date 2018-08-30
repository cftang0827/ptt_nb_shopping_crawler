
import requests
from bs4 import BeautifulSoup

# tag = input("請輸入定位元素，class前面加上.，id前面加上# ")
res = requests.get('https://www.ptt.cc/bbs/nb-shopping/index.html')
soup = BeautifulSoup(res.text, "lxml")

search_page = int(input('請問要翻幾頁搜尋: ')) - 1
search_class = '[' + input('請問要找買or賣 (徵/賣)')
search_region = input('請輸入您要找的地點關鍵字: ')

latest_page_number = int(soup.find_all('a', string='‹ 上頁')[0].attrs['href'].split('/')[3].split('.')[0].split('index')[1])


all_div_r_ent = soup.find_all('div', class_='r-ent')
for div in all_div_r_ent:
    div_content = div.find_all('a')
    div_date = div.find('div', class_='date').contents[0]
    for item in div_content:
        item_content = item.contents[0]
        if (search_class in item_content) and (search_region in item_content):
            print(item_content + "    " + div_date)
