# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from siteManager.models import ProductType, ProductContent, PlanType, PlanContent, CaseType, CaseContent, Attachment, \
    ArticleCategory, ArticleType, ArticleContent, RecruitContent, EmployeeLife, AttachmentPlan, HeroList, LeagueContent
from gsoftSite import settings
from django.http import JsonResponse
from django.core import serializers
import json as simplejson
from django.http import StreamingHttpResponse
import os
from django.db.models import Count

"""
    条件选取querySet的时候，filter表示=，exclude表示!=。
    querySet.distinct()  去重复
    __exact        精确等于 like 'aaa'
     __iexact    精确等于 忽略大小写 ilike 'aaa'
     __contains    包含 like '%aaa%'
     __icontains    包含 忽略大小写 ilike '%aaa%'，但是对于sqlite来说，contains的作用效果等同于icontains。
    __gt    大于
    __gte    大于等于
    __lt    小于
    __lte    小于等于
    __in     存在于一个list范围内
    __startswith   以...开头
    __istartswith   以...开头 忽略大小写
    __endswith     以...结尾
    __iendswith    以...结尾，忽略大小写
    __range    在...范围内
    __year       日期字段的年份
    __month    日期字段的月份
    __day        日期字段的日
    __isnull=True/False

"""
def index(request):

    content = {

    }
    return render(request, 'siteManager/index.html', content)

def homepage(request):
    carousel_page_list = {}
    companyContent = {}

    # 新闻热点
    if ArticleContent.objects.count() > 0:
        carousel_page_list = ArticleContent.objects.filter(Category__Code__exact='news').filter(
            IsPublish=True).values('id', 'Category__Code', 'Type__Code', 'Title', 'Attachment').order_by(
            '-PublishTime')[0:5]

    # 公司简介
    if ArticleContent.objects.filter(Category__Code='about').filter(Type__Code='about_company').count() > 0:
        companyContent = ArticleContent.objects.filter(Category__Code='about').filter(
            Type__Code='about_company').values('Content').first()

    content = {
        'carousel_page_list': carousel_page_list,
        'imgurl': settings.MEDIA_URL,
        'companyContent': companyContent
    }
    return render(request, 'siteManager/index_show.html', content)


# 加入我们
def joinus(request):
    live_list = {}
    recruit_list = {}
    # 员工生活
    if EmployeeLife.objects.filter().count() > 0:
        live_list = EmployeeLife.objects.filter().values(
            'id', 'Title', 'Attachment').order_by('-CreateTime')[0:5]

    # 人才招聘
    if RecruitContent.objects.filter(IsFinish=False).count() > 0:
        recruit_list = RecruitContent.objects.filter(IsFinish=False, IsPublish=True).values(
            'id', 'Position', 'Attachment')[0:3]

    content = {
        'liveList': live_list,
        'recruitlist': recruit_list,
        'imgurl': settings.MEDIA_URL,

    }

    return render(request, 'siteManager/joinus.html', content)


def joinusdetail(request, id):
    recruit_content = {}

    ecruit_list_new = []

    # 招聘详细信息
    if RecruitContent.objects.filter(IsFinish=False).count() > 0:
        ecruit_list = RecruitContent.objects.filter(IsFinish=False, IsPublish=True).values('id', 'Position')
    try:
        recruit_content = RecruitContent.objects.filter(pk=id).values('id', 'Position', 'Content').first()
    except recruit_content.DoesNotExist:
        raise Http404

    for ecruit in ecruit_list:

        if ecruit['id'] == int(id):
            model = {"id": ecruit['id'], "Position": ecruit['Position'], "iscurrent": True}
            ecruit_list_new.append(model)
        else:
            model = {"id": ecruit['id'], "Position": ecruit['Position'], "iscurrent": False}
            ecruit_list_new.append(model)

    if ecruit_list_new == None:
        ecruit_list_new = [{"id": "", "Position": "", "iscurrent": False}]

    content = {
        'recruit_list': ecruit_list_new,
        'recruit_content': recruit_content
    }
    return render(request, 'siteManager/joinusdetail.html', content)


def channel(request):
    content = {}
    return render(request, 'siteManager/channel.html', content)


def case(request):
    category_list = CaseType.objects.all().values('id', 'Name').order_by('SeqNumber')
    content_list = CaseContent.objects.filter(IsPublish=True).values('Title', 'TypeID__Name', 'TypeID').order_by('TypeID__SeqNumber', 'Title')
    content = {
        'category_list': category_list,
        'imgurl': settings.STATIC_URL,
        'content_list': content_list,
    }
    return render(request, 'siteManager/caseb.html', content)


def view_options(request, tabletype):
    if tabletype == 'product':
        if ProductType.objects.count() > 0:
            category_list = ProductType.objects.all().values('Code', 'Name', 'EnglishName').order_by('SeqNumber')

    if tabletype == 'plan':
        if PlanType.objects.count() > 0:
            category_list = PlanType.objects.all().values('Code', 'Name', 'EnglishName').order_by('SeqNumber')

    if tabletype == 'case':
        if CaseType.objects.count() > 0:
            category_list = CaseType.objects.all().values('Code', 'Name', 'EnglishName').order_by('SeqNumber')

    content = {
        'category_list': category_list,
        'tabletype': tabletype,
    }

    return render(request, 'siteManager/options.html', content)


def view_list(request, tabletype, typecode):
    category_list = {}
    detail_content = []
    category_first = {}

    # 公司产品 初始化加载
    if tabletype == 'product':
        if ProductContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).count() > 0:
            category_list_product = ProductContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).values(
                'Title', 'TypeID__Name', 'id')

            if category_list_product.__len__() > 0:
                category_list = category_list_product
                detail_content = Attachment.objects.filter(ForeiginID__exact=category_list_product[0]['id']).values(
                    'id', 'Attachment').order_by('OrderNumber')
                category_first = category_list_product.values('TypeID__Name').first()

    # 产品方案 初始化加载
    if tabletype == 'plan':
        if PlanContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).count() > 0:
            category_list_plan = PlanContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).values(
                'Title', 'TypeID__Name', 'id')

            if category_list_plan.__len__() > 0:
                category_list = category_list_plan
                detail_content = AttachmentPlan.objects.filter(ForeiginID__exact=category_list_plan[0]['id']).values(
                    'id', 'Attachment').order_by('OrderNumber')
                category_first = category_list_plan.values('TypeID__Name').first()

    if tabletype == 'case':
        if CaseContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).count() > 0:
            category_list = CaseContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).values('Title',
                                                                                                            'TypeID__Name',
                                                                                                            'id',
                                                                                                            'TypeID__Code')

    content = {
        'category_list': category_list,
        'category_first': category_first,
        'tabletype': tabletype,
        'detail_content': detail_content,
        'imgurl': settings.MEDIA_URL,
    }

    # return render(request, 'siteManager/detail.html', content)
    # return render(request, 'siteManager/detail_ajax.html', content)  # ajax版本

    return render(request, 'siteManager/detail_new.html', content)  # 新版本，内容图片


def view_detail(request, tabletype, typecode, contentid):
    category_list = {}
    category_first = {}
    if tabletype == 'product':
        if ProductContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).count() > 0:
            category_list = ProductContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).values('Title',
                                                                                                               'TypeID__Name',
                                                                                                               'id',
                                                                                                               'TypeID__Code')
            try:
                detail_content = ProductContent.objects.filter(pk=contentid).values('Title', 'Content').first()
            except detail_content.DoesNotExist:
                return HttpResponseRedirect(reverse('list'))

    if tabletype == 'plan':
        if PlanContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).count() > 0:
            category_list = PlanContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).values('Title',
                                                                                                            'TypeID__Name',
                                                                                                            'id',
                                                                                                            'TypeID__Code')
            try:
                detail_content = PlanContent.objects.filter(pk=contentid).values('Title', 'Content').first()
            except detail_content.DoesNotExist:
                return HttpResponseRedirect(reverse('list'))

        if tabletype == 'case':
            if CaseContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).count() > 0:
                category_list = CaseContent.objects.filter(TypeID__Code__exact=typecode, IsPublish=True).values('Title',
                                                                                                                'TypeID__Name',
                                                                                                                'id',
                                                                                                                'TypeID__Code')
                try:
                    detail_content = CaseContent.objects.filter(pk=contentid).values('Title', 'Content').first()
                except detail_content.DoesNotExist:
                    return HttpResponseRedirect(reverse('list'))

    if category_list.__len__() > 0:
        category_first = category_list.values('TypeID__Name').first()

    content = {
        'category_list': category_list,
        'category_first': category_first,
        'tabletype': tabletype,
        'detail_content': detail_content,
    }
    return render(request, 'siteManager/detail.html', content)


def view_article(request, category):
    article_list = []
    article_list2 = []
    if category == 'news':
        # 新闻列表

        if ArticleCategory.objects.filter(Code=category).count() > 0:
            article_list = ArticleContent.objects.filter(Category__Code=category).filter(
                Type__Code='news_company').filter(IsPublish=True).values(
                'id', 'Category', 'Type', 'Type__Code', 'Title', 'Attachment', 'CreateTime').order_by('-PublishTime')[
                           0:6]
            article_list2 = ArticleContent.objects.filter(Category__Code=category).filter(
                Type__Code='news_hotspot').filter(IsPublish=True).values(
                'id', 'Category', 'Type', 'Type__Code', 'Title', 'Attachment', 'CreateTime').order_by('-PublishTime')[
                            0:6]

    content = {
        'article_list': article_list,
        'article_list2': article_list2,
        'articletype': category,
        'imgurl': settings.MEDIA_URL,
    }

    return render(request, 'siteManager/newslist.html', content)


def view_about(request):
    companyContent = {}

    # 公司简介
    if ArticleContent.objects.filter(Category__Code='about').filter(Type__Code='about_company').count() > 0:
        companyContent = ArticleContent.objects.filter(Category__Code='about').filter(
            Type__Code='about_company').values('Content').first()

    content = {
        'companyContent': companyContent
    }

    return render(request, 'siteManager/about.html', content)


def view_articledetail(request, category, typecode, contentid):
    article_list_new = []
    article_first = {}
    detail_content = {}

    if category == 'news':
        # 新闻列表
        if ArticleType.objects.filter(Code=typecode).count() > 0:
            article_list = ArticleContent.objects.filter(Type__Code__exact=typecode).values(
                'Title', 'Type__Name', 'id').order_by('-PublishTime')
            try:
                detail_content = ArticleContent.objects.filter(pk=contentid).values('Title', 'Content',
                                                                                    'CreateTime').first()
            except detail_content.DoesNotExist:
                raise Http404

    for article in article_list:
        if article['id'] == int(contentid):
            article_list_new.append({"Title": article['Title'], "id": article['id'], "iscurrent": True})
        else:
            article_list_new.append({"Title": article['Title'], "id": article['id'], "iscurrent": False})

    if article_list.__len__() > 0:
        article_first = article_list.values('Type__Name').first()

    content = {
        'article_list': article_list_new,
        'article_first': article_first,
        'tabetype': category,
        'detail_content': detail_content
    }
    return render(request, 'siteManager/newsdetail.html', content)


def getContent_Ajax(request):
    tabletype = request.GET['table']
    contentid = request.GET['contentid']

    detail_content_default = {"Title": "", "Content": ""}

    # 产品 方案
    detail_default = {"id": "", "Attachment": ""}

    # 新闻
    detail_news_default = {"Title": "", "Content": "", "CreateTime": ""}
    # 招聘
    detail_joinus_default = {"id": "", "Position": "", "Content": ""}

    # 获取产品
    if tabletype == 'product':
        try:
            # detail_content = ProductContent.objects.filter(pk=contentid).values('Title', 'Content').first()
            product_content = Attachment.objects.filter(ForeiginID__exact=contentid).values('id',
                                                                                            'Attachment').order_by(
                'OrderNumber')
        except product_content.DoesNotExist:
            product_content = {"data": detail_default}

        # 判断是否为空
        if product_content == None:
            product_content = detail_default

        product_dict = ValuesQuerySetToDict(product_content)
        detail_content = {"data": simplejson.dumps(product_dict)}

    # 产品方案
    if tabletype == 'plan':
        try:
            # detail_content = PlanContent.objects.filter(pk=contentid).values('Title', 'Content').first()
            plan_content = AttachmentPlan.objects.filter(ForeiginID__exact=contentid).values('id',
                                                                                             'Attachment').order_by(
                'OrderNumber')
        except plan_content.DoesNotExist:
            plan_content = {"data": detail_default}

        # 判断是否为空
        if plan_content == None:
            plan_content = detail_default

        plan_dict = ValuesQuerySetToDict(plan_content)
        detail_content = {"data": simplejson.dumps(plan_dict)}


    # 获取案例
    if tabletype == 'case':
        try:
            detail_content = CaseContent.objects.filter(pk=contentid).values('Title', 'Content').first()
        except detail_content.DoesNotExist:
            detail_content = detail_content_default
            # 新闻
    if tabletype == 'news':
        try:
            detail_content = ArticleContent.objects.filter(pk=contentid).values('Title', 'Content',
                                                                                'CreateTime').first()
        except detail_content.DoesNotExist:
            detail_content = detail_news_default

    if tabletype == 'joinus':
        try:
            detail_content = RecruitContent.objects.filter(pk=contentid).values('id', 'Position', 'Content').first()
        except detail_content.DoesNotExist:
            detail_content = detail_joinus_default

    if detail_content == None:
        detail_content = detail_content_default

    return JsonResponse(detail_content)


# 获取选择省份的数据
def getCase_Ajax(request):
    area = request.GET['area']
    caseType_list = {"Code": "", "Name": ""}
    detail_content_default = {"TypeID__Name": "", "Title": ""}

    try:
        detail_content = CaseContent.objects.filter(Area=area, IsPublish=True).values('TypeID__Name', 'Title').order_by(
            'TypeID__Name')

    except detail_content.DoesNotExist:
        detail_content = detail_content_default

    if detail_content == None:
        detail_content = detail_content_default

    if CaseType.objects.filter().count() > 0:
        caseType_list = CaseType.objects.filter().values('Code', 'Name')

    data_dict = ValuesQuerySetToDict(detail_content)
    data_json = simplejson.dumps(data_dict)

    type_dict = ValuesQuerySetToDict(caseType_list)
    type_json = simplejson.dumps(type_dict)

    return JsonResponse({"res": "success", "msg": data_json, "type": type_json})
    # return HttpResponse(data_json)


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]


# 获取 所有案例的所在的省份
def getArea_Ajax(request):
    area_default = {"Area": "浙江", "dcount": "0"}

    # area_list= CaseContent.objects.filter(IsPublish=True).values('Area').distinct()

    # 获取默认省份
    maxarea = CaseContent.objects.values('Area').annotate(dcount=Count('Area')).order_by('-dcount').first()

    if maxarea == None:
        maxarea = area_default

    # area_dict=ValuesQuerySetToDict(maxarea)
    area_json = simplejson.dumps(maxarea)

    return JsonResponse({"data": area_json})


# 文件下载
def download(request):
    # do something...

    # fileid_=request.GET["fileid"]
    fileid_ = u'加盟申请表.doc'
    filepath_ = ('%s/%s' % (settings.MEDIA_ROOT, fileid_))  # 文件全路径
    file_ = fileid_.split('.', 1)
    filename_ = file_[0]
    filetype_ = '.' + file_[1]

    # fileid_ = u'加盟申请表.doc'
    # filepath_ = ('%s/%s' % (settings.MEDIA_ROOT, fileid_))  # 文件全路径
    # filename_ = u'加盟申请表'
    # filetype_ = u'.doc'

    if os.path.isfile(filepath_):
        pass
    else:
        # 文件不存在
        # pass
        return HttpResponse(u"文件不存在!")

    # 下载文件
    def readFile(fn, buf_size=262144):  # 大文件下载，设定缓存大小
        f = open(fn, "rb")
        while True:  # 循环读取
            c = f.read(buf_size)
            if c:
                yield c
            else:
                break
        f.close()

    response = HttpResponse(readFile(filepath_),
                            content_type='APPLICATION/OCTET-STREAM')  # 设定文件头，这种设定可以让任意文件都能正确下载，而且已知文本文件不是本地打开
    response['Content-Disposition'] = 'attachment; filename=' + filename_.encode('utf-8') + filetype_.encode(
        'utf-8')  # 设定传输给客户端的文件名称
    response['Content-Length'] = os.path.getsize(filepath_)  # 传输给客户端的文件大小

    return response


def league(request):
    content = {}
    return render(request, 'siteManager/league.html', content)


# 英雄榜数据
def getHero_Ajax(request):
    type = request.GET['type']
    detail_content_default = {"SeqNumber": "", "Name": ""}

    try:
        detail_content = HeroList.objects.filter(Type=type, IsPublish=True).values('SeqNumber', 'Name').order_by(
            'SeqNumber')[0:10]
    except detail_content.DoesNotExist:
        detail_content = detail_content_default
        return JsonResponse({"res": "failure", "msg": u'英雄榜没有数据'})

    if detail_content == None:
        detail_content = detail_content_default

    data_dict = ValuesQuerySetToDict(detail_content)
    data_json = simplejson.dumps(data_dict)
    return JsonResponse({"res": "success", "msg": data_json})


# 数据
def getLeagueContent_Ajax(request):
    type = request.GET['type']
    detail_content_default = {"Title": '', "Content": ""}

    try:
        detail_content = LeagueContent.objects.filter(ContentType=type, IsPublish=True).values('Title',
                                                                                               'Content').first()
    except detail_content.DoesNotExist:
        detail_content = detail_content_default
        return JsonResponse({"res": "failure", "msg": u'没有数据'})

    if detail_content == None:
        detail_content = detail_content_default

    # data_dict = ValuesQuerySetToDict(detail_content)
    # data_json = simplejson.dumps(data_dict)
    return JsonResponse({"res": "success", "msg": detail_content['Content']})


def getjoinus_Ajax(request):
    type = request.GET['type']
    content_default = {"id": '', "Title": "","Attachment": ""}

    if type == 'employeeLife' > 0:
         try:
            live_list = EmployeeLife.objects.filter().values('id', 'Title', 'Attachment').order_by('-CreateTime')[0:5]
         except live_list.DoesNotExist:
            live_list = content_default
            return JsonResponse({"res": "failure", "msg": u'没有数据'})

    data_dict = ValuesQuerySetToDict(live_list)
    return JsonResponse({"res": "success", "msg": simplejson.dumps(data_dict)})


def view_leaguedetail(request, typecode):
    article_list_new = []
    article_first = {}
    detail_content = {}

    # 新闻列表
    if LeagueContent.objects.filter(ContentType=typecode).count() > 0:
        article_list = LeagueContent.objects.values('Title', 'ContentType', 'id').order_by('SeqNumber')
        try:
            detail_content = LeagueContent.objects.filter(ContentType=typecode).values('Title', 'Content',
                                                                                'CreateTime').first()
        except detail_content.DoesNotExist:
            raise Http404

    for article in article_list:
        if article['ContentType'] == typecode:
            article_list_new.append({"Title": article['Title'], "ContentType": article['ContentType'], "iscurrent": True})
        else:
            article_list_new.append({"Title": article['Title'], "ContentType": article['ContentType'], "iscurrent": False})

    if article_list.__len__() > 0:
        article_first = article_list.values('ContentType').first()

    content = {
        'article_list': article_list_new,
        'article_first': article_first,
        'detail_content': detail_content
    }
    return render(request, 'siteManager/league_detail.html', content)