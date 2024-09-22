from flask import Flask,redirect,url_for
from views import home_page,shopping
app = Flask(__name__)
__id = id('secretKEY')
app.secret_key = '<{0}w@3{0}2g5%^jX6(__init__.py)fG54f{0}2h112FfF12gf5g{0}4h32g1f3h4{0}#5>'.format(__id)

# route's >>>
app.add_url_rule('/',endpoint='index',view_func=home_page,methods=['get'])
app.add_url_rule('/shop/',endpoint='shop',view_func=shopping,methods=['get'])

# Exception >>>
@app.route("/<name>")
def raise1(name):
    print(name)
    return redirect(url_for("index"),code=302,)

# Server >>>
if __name__=="__main__":
    app.port = 5000
    app.debug = True
    app.host = "127.0.0.1"
    app.name = 'mykala'
    app.run()