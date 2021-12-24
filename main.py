import urllib.request
import json


def save_file(filename, content):
    """提供保存路径和字符串格式的保存内容，函数将以utf-8的编码形式保存文件"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(str(content))


def get_huizhou_houses_address():
    response = urllib.request.urlopen('http://113.106.199.150:9086/web_homepage/houseList')
    content = response.read().decode('utf-8')
    result = json.loads(content)

    # dict_houses包含了所有的房屋信息，有重复项
    dict_houses = result['rows']
    house_data = {}
    # 字典推导式，提取dict_data中的项目名称和地址两列数据，返回新字典。并且去重。
    house_data = {each_house['PROJECT']:each_house['ADDRESS'] for each_house in dict_houses}

    save_file('houses_data.txt', house_data)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    get_huizhou_houses_address()

