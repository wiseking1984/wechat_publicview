#coding=utf-8
import hashlib
import web


from  msgparser import *
import picsave
import accessToken


basic = accessToken.Basic()
class InfoHandler:
    def GET(self):
        try:
            print "get request in Infohandler"
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "bio035token"

            list1 = [token, timestamp, nonce]
            list1.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list1)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            print "get exception in get"
            return Argument
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            recMsg = receive.parse_xml(webData)
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType != 'image':
                print "get common text wx msg msgtype:",recMsg.MsgType                
                content = "请把图片发给我，只接受图片哦" 
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'image':
                try:
                    print "get common image wx msg"
                    ps=picsave.picsave(recMsg.PicUrl,recMsg.FromUserName,recMsg.MediaId)
                    ps.save(basic.get_access_token())
                    content="图片已成功保存到服务器"
                    commonmsg = reply.TextMsg(toUser, fromUser, content)
                    return commonmsg.send()
                except IOError:
                    content="骚年，你传的图片太多了"
                    commonmsg = reply.TextMsg(toUser, fromUser, content)
                    return commonmsg.send()
            else:
                print "unknow msg type:"+recMsg.MsgType
                return "success"
        except Exception, Argment:
            print "get exception in post",Argment
            return Argment