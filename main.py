import urllib.request
import urllib.parse
import json


def save_file(filename, content):
    """提供保存路径和字符串格式的保存内容，函数将以utf-8的编码形式保存文件"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(str(content))


def get_huizhou_houses_address():
    response = urllib.request.urlopen('http://113.106.199.150:9086/web_homepage/houseList')
    content = response.read().decode('utf-8')
    result = json.loads(content)
    house_data = {}
    for each_house in result['rows']:
        if each_house['PROJECT'] not in house_data.keys():
            house_data[each_house['PROJECT']] = each_house['ADDRESS']

    save_file('houses_data.txt', house_data)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    get_huizhou_houses_address()

