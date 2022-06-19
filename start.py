# from pytest import importorskip
from xmlrpc.client import Server
from Control.rpc.app import app

app.run(debug=True,port=1024,host="0.0.0.0",threaded=True)