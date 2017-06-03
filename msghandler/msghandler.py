import hashlib
import web


from  msgparser import *
import picsave
import accessToken


basic = accessToken.Basic()
class InfoHandler:
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "bio035token" #请按照公众平台官网\基本配置中信息填写

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
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                print "get common text wx msg"
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "test" # 待替换成原始内容
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'image':
                print "get common image wx msg"
                ps=picsave(recMsg.PicUrl,recMsg.FromUserName,recMsg.MediaId)
                ps.save(basic.get_access_token())
                commonmsg = reply.Msg
                return commonmsg.send()
            else:
                print "未知消息类型暂且不处理:"+recMsg.MsgType
                return "success"
        except Exception, Argment:
            print "get exception in post"
            return Argment