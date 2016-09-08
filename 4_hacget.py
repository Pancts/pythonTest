import urllib.request
import re
import codecs

# proxy_handler = urllib.request.ProxyHandler({'http': '127.0.0.1:8087'})
# opener = urllib.request.build_opener(proxy_handler)
# f = opener.open('https://www.google.com/')
# a = f.read()
# print(a)

#! /usr/bin/env python3

#-------------------------------------------------------------------------
#使用127.0.0.1:8087代理的代码
proxy_support = urllib.request.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
#-------------------------------------------------------------------------


#读取json文件
file = codecs.open('4_hacget.json','w+','utf-8')
file.write('{\r\n')

'''
a = urllib.request.urlopen("http://www.hacg.li/wp/23806.html").read().decode("utf8")  #读取了琉璃神社的某个网页内容
#开始使用正则来匹配
magHash = re.findall('[a-zA-Z0-9]{40}',a)
print(magHash)
#print(a)

'''

context = urllib.request.urlopen('http://www.hacg.li/wp/anime.html').read().decode('utf8')
h1 = re.findall('<h1 class="entry-title">.*</h1>',context)

#定义一些变量

#urllink = []
#urlTitle = []
count = 1
for n in h1:
	#urllink = re.findall('(?<=<h1 class="entry-title"><a href=").*html',n)
	

	#urllink.append(re.findall('(?<=<h1 class="entry-title"><a href=").*html',n))


	#urlTitle = re.findall('(?<='+urllink[0]+'" title=").{15}',n)
	#urlTitle = re.findall('\s\[.+?[\]]?\s',n)
	
	#urlTitle[i] = re.findall('(?<=title=").*(?="\srel)',n)
	
	#urlTitle.append((re.findall('(?<=title=").*(?="\srel)',n))[0])
	file.write('"title'+str(count)+'":"'+(re.findall('(?<=title=").*(?="\srel)',n))[0]+'",\r\n')
	file.write('"maghash'+str(count)+'":[')
	count = count + 1

	urllink = (re.findall('(?<=<h1 class="entry-title"><a href=").*html',n))
	for i in urllink : 
		source = urllib.request.urlopen(i).read().decode('utf8')
		magHash = re.findall('[a-zA-Z0-9]{40}',source)

		for index in range(len(magHash)) : 
			#file.write('"maghash":"'+j+'"}\r\n')
			file.write('"'+magHash[index]+'"')
			if(index<len(magHash)-1):
				file.write(',')
		file.write(']')

	if(n!=h1[len(h1)-1]):
		file.write(',\r\n')	
	

	#file.write(re.findall('(?<=<h1 class="entry-title"><a href=").*html',n)[0]+'}')

	#print(urlTitle)
	#print('%s\n'%n)
	#print(urlTitle)
file.write('\r\n}')
file.close()

'''
for i in urllink :
	source = urllib.request.urlopen(i).read().decode('utf8')
	
	magHash = re.findall('[a-zA-Z0-9]{40}',source)
	for j in magHash :
		print('magnet:?xt=urn:btih:%s'%j)
	#print('magnet:?xt=urn:btih:'+magHash)
'''

'''
------------------添加magnet:?xt=urn:btih:---------------
k = 0
for i in urllink :
	print('%s\n'%urlTitle[k])
	k = k+1

	for j in i:
		source = urllib.request.urlopen(j).read().decode('utf8')
		magHash = re.findall('[a-zA-Z0-9]{40}',source)	
	
	for m in magHash :
		print('magnet:?xt=urn:btih:%s\n'%m)
'''