#未完善
import json

def dict2user(d):#dict转user类
    return user(d['user_status'],d['id'],d['phone'],d['passwd'])
  
IS_LOGIN="NO"#登录状态初始化
USER_LIST=user("unlogin",0,0,0)#登录信息存储

def user_register():  #注册函数
    registerid=input("请输入用户名：")
    registertype_judge=input("请选择用户类型：0.管理员 1.学生")
    if registertype_judge=="0":
        registertype="administrator"
    else:
        registertype="student"
    while True:
        registerpasswd=input("请输入密码：")
        if len(registerpasswd)>=8:
            break
    while True:
        registerphone=input("请输入手机号：")
        if len(registerphone)==11:
            break
    register_user = user(registertype,registerid,registerphone,registerpasswd)
    registered=0
    with open("user.txt","r") as f:#对比是否已经注册过
        for line in f:
            user_list=json.loads(line,object_hook=dict2user)
            if register_user.id==user_list.id:
                print("用户名已被注册")
                registered=1
                break
            if register_user.phone==user_list.phone:
                print("手机号已被注册")
                registered=1
                break
    if registered==0:
        with open("user.txt","a") as f:
            f.write(json.dumps(register_user,default=lambda obj: obj.__dict__)+"\n")
        print("注册成功")
        
def register(): #注册
    if IS_LOGIN=="YES":
        print("已登录，无法注册")
    else:
        user_register()

def login():#登录  待完善检测
    userid=input("请输入用户id")
    userpasswd=input("请输入密码")
    with open("user.txt","r") as f:
        for line in f:
            user_list=json.loads(line,object_hook=dict2user)
            if user_list.id==userid and user_list.passwd==userpasswd:
                print("登录成功")
                global USER_LIST
                USER_LIST=user_list
                IS_LOGIN="YES"
            else:
                print("用户名或密码错误")
