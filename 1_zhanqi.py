import urllib.request as http
import re
import codecs
file_00=codecs.open('test.dpl','w+','utf-8')
file_00.write('DAUMPLAYLIST'+'\n')



content= http.urlopen('http://www.zhanqi.tv/games/Entertainment').read()
xsource= content.decode('UTF-8')

#id= re.match('\d{3,6}_\w{5}(?=_)',xsource)
#print(id)

id= re.findall('\d{3,6}_\w{5}(?=_)',xsource)
title=re.findall('(?<=<span class="name">)[^$<]*',xsource)
n=1
for (i,j)in zip(id,title):
    file_00.write(str(n)+"*file*http://wshdl.load.cdn.zhanqi.tv/zqlive/"+i+'.flv\n')
    file_00.write(str(n)+"*title*"+j+'\n')
    n=n+1
    #print(i,j)

#print(id)
#print(title)

#####新增后续网页

add= http.urlopen('http://www.zhanqi.tv/api/static/game.lives/45/30-2.json').read()
xadd= add.decode('utf-8')
idx= re.findall('(?<=videoId":")[^"]*',xadd)
xtitle=re.findall('(?<=title":")[^"]*',xadd)
for (i,j)in zip(idx,xtitle):
    file_00.write(str(n)+"*file*http://wshdl.load.cdn.zhanqi.tv/zqlive/"+i+'.flv\n')
    file_00.write(str(n)+"*title*"+j+'\n')
    n=n+1

add= http.urlopen('http://www.zhanqi.tv/api/static/game.lives/45/30-3.json').read()
xadd= add.decode('utf-8')

###重复代码
idx= re.findall('(?<=videoId":")[^"]*',xadd)
xtitle=re.findall('(?<=title":")[^"]*',xadd)
for (i,j)in zip(idx,xtitle):
    file_00.write(str(n)+"*file*http://wshdl.load.cdn.zhanqi.tv/zqlive/"+i+'.flv\n')
    file_00.write(str(n)+"*title*"+j+'\n')
    n=n+1



def format(xadd):
    idx= re.findall('(?<=videoId":")[^"]*',xadd)
    xtitle=re.findall('(?<=title":")[^"]*',xadd)
    for (i,j)in zip(idx,xtitle):
        file_00.write(str(n)+"*file*http://wshdl.load.cdn.zhanqi.tv/zqlive/"+i+'.flv\n')
        file_00.write(str(n)+"*title*"+j+'\n')
        n=n+1



file_00.close()
print('写入完成')
