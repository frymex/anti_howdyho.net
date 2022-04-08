import requests

url = input('Ссылка: ')

cookies = {
    'online-cache': '%7B%22id%22%3A%221929540%22%2C%22visit%22%3A1649452468%7D',
    '_ym_d': '1649452469',
    '_ym_uid': '1649452469632012729',
    '_ym_visorc': 'w',
    '_ym_isad': '2',
}

headers = {
    'authority': 'howdyho.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'PHPSESSID=ugtq0nqiec1jqsin94qp1rg354; online-cache=%7B%22id%22%3A%221929540%22%2C%22visit%22%3A1649452468%7D; _ym_d=1649452469; _ym_uid=1649452469632012729; _ym_visorc=w; _ym_isad=2',
    'dnt': '1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}

response = requests.get('https://howdyho.net/cybersecurity/private-hub-hranilishe-dlya-lyubyh-fajlov', headers=headers, cookies=cookies)
if response.ok:
    id = response.text.split('id="download-start"')[1].split(' data-mid="')[1].split('"')[0]
    print('wait . . .')
    d2 = requests.get(f'https://howdyho.net/download/start/{id}', headers=headers, cookies=cookies).url
    print(d2)