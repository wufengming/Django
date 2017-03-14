# -*- coding:utf-8 -*-

from django.contrib import admin
from siteManager.models import ProductType, ProductContent, PlanType, PlanContent, CaseType, CaseContent, Attachment, \
    ArticleCategory, ArticleType, ArticleContent, RecruitContent, EmployeeLife, AttachmentPlan, LeagueContent, HeroList
import time


def make_published(modeladmin, request, queryset):
    queryset.update(IsPublish=True)


make_published.short_description = "发布 所选的内容"  # 这里的短描述是action下拉框中显示的描述


def make_publishedTime(modeladmin, request, queryset):
    queryset.update(IsPublish=True, PublishTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


make_publishedTime.short_description = "发布 所选的内容"  # 这里的短描述是action下拉框中显示的描述


class ProductContentAdmin(admin.ModelAdmin):
    list_display = ['Title', 'TypeID', 'IsPublish', 'CreateTime']
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ['TypeID__Name', 'CreateTime']
    # 这是发布操作
    actions = [make_published]

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    list_filter = ('TypeID', 'IsPublish')  # 筛选器
    search_fields = ('Title',)  # 搜索字段


class PlanContentAdmin(admin.ModelAdmin):
    list_display = ['Title', 'TypeID', 'IsPublish', 'CreateTime']
    ordering = ['TypeID__Name', 'CreateTime']
    actions = [make_published]

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    list_filter = ('TypeID', 'IsPublish')  # 筛选器
    search_fields = ('Title',)  # 搜索字段


class CaseContentAdmin(admin.ModelAdmin):
    list_display = ['Title', 'TypeID', 'Area', 'IsPublish', 'CreateTime']
    ordering = ['Area', 'TypeID__Name', 'CreateTime']
    actions = [make_published]

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    list_filter = ('TypeID', 'IsPublish', 'Area')  # 筛选器
    search_fields = ('Title',)  # 搜索字段


# ArticleContent模型的管理器
class ArticleContentAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('Title', 'Category', 'Type', 'IsPublish', 'PublishTime', 'CreateTime')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-CreateTime',)

    # 筛选器
    list_filter = ('Category', 'Type')  # 过滤器
    search_fields = ('Title',)  # 搜索字段
    # date_hierarchy = 'CreateTime'  # 详细时间分层筛选

    # 排除 编辑/新增  页面显示的字段
    exclude = ('Hits', 'PublishTime')  # 排除该字段
    actions = [make_publishedTime]

    # 方法二fieldsets
    # 编辑字段集合 组合显示 编辑页面的字段显示的位置
    # fieldsets = (
    #     ("Type", {'fields': ['Category', 'Type']})
    #     ("Information", {'fields': ['Title', 'Summary','Content','IsPublish','IsHot']}),
    #     ("Content", {'fields': ['Content']}),
    #
    # )


class TypeAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Name', 'EnglishName', 'SeqNumber')


class RecruitContentAdmin(admin.ModelAdmin):
    list_display = ['Position', 'IsPublish', 'CreateTime']
    ordering = ['IsPublish', 'CreateTime']
    actions = [make_published]

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    list_filter = ('Position', 'IsPublish')  # 筛选器
    search_fields = ('Position',)  # 搜索字段


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('ForeiginID', 'Attachment', 'OrderNumber')


class AttachmentPlanAdmin(admin.ModelAdmin):
    list_display = ('ForeiginID', 'Attachment', 'OrderNumber')


class LeagueContentAdmin(admin.ModelAdmin):
    list_display = ['Title', 'ContentType', 'IsPublish', 'CreateTime', 'SeqNumber']
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ['SeqNumber', 'ContentType']
    # 这是发布操作
    actions = [make_published]

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    list_filter = ('ContentType', 'IsPublish')  # 筛选器
    search_fields = ('Title',)  # 搜索字段


class HeroListAdmin(admin.ModelAdmin):
    list_display = ['SeqNumber', 'Name', 'Type', 'IsPublish', 'CreateTime']
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ['Type', 'SeqNumber', 'CreateTime']
    # 这是发布操作
    actions = [make_published]

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    list_filter = ('Type', 'IsPublish')  # 筛选器
    search_fields = ('Name',)  # 搜索字段


# Register your models here.
admin.site.register(ProductType, TypeAdmin)
admin.site.register(ProductContent, ProductContentAdmin)
admin.site.register(PlanType, TypeAdmin)
admin.site.register(PlanContent, PlanContentAdmin)
admin.site.register(CaseType, TypeAdmin)
admin.site.register(CaseContent, CaseContentAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(ArticleCategory)
admin.site.register(ArticleType)
admin.site.register(ArticleContent, ArticleContentAdmin)
admin.site.register(RecruitContent, RecruitContentAdmin)
admin.site.register(EmployeeLife)
admin.site.register(LeagueContent, LeagueContentAdmin)
admin.site.register(HeroList, HeroListAdmin)
admin.site.register(AttachmentPlan, AttachmentPlanAdmin)
