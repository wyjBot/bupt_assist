# from pytest import importorskip
from xmlrpc.client import Server
from Control.rpc.app import app
import os,Utils.corn

Utils.corn.cleanFile()
os.remove("Control/cfg.lock")
app.run(debug=False,port=1024,host="0.0.0.0",processes=50,threaded=False)
