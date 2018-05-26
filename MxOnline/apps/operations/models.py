from django.db import models

from users.models import UserProfile
from courses.models import Course

# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name=u'姓名')
    mobile = models.CharField(max_length=11,
                              verbose_name=u'手机号码')
    course_name = models.CharField(max_length=50,
                                   verbose_name=u'课程名称')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE,
                             verbose_name=u'评论者')
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name=u'课程名称')
    comments = models.CharField(max_length=200,
                                verbose_name=u'评论内容')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE,
                             verbose_name=u'收藏用户')
    fav_id = models.IntegerField(default=0,
                                 verbose_name=u'数据id')
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '课程机构'), (3, '讲师')),
                                   default=1,
                                   verbose_name=u'收藏类型')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user_id = models.IntegerField(default=0,
                                  verbose_name=u'接受用户id')
    message = models.CharField(max_length=500,
                               verbose_name=u'消息内容')
    has_read = models.BooleanField(default=False,
                                   verbose_name=u'是否已读')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             verbose_name=u'用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name=u'课程')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name
