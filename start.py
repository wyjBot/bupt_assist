# from pytest import importorskip
from xmlrpc.client import Server
from Control.app import app

app.run(debug=True,port=1024,host="0.0.0.0")