from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

urlList = []
privacyList = []
privacyKeyword = ["개인정보처리방침", "Privacy", "Privacy Policy", "개인정보 보호", "Footer__privacy"]

urlList.append('https://lovepik.com/')
urlList.append('https://zoom.us')
urlList.append('https://www.miricanvas.com/')
urlList.append('https://www.inflearn.com')
urlList.append('https://www.kaggle.com')
list_len = len(urlList)

for i in range(list_len):
    url = urlList[i]
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    bsObject = BeautifulSoup(page, 'html.parser')

    for link in bsObject.find_all('a'):
        if link.text.strip() in privacyKeyword:
            print(link.text.strip())
            print('privacy link : ', link, '\n')
            privacy_link = link.get('href')
            privacyList.append(privacy_link)
            # privacy_req = Request(privacy_link, headers={'User-Agent': 'Mozila/5.0'})
            # policy_html = urlopen(privacy_req).read()
            # privacy_bsObject = BeautifulSoup(policy_html, 'html.parser')

print(privacyList)