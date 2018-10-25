#
# 2018-10-25

# import  urllib.request
# keywd="中文"
# #处理中文方法
# keywd=urllib.request.quote(keywd)
# #爬取http代替HTTPS
# url="http://www.baidu.com/s?wd="+keywd
# #封装一个请求
# req=urllib.request.Request(url)
# data=urllib.request.urlopen(req).read()
# fh=open("F:\python\code\h2.html","wb")
# fh.write(data)
# fh.close()

###



##
# import urllib.request
# # import urllib.parse
# # url="http://www.iqianyue.com/mypost"
# # #登录表单
# # mydata=urllib.parse.urlencode(
# #     {
# #         "name":"eco@iqiyuan",
# #         "pass":"123151"
# #     }
# #
# # ).encode("utf-8")
# # req=urllib.request.Request(url,mydata)
# # data=urllib.request.urlopen(req).read()
# # fh=open("F:\python\code\h3.html","wb")
# # fh.write(data)
# # fh.close()
# # #
####


##异常处理
# import urllib.error
# import  urllib.request
# try:
#     urllib.request.urlopen("http://blog.csdn.net")
# except urllib.error.URLError as e:
#     if hasattr(e,"code"):
#         print(e.code)
#     if hasattr(e,"reason"):
#         print(e.reason)



##浏览器伪装
# import urllib.request
# url="https://blog.csdn.net/c406495762/article/details/60137956/"
# headers=("User-Agent","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")
# opener=urllib.request.build_opener()
# opener.add_handler=[headers]
# data=opener.open(url).read()
# fh=open("F:\python\code\h7.html","wb")
# fh.write(data)
# fh.close()
# ###


##爬取新闻

import urllib.request
import  re
import urllib.error

data=urllib.request.urlopen("https://news.sina.com.cn/").read()
data2=data.decode("utf-8","ignore")
pat='href="(https://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data2)
for i in range(0,len(allurl)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl=allurl[i]
        file="F:\python\code\sin"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,file)
        print("-----------成功-------------")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

















