import requests
import json
import csv
from time import sleep
import os.path


def get_page(url: str, payload=None, pause=0):
    if payload is None:
        payload = {}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 "
                      "Safari/537.36",
        "Accept": "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8'
    }
    r = requests.get(url=url, headers=headers, params=payload)
    sleep(pause)
    return r


def save2json(data, filename):
    if not os.path.exists("json"):
        os.mkdir('./json')

    with open(f'json/{filename}.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        # json.dump(data, file)


def save2csv(data, filename):
    if not os.path.exists("CSV"):
        os.mkdir('CSV')

    with open(f'CSV/{filename}.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def main():
    # get page

    # url = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C' \
    #       '%22mapBounds%22%3A%7B%22west%22%3A-123.21895465765536%2C%22east%22%3A-114.15523395453036%2C%22' \
    #       'south%22%3A32.00401294910892%2C%22north%22%3A39.23705155265529%7D%2C%22isMapVisible%22%3Atrue%2C%22filter' \
    #       'State%22%3A%7B%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22isAllHomes%22%3A%7B%22' \
    #       'value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D&wants={%22cat1%22:[%22' \
    #       'listResults%22,%22mapResults%22],%22cat2%22:[%22total%22]}'
    # r = get_page(url).json()
    # save2json(r, 'zillow')

    with open('json/zillow.json') as file:
        res = json.load(file)['cat1']['searchResults']['listResults']
        head = ('Address', 'Price', 'Link')
        save2csv(head, 'zillow')
        for item in res:
            address_full = item['address']
            price = str(item['price'])
            link = item['detailUrl']
            # address = str(item['addressStreet'].strip())
            # city = str(item['addressCity'].strip())
            # state = str(item['addressState'].strip())
            # zipcode = str(item['addressZipcode'].strip())
            # status_type = item['hdpData']['homeInfo']['homeStatus'].strip()
            out = (
                address_full,
                price,
                link
            )
            save2csv(out, 'zillow')
            print(out)


if __name__ == '__main__':
    main()
