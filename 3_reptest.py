# python的正则表达式要使用re模块
import re
pa = re.compile('\d{5}')# 如果使用r开头，表示里面是原字符串
str = '12345abc45678axxxxd5555'
xx = pa.match(str);
print(type(xx))
