import sys
import os
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    print "import "+parent_path
    sys.path.append(parent_path)
import web
urls=(
      '/','index'
)
app = web.application(urls,globals())
if __name__ == "__main__": app.run()

class index:
    def GET(self):
        return "Hello world!" 