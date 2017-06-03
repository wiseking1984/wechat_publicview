import sys
import os

import threading
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    print "import "+parent_path
    sys.path.append(parent_path)
import web
import accessToken.Basic
from msghandler import *
urls=(      
      "/wx","InfoHandler"
)
msghandler.basic = accessToken.Basic()
accessTask = threading.Thread(target=msghandler.basic.run(),args=())

app = web.application(urls,globals())
if __name__ == "__main__": 
    accessTask.setDaemon(True)
    accessTask.run()
    app.run()

#for test only
class index:
    def GET(self):
        return "Hello world!" 