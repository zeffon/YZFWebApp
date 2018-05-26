from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), max_length=5, verbose_name=u'性别', default='female')
    address = models.CharField(max_length=100, default=u'', verbose_name=u'联系地址')
    mobile = models.CharField(max_length=11, verbose_name=u'手机号码', null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100,
                              verbose_name=u'用户头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username



