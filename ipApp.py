from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import InternalServerError
import os
from subprocess import check_output

#Returns the internal ipv4: public and private
def local_ipv4():
    internalIP = check_output(['hostname', '-I'])
    internalIP = str(internalIP)[2:-3]
    return internalIP

# Returns the external ipv4
def external_ipv4():
    externalIP  = os.popen('curl -s -4 icanhazip.com').readline()
    return externalIP

app = Flask(__name__)

#if we get an internal server error we print an error message on the screen
@app.errorhandler(InternalServerError)
def validation_failure(err):
  return jsonify({"ERROR NAME !!!":" ---> PLEASE,TRY AGAIN !!!"}),500


@app.route('/')
def index():
    ex_ipv4_out = external_ipv4()
    in_ipv4_out = local_ipv4()
    return render_template('ipapp_ui.html',ex_ipv4 = ex_ipv4_out, in_ipv4 = in_ipv4_out)

if __name__=="__main__":
   #app.run(port=80,host="0.0.0.0")
    app.run(port=8080,host="0.0.0.0")


