# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Order(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u"创建时间")
    update_time = models.DateTimeField(auto_now_add=True,verbose_name=u"修改时间")
    current_status = models.CharField(max_length=50,verbose_name=u"当前状态")
    current_location = models.CharField(max_length=50,verbose_name=u"当前位置")
    weight = models.FloatField(null=True, blank=True,verbose_name=u"重量")

    sender_name = models.CharField(max_length=50,verbose_name=u"发件人姓名")
    sender_address = models.CharField(max_length=50,verbose_name=u"发件人地址")
    sender_city = models.CharField(max_length=50,verbose_name=u"发件人城市")
    sender_country = models.CharField(max_length=50,verbose_name=u"发件人国家")
    sender_zip = models.CharField(max_length=50,verbose_name=u"发件人邮编")
    sender_contact = models.CharField(max_length=50,verbose_name=u"发件人联系方式")
    
    receiver_name = models.CharField(max_length=50,verbose_name=u"收件人姓名")
    receiver_address = models.CharField(max_length=50,verbose_name=u"收件人地址")
    receiver_city = models.CharField(max_length=50,verbose_name=u"收件人城市")
    receiver_country = models.CharField(max_length=50,verbose_name=u"收件人国家")
    receiver_zip = models.CharField(max_length=50,verbose_name=u"收件人邮编")
    receiver_contact = models.CharField(max_length=50,verbose_name=u"收件人联系方式")

    def __unicode__(self):
        return self.id
