# -*- coding: utf-8 -*-

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField




# Create your models here.

class ProductType(models.Model):
    Code = models.CharField(verbose_name='编码', max_length=20, unique=True)
    Name = models.CharField(verbose_name='名称', max_length=50)
    EnglishName = models.CharField(verbose_name='英文名称', max_length=100)
    SeqNumber = models.IntegerField(verbose_name='序号', null=True, blank=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Name

    class Meta:
        verbose_name = '产品类别'
        verbose_name_plural = '产品类别'


class ProductContent(models.Model):
    TypeID = models.ForeignKey(ProductType, verbose_name='产品类别')
    # TypeCode = models.CharField(verbose_name='编码', max_length=20, unique=True)  #字段废除
    ProductType = models.CharField(verbose_name='产品细类', max_length=20, blank=True)
    Title = models.CharField(verbose_name='标题', max_length=100)
    Summary = models.CharField(verbose_name='副标题', max_length=200, null=True, blank=True)
    Content = RichTextUploadingField(verbose_name='详细内容', null=True, blank=True)
    Hits = models.IntegerField(verbose_name='点击数', null=True, blank=True, editable=False)
    IsPublish = models.BooleanField(verbose_name='是否发布', default=False)
    Attachment = models.FileField(verbose_name='附件', null=True, blank=True)
    CreateTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Title

    class Meta:
        verbose_name = '产品内容'
        verbose_name_plural = '产品内容'


class PlanType(models.Model):
    Code = models.CharField(verbose_name='编码', max_length=20, unique=True)
    Name = models.CharField(verbose_name='名称', max_length=50)
    EnglishName = models.CharField(verbose_name='英文名称', max_length=100)
    SeqNumber = models.IntegerField(verbose_name='序号', null=True, blank=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Name

    class Meta:
        verbose_name = '方案类别'
        verbose_name_plural = '方案类别'


class PlanContent(models.Model):
    TypeID = models.ForeignKey(PlanType, verbose_name='方案类别')
    # TypeCode = models.CharField(verbose_name='编码', max_length=20, unique=True)
    ProductType = models.CharField(verbose_name='产品细类', max_length=20, blank=True)
    Title = models.CharField(verbose_name='标题', max_length=100)
    Summary = models.CharField(verbose_name='副标题', max_length=200, null=True, blank=True)
    Content = RichTextUploadingField(verbose_name='详细内容', null=True, blank=True)
    Hits = models.IntegerField(verbose_name='点击数', null=True, blank=True, editable=False)
    IsPublish = models.BooleanField(verbose_name='是否发布', default=False)
    Attachment = models.CharField(verbose_name='附件', max_length=200, null=True, blank=True)
    CreateTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Title

    class Meta:
        verbose_name = '方案内容'
        verbose_name_plural = '方案内容'


class CaseType(models.Model):
    Code = models.CharField(verbose_name='编码', max_length=20, unique=True)
    Name = models.CharField(verbose_name='名称', max_length=50)
    EnglishName = models.CharField(verbose_name='英文名称', max_length=100)
    SeqNumber = models.IntegerField(verbose_name='序号', null=True, blank=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Name

    class Meta:
        verbose_name = '案例类别'
        verbose_name_plural = '案例类别'


class CaseContent(models.Model):
    AREA_CHOICES = (
        (u'北京', u'北京'),
        (u'天津', u'天津'),
        (u'上海', u'上海'),
        (u'重庆', u'重庆'),
        (u'河北', u'河北'),
        (u'河南', u'河南'),
        (u'云南', u'云南'),
        (u'辽宁', u'辽宁'),
        (u'黑龙江', u'黑龙江'),
        (u'湖南', u'湖南'),
        (u'安徽', u'安徽'),
        (u'山东', u'山东'),
        (u'新疆', u'新疆'),
        (u'江苏', u'江苏'),
        (u'浙江', u'浙江'),
        (u'江西', u'江西'),
        (u'湖北', u'湖北'),
        (u'广西', u'广西'),
        (u'山西', u'山西'),
        (u'内蒙古', u'内蒙古'),
        (u'陕西', u'陕西'),
        (u'吉林', u'吉林'),
        (u'福建', u'福建'),
        (u'贵州', u'贵州'),
        (u'广东', u'广东'),
        (u'青海', u'青海'),
        (u'西藏', u'西藏'),
        (u'四川', u'四川'),
        (u'宁夏', u'宁夏'),
        (u'海南', u'海南'),
        (u'台湾', u'台湾'),
        (u'香港', u'香港'),
        (u'澳门', u'澳门'),
        (u'南海诸岛', u'南海诸岛'),
    )
    TypeID = models.ForeignKey(CaseType, verbose_name='案例类别', related_name='TypeName')
    # TypeCode = models.CharField(verbose_name='编码', max_length=20, unique=True)
    Area = models.CharField(verbose_name='区域', max_length=10, choices=AREA_CHOICES, default=u'浙江')
    # ProductType = models.CharField(verbose_name='产品细类', max_length=20, blank=True)
    Title = models.CharField(verbose_name='单位名称', max_length=100)
    Summary = models.CharField(verbose_name='标题', max_length=200, null=True, blank=True)
    Content = RichTextUploadingField(verbose_name='详细内容', null=True, blank=True)
    Hits = models.IntegerField(verbose_name='点击数', null=True, blank=True, editable=False)
    IsPublish = models.BooleanField(verbose_name='是否发布', default=False)
    Attachment = models.FileField(verbose_name='附件', null=True, blank=True)
    CreateTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Title

    class Meta:
        verbose_name = '案例内容'
        verbose_name_plural = '案例内容'


class Attachment(models.Model):
    ForeiginID = models.ForeignKey(ProductContent,verbose_name='产品内容')
    # AttachmentName = models.CharField(verbose_name='名称', max_length=100,null=True, blank=True)
    OrderNumber= models.IntegerField(verbose_name='排序号',default=1)
    Attachment = models.FileField(verbose_name='附件', null=True, blank=True)
    CreateTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    # def __unicode__(self):  # For Python 2, use __str__ on Python 3
    #     return self.AttachmentName

    class Meta:
        verbose_name_plural =verbose_name = '产品内容-附件'


class ArticleCategory(models.Model):
    Code = models.CharField(verbose_name='编码', max_length=20, unique=True)
    Name = models.CharField(verbose_name='名称', max_length=50)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Name

    class Meta:
        verbose_name = '文章大类'
        verbose_name_plural = '文章大类'


class ArticleType(models.Model):
    Code = models.CharField(verbose_name='编码', max_length=20, unique=True)
    Name = models.CharField(verbose_name='名称', max_length=50)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Name

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = '文章类别'


class ArticleContent(models.Model):
    Category = models.ForeignKey(ArticleCategory, verbose_name='文章大类')
    Type = models.ForeignKey(ArticleType, verbose_name='文章类别')
    # TypeCode = models.CharField(verbose_name='编码', max_length=20, unique=True)   #字段废除
    ProductType = models.CharField(verbose_name='产品细类', max_length=20, blank=True)
    Title = models.CharField(verbose_name='标题', max_length=100)
    Summary = models.CharField(verbose_name='副标题', max_length=200, blank=True)
    Content = RichTextUploadingField(verbose_name='详细内容')
    Hits = models.IntegerField(verbose_name='点击数', null=True, default=0)
    IsPublish = models.BooleanField(verbose_name='是否发布', default=False)
    PublishTime = models.DateTimeField(verbose_name='发布时间',auto_now=True)  # 字段废除
    IsHot = models.BooleanField(verbose_name='是否热门')
    Attachment = models.FileField(verbose_name='附件', null=True, blank=True)
    Editor = models.CharField(verbose_name='编辑者', max_length=50, blank=True)
    CreateTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Title

    class Meta:
        verbose_name = '文章内容'
        verbose_name_plural = '文章内容'

class RecruitContent(models.Model):
    Position = models.CharField(verbose_name='招聘职位', max_length=50, blank=True)
    Content = RichTextUploadingField(verbose_name='招聘内容',null=True, blank=True)
    IsPublish = models.BooleanField(verbose_name='是否发布', default=False)
    IsFinish = models.BooleanField(verbose_name='招聘结束', default=False)
    Attachment = models.FileField(verbose_name='附件', null=True, blank=True)
    CreateTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Position

    class Meta:
        verbose_name_plural = verbose_name = '招聘内容'


class EmployeeLife(models.Model):
    Title = models.CharField(verbose_name='图片说明', max_length=100)
    Attachment = models.FileField(verbose_name='图片上传', null=True, blank=True)
    CreateTime = models.DateTimeField(verbose_name='新增时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Title

    class Meta:
        verbose_name_plural =verbose_name = '员工生活'


#加盟我们内容表
class LeagueContent(models.Model):
    LEAGUE_CONTENTTYPE_CHOICES = (
        (u'申请加盟', u'申请加盟'),
        (u'支持保障', u'支持保障'),
        (u'伙伴体系', u'伙伴体系'),
        (u'伙伴招聘', u'伙伴招聘'),
    )
    ContentType = models.CharField(verbose_name='内容类别', max_length=10, choices=LEAGUE_CONTENTTYPE_CHOICES, default=u'申请加盟')
    Title = models.CharField(verbose_name='标题', max_length=100)
    Content = RichTextUploadingField(verbose_name='详细内容')
    IsPublish = models.BooleanField(verbose_name='是否发布', default=False)
    CreateTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    SeqNumber = models.IntegerField(verbose_name='序号', null=True, blank=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Title

    class Meta:
        verbose_name = '渠道加盟-内容'
        verbose_name_plural = '渠道加盟-内容'


class HeroList(models.Model):
    Type = models.CharField(verbose_name='类别', max_length=10, default=u'渠道')
    Name = models.CharField(verbose_name='英雄名称', max_length=100)
    SeqNumber = models.IntegerField(verbose_name='序号', unique=True, default= 1)
    IsPublish = models.BooleanField(verbose_name='是否发布', default=False)
    CreateTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.Name

    class Meta:
        verbose_name = '英雄榜'
        verbose_name_plural = '英雄榜'


class AttachmentPlan(models.Model):
    ForeiginID = models.ForeignKey(PlanContent,verbose_name='方案内容')
    OrderNumber= models.IntegerField(verbose_name='排序号',default=1)
    Attachment = models.FileField(verbose_name='附件', null=True, blank=True)
    CreateTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name_plural =verbose_name = '方案内容-附件'