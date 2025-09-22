from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI(web server Gateqay interface) application
'''
app=Flask(__name__) ##WSGI application

@app.route("/")
def welcome():
    return "Welcome to this best FLask COurse. This should be an amazing course "

@app.route("/index")
def index():
    return "Welcome to this index page "


if __name__=="__main__":
    app.run(debug=True)