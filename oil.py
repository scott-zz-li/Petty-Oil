from bs4 import BeautifulSoup
import requests

print('歡迎來到小資計算油價!\n')
url = r'https://new.cpc.com.tw/Home/'

print('下載資料中...')
r = requests.get(url)
content = r.content
print('下載完畢!')
soup = BeautifulSoup(content, 'html.parser')

data = soup.find('ul', {'class': 'today_price_ct'})

oil92 = data.find_all('b')[1].get_text()
oil95 = data.find_all('b')[3].get_text()
oil98 = data.find_all('b')[5].get_text()

print('\n今日 92無鉛 油價: ', oil92, ' 元/公升')
print('今日 95無鉛 油價: ', oil95, ' 元/公升')
print('今日 98無鉛 油價: ', oil98, ' 元/公升\n')

oilType = input('92, 95 or 98? ')
currentOil = 0

if oilType == '92':
    currentOil = oil92
elif oilType == '95':
    currentOil = oil95
elif oilType == '98':
    currentOil = oil98
else:
    print('error!')
currentOil = float(currentOil)

liter = float(input('輸入大約公升數->'))
oilself = input('自助加油(y/n)? ')
if oilself.lower() == 'y':
    currentOil -= 0.8
elif oilself.lower() == 'n':
    pass

i = -1.00
while i <= 1.01:
    if 0.4 <= round(currentOil * (liter + i), 2) - round(currentOil * (liter + i)) <= 0.44:
        print('目前油價-> {:.1f} 元/公升\t公升數-> {:.2f} 公升\t價錢-> {:.3f} 元'.format(
            round(currentOil, 2), round(liter + i, 2), round(currentOil * (liter + i), 3)))
    i += 0.01
