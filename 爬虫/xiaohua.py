import urllib.request as r
import re

ys = int(input('请输入需要获取图片的页数：')) - 1
print('开始爬取！')

url = 'http://www.xiaohuar.com/list-1-%s.html'%ys
url1 = 'http://www.xiaohuar.com'

wy = r.urlopen(url)
ym = wy.read().decode('gb18030')

bq = re.findall(r'/p-1-.+?html',ym)
temp = []
[temp.append(i) for i in bq if not i in temp]
#print(temp)

for ur in temp:
    bqwy = r.urlopen(url1+ur)
    bqym = ((bqwy.read().decode('gb18030')).split('<div class="hot_tag">推 广 链 接</div>'))[0]
    tp = re.findall(r'src="(/d/file/20.+?\.png|/d/file/20.+?\.jpg)"',bqym)
    xh = 0
    #print(tp)

    for i in tp:
        url2 = url1+i
        tpwy = r.urlopen(url2)        
        tpym = tpwy.read()
        mz = re.findall(r'<td>(.+?)</td>',bqym)
        xh += 1
        sx = str(xh)
        mzmz = mz[0] + sx
        with open('%s.jpg'%mzmz,'wb') as t:
            t.write(tpym)

print('爬取完成！')
