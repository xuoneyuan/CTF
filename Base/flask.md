## flask是用python编写的一个轻量web开发框架

### web工作原理
#### B/S和C/S架构
- B/S：浏览器/服务器架构（客户端需要更新才行）
- C/S：客户端/服务器架构（刷新页面即可更新）（可能会成为主流）
#### WEB工作原理
客户端 > 服务器 > python(flask) > 数据库(mysql)

### Flask框架
#### 简介
是一个非常小的框架，可以称为微型框架，只提供了一个强劲的核心，其他的功能都需要使用拓展来实现。意味着可以根据自己的需求量身打造
#### 组成
- 调试、路由、wsgi系统
- 模板引擎(Jinja2)
#### 简单使用
~~~
# 导入Flask类库
from flask import Flask
# 创建应用实例
app = Flask(__naem__)
# 视图函数（路由）
@app.route('/')
def index():
	return '<h1>Hello Flask!<h1>'
# 启动实施（只在当前模块运行）
if __name__ == '__main__':
	app.run()
~~~

#### run方法参数
| 参数     | 说明                                 | 默认值        |
| -------- | ------------------------------------ | ------------- |
| debug    | 代码更新是否自动重启                 | False         |
| threaded | 是否开启多线程                       | False         |
| port     | 指定端口                             | 5000          |
| host     | 指定主机（设置0.0.0.0可以通过本地IP访问） | 127.0.0.1    |
#### 请求和响应
| 变量          | 上下文     | 描述                                                                                          |
| ------------- | ---------- | ----------------------------------------------------------------------------------------------- |
| current_app   | 应用上下文 | 相当于在主程序中激活的实例化 app（app=Flask(__name__)）                                            |
| g             | 应用上下文 | 一次性函数，处理请求的临时变量。只在一个请求中被应用，下个请求开始时会自动重置                    |
| request       | 请求上下文 | 请求对象。存放了客户端发来的 HTTP 信息                                                           |
| session       | 请求上下文 | 记录用户和服务器之间的会话的。在服务器端记录需要记住的信息。（和 cookie 对应，cookie 是记录在客户端的） |
#### 请求钩子装饰器
| 函数                   | 描述                           |
|------------------------|--------------------------------|
| before_first_request   | 在第一次请求之前运行            |
| before_request         | 每次请求之前运行                |
| app.after_request      | 没有异常时，在每次请求结束后运行 |
| app.teardown_request   | 有异常时，在每次请求结束后运行   |
#### 视图参数
1. 不带参数的视图函数
~~~
# 导入Flask类库
from flask import Flask
# 创建应用实例
app = Flask(__name__)
# 视图函数（路由）
@app.route('/index')
def index():
	return '<h1>Hello Flask!<h1>'
# 启动实施（只在当前模块运行）
if __name__ == '__main__':
	app.run()
~~~
2. 带参数的视图函数
~~~
# 导入Flask类库
from flask import Flask
# 创建应用实例
app = Flask(__name__)
# 视图函数（路由）
@app.route('/user/<username>')
def say_hello(username):
	return '<h1>Hello %s !<h1>' % username
# 启动实施（只在当前模块运行）
if __name__ == '__main__':
	app.run()
~~~
3. 带类型限定（path）的视图函数
~~~
# 导入Flask类库
from flask import Flask
# 创建应用实例
app = Flask(__name__)
# 视图函数（路由）
@app.route('/user/<path:info>')
def test(info):
	return info
# 启动实施（只在当前模块运行）
if __name__ == '__main__':
	app.run()
~~~
#### 获取request请求值
~~~
# 导入Flask类库
from flask import Flask,request
# 创建应用实例
app = Flask(__name__)
# request
@app.route('/request/<path:info>')
def request_url(info):
	# 完整的请求URL
	return request.url
	'''
	url：127.0.0.1:5000/request/abc/def?username=xiaoming&pwd=123
	网页返回值：http://127.0.0.1:5000/request/abc/def?username=xiaoming&pwd=123
	'''
	# 去掉GET参数的URL
	return request.base_url
	'''
	网页返回值：http://127.0.0.1:5000/request/abc/def
	'''
	# 只有主机和端口的URL
	return request.host_url
	'''
	网页返回值：http://127.0.0.1:5000/
	'''
	# 装饰器中写的路由地址
	return request.path
	'''
	网页返回值：/request/abc/def
	'''
	# 请求方法类型
	return request.method
	'''
	网页返回值：GET （也有可能时POST）
	'''
	# 远程地址
	return request.remote_addr
	'''
	网页返回值：127.0.0.1:5000
	'''
	# 获取url参数
	return request.args.get('username')
	return request.args.get('pwd')
	return str(request.args)
	# 获取headers信息
	return request.headers.get('User-Agent')
# 启动实施（只在当前模块运行）
if __name__ == '__main__':
	app.run()
~~~
#### 响应的构造（make_response）
~~~
from flask import Flask,make_response
app = Flask(__name__)
@app.route('/response/')
def response():
	# 不指定状态码，默认为200，表示OK
	# return ‘OK’
	# 构造一个404状态码
	# 方法一
	return 'not fount',404
	# 方法二
	# 导入make_response
	# 自定义构造一个响应，然后返回200，构造也可以指定状态码404
	res = make_response('我是通过函数构造的响应',404)
	return res
if __name__ == '__main__':
	app.run()
~~~
#### 重定向（redirect）
~~~
from flask import Flask,redirect
app = Flask(__name__)
@app.route('/old/)
def old():
	# return '这里是原始内容。'
	# 如果输入旧的old路由，会指向新的地址。
	# 先输入一个外地请求试试
	return redirect('https://www.baidu.com')
	# 再输入一个本地请求试试
	return redirect('/new/')
	# 根据视图函数找到路由,指向方法：<url_for>中的参数'new'指向的是<函数名>
	return redirect(url_for('new'))
	return redirect(url_for('say_hello',username='xiaoming'))
@app.rout('/new/')
def new():
	return '这里是新的内容'
if __name__ == '__main__':
	app.run()
~~~
#### 终止abort
~~~
from flask import Flask
app = Flask(__name__)
@app.route('/login/')
def login():
	# return '欢迎登录'
	# 此处使用abort可以主动抛出异常
	abort(404)
if __name__ == '__main__':
	app.run()
~~~
#### 会话控制cookie和session（附加过期时间的设置）
1. 会话控制cookie
~~~
# 发送到response的headers里面（客户端）
from flask import Flask
import time
app = Flask(__name__)
@app.route('/set_cookie/')
def set_cookie():
	resp = make_response('设置cookie')
	# 指定过期时间
	expires = time.time + 10
	resp.set_cookie('name','xiaoming',expires=expires)
	return resp
if __name__ == '__main__':
	app.run()
~~~
~~~
# 发送到request的headers里面（服务器）
# 如果清除cookie后，会导致name=xiaoming的cookie被清除。
# 那么就会在网页显示'你是哪个？'
from flask import Flask，request
app = Flask(__name__)
@app.route('/get_cookie/')
def get_cookie():
	return request.cookie.get('name') or '你是哪个？'
if __name__ == '__main__':
	app.run()
~~~
2. 会话控制session
~~~
# 发送到response的headers里面（客户端）
from flask import Flask,session
import time,os
'''
这里可以给SECRET_KEY设置一个随机N位字符串：os.urandom(n)
'''
app = Flask(__name__)
# 设置一个随机18位字符串的密钥，也可以设置成固定字符串
app.config['SECRET_KEY'] = os.urandom(18)
# app.config['SECRET_KEY'] = '这是个密钥字符串'
@app.route('/set_session/')
def set_session():
	# session本身是个字典，需要直接添加键值对
	'''
	添加session值之前，必须先设置SECRET_KEY
	'''
	session['username'] = 'xiaoqiao'
	return 'session已设置'
@app.route('/get_session/')
def get_session():
	# 获取session中的username的值，否则返回'who are you ?'
	return session.get('username','who are you ?')
if __name__ == '__main__':
	app.run()
~~~

## ssti
flask使用jinjia2渲染引擎进行网页渲染，当处理不得当，未进行语句过滤，用户输入{{控制语句}}，会导致渲染出恶意代码，形成注入

### flask基础知识
所有的子类都有一个共同的父类object,如果没指定继承，默认父类是object\
__class__:返回当前类（输入abc,是字符串类，除此以外还有元组类，字典类等）\
__mor__:返回解析函数时，类的调用顺序，本例先调用str类，再调用object类，通过索引的方式__mor[1]，就可返回object类\
当然还可以通过__base__：返回当前类父类（以字符串的形式）或者__bases__以元组的形式返回所有父类（元组可通过索引访问\


print('abc'.__class__.__bases__[0].__subclasses__())\
print('abc'.__class__.__base__.__subclasses__())这两者一样）\
__subclass__():返回当前类所有的子类，可通过索引的方式定位某一个子类
