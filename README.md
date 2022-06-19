DataBase为公用数据结构,子文件按类型进行划分储存
Upload为用户上传的作业(各种)文件,子文件按日期进行划分储存
Utils为公用基础模块,下辖用户管理模块[3],基本数据类型定义[2],日志记录与管理[1]
Navigate为导航路径规划模块 由[1]完成
Control/Panel为前端,由[2]完成
Control/rpc为主控交互模块,,由[2]完成
Control/admin.py为管理员工具,,由[2]完成

# 管理员数据导入方法
在`\Control\import`下放好json数据后
在根目录运行`python Control/admin.py`

# 安装方法
在根目录运行`python Control/reInstall.py`

# 日志文件查看
在`\Control\Log`下

