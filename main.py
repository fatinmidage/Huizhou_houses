import urllib.request
import urllib.parse
import json


def get_huizhou_houses_address():
    data = {
        'advanced_search': '"[{\"filter\":\"and\",\"filed\":\"PRESELL.REGIONCODE\",\"code\":\"like\",\"value\":\"441302\",\"type\":\"undefined\"},{\"filter\":\"and\",\"filed\":\"PRESELL.PROJECT\",\"code\":\"like\",\"value\":\"明昱\",\"type\":\"undefined\"}]"',
        'limit': '200', 'offset': '0', 'order': "desc", 'pageNumber': '1', 'search_filed': "[]",
        'sort': "presell.INDATE", '_token': ""}
    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen('http://113.106.199.150:9086/web_homepage/houseList')
    content = response.read().decode('utf-8')
    result = json.loads(content)
    house_data = {}
    for each_house in result['rows']:
        if each_house['PROJECT'] not in house_data.keys():
            house_data[each_house['PROJECT']] = each_house['ADDRESS']

    with open('houses_data.txt', mode='w', encoding='utf-8') as b:
        b.write(str(house_data))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    get_huizhou_houses_address()
