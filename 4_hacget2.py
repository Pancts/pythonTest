#修改版获取琉璃神社代码
import urllib.request
import re
import codecs
#-------------------------------------------------------------------------
#使用127.0.0.1:8087代理的代码
proxy_support = urllib.request.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
#-------------------------------------------------------------------------

#读取网页源代码，并获取标题元素
context = urllib.request.urlopen('http://www.hacg.li/wp/anime.html').read().decode('utf8')
h1 = re.findall('<h1 class="entry-title">.*</h1>',context)

#定义变量，保存标题，磁力链hash值
urlMag = []
urlTitle = []

#读取子页面，并获取磁力链hash值
for n in h1:
	urlTitle.append((re.findall('(?<=title=").*(?="\srel)',n))[0]);
	#获取子链接
	urllink = (re.findall('(?<=<h1 class="entry-title"><a href=").*html',n))
	for i in urllink : 
		source = urllib.request.urlopen(i).read().decode('utf8')
		magHash = re.findall('[a-zA-Z0-9]{40}',source)
		urlMag.append(magHash)

#打开json文件，并写入已爬取的数据
file = codecs.open('4_hacget.json','w+','utf-8')
file.write('{\r\n"title":'+ re.sub('\'','"',str(urlTitle)) + ',\r\n"maghash":' + re.sub('\'','"',str(urlMag)) + '\r\n}')
file.close()