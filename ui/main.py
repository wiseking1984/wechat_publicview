import sys
import os

import threading
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    print "import "+parent_path
    sys.path.append(parent_path)
import web
import accessToken
from msghandler import *
urls=(      
      #"/wx","InfoHandler"
      '/','index'
)
msghandler.basic = accessToken.Basic()
accessTask = threading.Thread(target=msghandler.basic,args=())


if __name__ == "__main__": 
    print "start main"    
    app = web.application(urls,globals())
    app.run()
    accessTask.setDaemon(True)
    accessTask.start()
    print "app run"

#for test only
class index:
    def GET(self):        
        return "Hello world!" +msghandler.basic.get_access_token()