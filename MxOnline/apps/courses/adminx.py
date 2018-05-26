__author__ = 'yuzefeng'
__date__ = '2018/5/13 16:15'


import xadmin

from .models import Course, CourseResource, Vedio, Lesson


class CourseAdmin(object):

    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']


class CourseResourceAdmin(object):

    list_display = ['course', 'name', 'download_url', 'add_time']
    search_fields = ['course', 'name', 'download_url']
    list_filter = ['course__name', 'name', 'download_url', 'add_time']


class VedioAdmin(object):

    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class LessonAdmin(object):

    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Vedio, VedioAdmin)
xadmin.site.register(Lesson, LessonAdmin)

