from django.db import models
# Create your models here.
#发布会
class Event(models.Model):
     name=models.CharField(max_length=100)#发布会标题
     limit=models.IntegerField() #参会人数
     status=models.BooleanField()#状态
     address=models.CharField(max_length=200)#地址
     start_time= models.DateTimeField('event_time')#发布会时间
     create_time=models.DateTimeField(auto_now=True)#创建时间

     def __str__(self):
         return self.name
#嘉宾表
class Guest(models.Model):
    event=models.ForeignKey(Event,on_delete=models.DO_NOTHING)#关联发布会id
    realname=models.CharField(max_length=20)#姓名
    phone=models.CharField(max_length=16) #电话
    email=models.EmailField()#邮箱
    sign=models.BooleanField()#签到状态
    models.DateTimeField(auto_now=True)

class Meta:
    unique_together=("event","phone")


def __str__(self):
    return self.realname
