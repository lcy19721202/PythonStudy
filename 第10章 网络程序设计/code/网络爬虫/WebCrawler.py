# -*- coding: cp936 -*-
import threading
import GetUrl
import urllib

g_mutex = threading.Lock()
g_pages = []      #�߳�����ҳ��󣬽�ҳ��������ӵ����list��
g_dledUrl = []    #�������ع���url
g_toDlUrl = []    #��ǰҪ���ص�url
g_failedUrl = []  #����ʧ�ܵ�url
g_totalcount = 0  #���ع���ҳ����

class WebCrawler:
    def __init__(self,threadNumber):
        self.threadNumber = threadNumber
        self.threadPool = []
        self.logfile = file('#log.txt','w')                                   ##

    def download(self, url, fileName):
        Cth = CrawlerThread(url, fileName)
        self.threadPool.append(Cth)
        Cth.start()

    def downloadAll(self):
        global g_toDlUrl
        global g_totalcount
        i = 0
        while i < len(g_toDlUrl):
            j = 0
            while j < self.threadNumber and i + j < len(g_toDlUrl):
                g_totalcount += 1    #����ѭ��������ҳ������1
                self.download(g_toDlUrl[i+j],str(g_totalcount)+'.htm')
                print 'Thread started:',i+j,'--File number = ',g_totalcount
                j += 1
            i += j
            for th in self.threadPool:
                th.join(30)     #�ȴ��߳̽�����30�볬ʱ
            self.threadPool = []    #����̳߳�
        g_toDlUrl = []    #����б�

    def updateToDl(self):
        global g_toDlUrl
        global g_dledUrl
        newUrlList = []
        for s in g_pages:
            newUrlList += GetUrl.GetUrl(s)   #######GetUrlҪ����ʵ��
        g_toDlUrl = list(set(newUrlList) - set(g_dledUrl))    #��ʾunhashable
                
    def Craw(self,entryUrl):    #����һ�������������g_toDlUrlΪ��ʱ����
        g_toDlUrl.append(entryUrl)
        depth = 0
        while len(g_toDlUrl) != 0:
            depth += 1
            print 'Searching depth ',depth,'...\n\n'
            self.downloadAll()
            self.updateToDl()
            content = '\n>>>Depth ' + str(depth)+':\n'                         ##���ñ�Ǳ�ʾ���������д�ļ���¼��
            self.logfile.write(content)                                        ##
            i = 0                                                              ##
            while i < len(g_toDlUrl):                                          ##
                content = str(g_totalcount + i) + '->' + g_toDlUrl[i] + '\n'   ##
                self.logfile.write(content)                                    ##
                i += 1                                                         ##
         
class CrawlerThread(threading.Thread):
    def __init__(self, url, fileName):
        threading.Thread.__init__(self)
        self.url = url    #���߳����ص�url
        self.fileName = fileName

    def run(self):    #�̹߳���-->����htmlҳ��
        global g_mutex
        global g_failedUrl
        global g_dledUrl
        try:
            f = urllib.urlopen(self.url)
            s = f.read()
            fout = file(self.fileName, 'w')
            fout.write(s)
            fout.close()
        except:
            g_mutex.acquire()    #�߳���-->����
            g_dledUrl.append(self.url)
            g_failedUrl.append(self.url)
            g_mutex.release()    #�߳���-->�ͷ�
            print 'Failed downloading and saving',self.url
            return None    #���ŷ���!
        
        g_mutex.acquire()    #�߳���-->����
        g_pages.append(s)
        g_dledUrl.append(self.url)
        g_mutex.release()    #�߳���-->�ͷ�
