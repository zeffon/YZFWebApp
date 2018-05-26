from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name=u'课程名称')
    desc = models.CharField(max_length=300,
                            verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=2,
                              choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')),
                              verbose_name=u'难度')
    learn_times = models.IntegerField(default=0,
                                      verbose_name=u'学习时长(分钟数)')
    students = models.IntegerField(default=0,
                                   verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0,
                                   verbose_name=u'收藏人数')
    image = models.ImageField(max_length=200,
                              upload_to='course/%Y/%m',
                              verbose_name=u'课程图片')
    click_nums = models.IntegerField(default=0,
                                     verbose_name=u'点击数')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 章节表
class Lesson(models.Model):
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name=u'课程')
    name = models.CharField(max_length=50,
                            verbose_name=u'章节标题')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 视频表
class Vedio(models.Model):
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               verbose_name=u'章节')
    name = models.CharField(max_length=50,
                            verbose_name=u'视频标题')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 资源表
class CourseResource(models.Model):
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name=u'课程')
    name = models.CharField(max_length=50,
                            verbose_name=u'资源名称')
    download_url = models.FileField(max_length=200,
                                    upload_to='course/resource/%Y/%m',
                                    verbose_name=u'资源文件')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



