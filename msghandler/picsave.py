#coding=utf-8
import time
import urllib2
import json
import os,errno

class picsave():
    SAVEDIR = "/home/image"#pic dir
    def __init__(self, url,openid,mediaid):
        self.url = url
        self.openid = openid
        self.mediaid = mediaid
        #print url,openid,mediaid
        datestr=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        dirpath = picsave.SAVEDIR +"/"+openid+"/"+datestr
        
        self.makesuredirexist(dirpath)
        self.savepath=dirpath+"/"+self.mediaid+".jpg"
    def makesuredirexist(self,dirpath):
        if os.path.isdir(dirpath):
            if self.checkdirfilecnt(dirpath) :
                return
            else:
                raise IOError
        else:
            try:
                print "ready mk image dir: ", dirpath
                os.makedirs(dirpath)
            except OSError as exc: # Python >2.5 (except OSError, exc: for Python <2.5)
                if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
                    print "dir exist exception"
                else: print "get exception in mkdir :"+exc
    def checkdirfilecnt(self,dirpath):
        count = len(os.listdir(dirpath))        
        print dirpath," 下的图片数量 ",count
        if count > 300:
            return False
        else:
            return True
            
    def save(self,accessToken):
        try:            
            #postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, self.mediaid)
            postUrl=self.url
            print "get image from url: ", postUrl
            urlResp = urllib2.urlopen(postUrl,timeout=10)
    
            headers = urlResp.info().__dict__['headers']
            if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
                jsonDict = json.loads(urlResp.read())
                print "temple pic but get json or text msg"
                print jsonDict
            else:
                picbuffer = urlResp.read()   
                mediaFile = file(self.savepath, "wb")
                mediaFile.write(picbuffer)
                print "successful write pic "+self.savepath
        except urllib2.HTTPError, e:
            print "error: get image url "+postUrl+" failed!"
            print e.code
        