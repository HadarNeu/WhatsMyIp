import urllib.request
from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import InternalServerError
import os

# class ipAppClass():
#     def __init__(self):
#         pass
def ip4Func():
    external_ip4 = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
    return external_ip4

def ip6Func():
    external_ip6 = urllib.request.urlopen('https://v6.ident.me').read().decode('utf8')
    return external_ip6

# Another way I liked to return the external ipv4
def ip4os():
    externalIP  = os.popen('curl -s ifconfig.me').readline()
    return externalIP

app = Flask(__name__)

#if we get an internal server error we print an error message on the screen
@app.errorhandler(InternalServerError)
def validation_failure(err):
  return jsonify({"ERROR NAME !!!":" ---> PLEASE,TRY AGAIN !!!"}),500


@app.route('/')
def index():
    ip4out = ip4Func()
    ip6out = ip6Func()
    return render_template('test.html',ipv4 = ip4out, ipv6 = ip6out)

if __name__=="__main__":
    app.run(port=80,host="0.0.0.0")

