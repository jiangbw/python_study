# 学习笔记

安装Django
1、mkdir learning_log
2、cd learning_log
3、python -m venv ll_env
4、source ll_env/bin/activate
   停止虚拟环境:deactivate
   1、pip install Django
   2、django-admin.py startproject learning_log .
   3、python3 manage.py migrate
   4、python3 manage.py runserver
   
创建应用
source ll_env/bin/activate 
python3 manage.py startapp learning_logs   

每当需要修改"学习笔记"，管理的数据时，都需要修改models.py、对learning_logs调用makemigrations、让Django迁移项目
1、修改models.py
2、python3 manage.py makemigrations learning_logs
3、python3 manage.py migrate

创建超级用户管理网站
source ll_env/bin/activate
python3 manage.py createsuperuser
jiang
110305
y
http://localhost:8000/admin/

learning_logs下都admin.py
from learning_logs.models import Topic,Entry
admin.site.register(Topic)
admin.site.register(Entry)

python3 manage.py shell
>>> from learning_logs.models import Topic
>>> Topic.objects.all()




