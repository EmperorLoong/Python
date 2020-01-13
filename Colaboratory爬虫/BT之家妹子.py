#bt之家美女图片
import requests as r
import re
import os

#切换到要保存的目录
path = "/content/drive/My Drive/爬虫妹子图"
os.chdir(path)

#打开网页
def wangye(url):
    ua = {}
    ua['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    fh = r.get(url,headers=ua)
    return fh

#找页数下的图片标签
def yeshubiaoqian(zhuye):
    sr = int(input('输入需要爬取的页数：'))+1 
    bqlb = []
    for i in range(1,sr):
        yeshu = 'forum-index-fid-8-page-%s.htm'%i
        url = zhuye + yeshu
        #print(url)
        nr = wangye(url).text
        #print(nr)
        bq = re.findall(r'<a target="_blank" href="(%s+thread-index-fid-8-tid-\d{5}.htm)".+?</a>'%zhuye,nr)
        #print(bq)
        bqlb += bq
    return bqlb

#找图片链接与名字
def tupian(bq):
    fh = wangye(i).text
    tp = re.findall(r'src="(htt.+?.jpg)"',fh)
    mz = re.findall(r'%s+">(.+?)</a>'%i,fh)
    #print(len(tp))
    return tp,mz

#保存图片
def baocun(tp,mz):
    sz = 0
    print('正在下载：',mz[0])
    print('一共：',len(tp),'张')
    os.mkdir(mz[0])
    os.chdir(mz[0])
    for i in tp:
        #t.sleep(3)
        ym = wangye(i).content
        sz += 1
        tps = mz[0]+str(sz)
        print('正在保存：',tps,i)
        with open('%s.jpg'%tps,'wb') as w:
            w.write(ym)
    os.chdir(path)
        
if __name__ == '__main__':
    zhuye = 'http://www.1btjia.com/'
    bq = yeshubiaoqian(zhuye)
    for i in bq:
        print('正在打开此链接：',i)
        tp,mz = tupian(i)
        baocun(tp,mz)
    print('爬取完成！')
