from flask import Flask,request,redirect,make_response,render_template
from flask import send_from_directory,send_file  
import os.path as path
import time,random,sys,os,shutil
import json as js
import numpy as np
from multiprocessing import Process
from .. Utils import log 
from datetime import datetime,timedelta

app = Flask(__name__,template_folder='')


def save_cfg():
    global pwd,cfgPwd
    global cfgs
    cfgfile=cfgPwd+"cfg.json"
    try:
        with open(cfgfile,"w+") as fw:
             js.dump(cfgs,fw)
    except:pass


def load_cfg():
    global cfgs
    global cronLock
    global pwd,cfgPwd
    cronLock=0;upfileId=0
    pwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"
    cfgPwd=os.path.join(pwd,"config")+"/"
    cfgfile=cfgPwd+"cfg.json"
    try:
        with open(cfgfile,"r+") as fr: cfgs=js.load(fr)
        upfileId=cfgs['upfileId']
    except:pass
    try:
        shutil.rmtree(pwd+"tmp")
    except:pass
    try:
        os.makedirs(pwd+"tmp")
        os.makedirs(cfgPwd)
    except:pass


if __name__ == '__main__':
    app.run(debug=True,port=1024,host="0.0.0.0")
