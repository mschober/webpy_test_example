import web
import os

urls = (
    '/', 'index'
)

app = web.application(urls, globals())
render = web.template.render('')

class index:
    def GET(self):
        return render.index()


def is_test():
    if 'WEBPY_ENV' in os.environ:
        return os.environ['WEBPY_ENV'] == 'test'

if (not is_test()) and __name__ == "__main__": 
    app.run()

