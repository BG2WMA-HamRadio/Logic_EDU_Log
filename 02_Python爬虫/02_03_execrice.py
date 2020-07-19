# ## 在 www.baidu.com上搜索一个关键字，并将结果（网页）保存到本地
# 导入模块
import urllib.parse
import urllib.request

# 获取网址
base_url = 'https://www.baidu.com/s?'
key_word = input('输入想要搜索的内容：')
wd = {'wd': key_word}
res = urllib.parse.urlencode(wd)
# 拼接 URL
url = base_url + res
# print(url)                              # https://www.baidu.com/s?wd=%E5%90%89%E4%BB%96
# 构建请求头
headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
}
#
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
file_name = base_url + '.html'
with open(file_name, 'w', encoding='utf-8') as fo:
    fo.write(html)
