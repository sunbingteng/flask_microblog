from flask import render_template, redirect
from app import app#从app包中导入 app这个实例
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
#1个视图函数
def index():
	user = {'username': 'sbt'}
	return render_template('index.html', title='Home', user=user)
@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()#表单实例化对象
	if form.validate_on_submit():
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)