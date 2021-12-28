import requests
import json

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
    url = 'http://113.106.199.150:9086/web_homepage/houseList'

    res = requests.get(url,headers=headers)
    target = json.loads(res.text)

    origin_houses_data = target['rows']
    houses_data = {each['PROJECT']:each['ADDRESS'] for each in origin_houses_data}

    print(houses_data)

    

if __name__ == '__main__':
    main()