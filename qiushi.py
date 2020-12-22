import urllib.request
import re

def Python(url):



 headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) "
                      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"
    }
 req = urllib.request.Request(url, headers=headers)
 response = urllib.request.urlopen(req)

 HTML = response.read().decode("utf-8")
# 正则表达式
 pat = r'<div class="author clearfix">(.*?)<span ' \
          r'class="stats-vote"><i class="number">'
 re_joke = re.compile(pat, re.S)
 divslist = re_joke.findall(HTML)

#dic = {}
 for div in divslist:
# 用户名
    re_u = re.compile(r"<h2>(.*?)</h2>", re.S)
    username = re_u.findall(div)
#前面有换行符，【0】直接拿文字
    username = username[0]

# 段子

    re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
    duanzi = re_d.findall(div)
    duanzi = duanzi[0]
    info = (username + "说" + duanzi)
    return info
    url = "https://www.qiushibaike.com/text/page/2/"

    data = Python(url)
   
#print(info)

 # print(len(duanzi))


#封装不了函数
