# -*- coding: cp936 -*-
import WebCrawler

url = raw_input('�������url(��-->http://www.baidu.com): \n')
thNumber = int(raw_input('�����߳���:'))    #֮ǰ����δת����bug

wc = WebCrawler.WebCrawler(thNumber)
wc.Craw(url)
