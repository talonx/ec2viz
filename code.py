import web
import ec2data

urls = (
    '/instancedata', 'ec2data.ec2data'
)

#class index:
#    def GET(self):
#        return ec2data.json()

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
