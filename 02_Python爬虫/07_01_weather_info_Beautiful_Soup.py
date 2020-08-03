import requests
from bs4 import BeautifulSoup

# 使用Beautifiul Soup获取中国天气网的天气数据
# 本代码并不包含实际功能，所获取的信息极为有限，只作为展示BeautifulSoup模块的练习。


# 获取大区url，获取每个大区的网页源码，并存储到临时文件夹
# 需在当前目录创建一个temp文件夹

def get_html():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
    url_location = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']
    base_url = 'http://www.weather.com.cn/textFC/{}.shtml'
    # 将获取到的源代码保存到temp文件夹中。
    for location in url_location:
        url = base_url.format(location)
        file_name = location + '.shtml'
        with open('temp/'+file_name, 'w', encoding='utf-8') as fo:
            res = requests.get(url, headers=headers).content.decode('utf-8')
            fo.write(res)


# get_html()
# 获取数据
def weather(file_name):

    with open(file_name, 'r', encoding='utf-8') as fo:
        html = fo.read()
    
    #

    # 官方文档建议使用lxml解析器，因为它速度更快。这里使用html5lib的原因是港澳台网页的源代码有问题，title没有结束的</title>
    # 而的html5lib可以自动帮我们补全缺少的标签。
    soup = BeautifulSoup(html, 'html5lib')
    # conMidtab 包含整个地区的所有信息
    conMidtab_tag = soup.find('div', class_="conMidtab")
    # 每一个table包含单个城市的信息
    tables = conMidtab_tag.findAll('table')

    # 对tables 遍历，从中提取城市以及天气信息。
    for table in tables:
        # table中的tr代表行政省中的地级市。如果是直辖市则代表区。 前2个tr是表头，这里过滤掉
        trs = table.findAll('tr')[2:]
        # 引入新方法enumerate(),这个函数返回两个值，第一个是索引，第二个是索引所对应的值。
        for index, tr in enumerate(trs):
            # 查找tr中对应的td，每个td都代表城市的一个属性，比如城市名，天气情况，风向风力，最低温度等
            # enumerate()函数生成两个对象，前边一个是当前元素的索引，后边一个是当前元素。
            tds = tr.findAll('td')
            city_td = tds[0]
            # 省级行政区的省会名在tds[1],这里通过索引判断，如果是第一个tr, 则选择tds[1]输出城市名（tds[0]是省名）
            if index == 0:
                city_td = tds[1]
            temp_td = tds[-2]

            city_name = list(city_td.stripped_strings)[0]
            city_temp = list(temp_td.stripped_strings)[0]

            # print('城市：', city_name, '\t', '最低温度：', city_temp)
            with open('temp/weather.txt', 'a+', encoding='utf-8') as fo:
                fo.write('城市：' + city_name + '\t' + '最低温度：' + city_temp + '\n')
                # fo.write()
        with open('temp/weather.txt', 'a+', encoding='utf-8') as fo:
            fo.write('---------------------------------------------------------------\n')
    with open('temp/weather.txt', 'a+', encoding='utf-8') as fo:
        fo.write('---------------------------------------------------------------\n')




def main():
    url_location = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']
    for location in url_location:
        file_name = 'temp/'+location+'.shtml'
        weather(file_name)




if __name__ == '__main__':
    # get_html()
    main()
