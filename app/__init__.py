from flask import Flask#从flask包中导入Flask类
from config import Config
app = Flask(__name__)#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app.config.from_object(Config)
from app import routes#从app包中导入模块routes