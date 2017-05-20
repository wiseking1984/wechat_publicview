import web
urls=(
      '/','index'
)
app = web.application(urls,globals())
if __name__ == "__main__": app.run()

class index:
    def GET(self):
        return "Hello world!" 