# -*- coding: utf-8 -*-

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gsoftSite.settings')

import django

django.setup()

from siteManager.models import ProductType, ProductContent, PlanType, PlanContent, CaseType, CaseContent, Attachment, \
    ArticleCategory, ArticleType, ArticleContent, LeagueContent

from django.contrib.auth.models import User


def createuser():
    superuser = User.objects.create_superuser('admin', '12@qq.com', '123456')
    # user = User.objects.create_user()


def populate():
    # ArticleCategory表的初始化创建（文章大类）

    add_category('news', '新闻动态')
    add_category('about', '关于我们')
    # ArticleType表的初始化创建 (文章类别)
    add_type('news_company', '公司动态')
    add_type('news_hotspot', '热点关注')
    add_type('about_company', '公司简介')
    # add_type('about_network', '营销网络')

    # ProductType表的初始化创建（产品类别）

    content_product_cz = add_producttype('cz', '数字财政', 'shuzicaizheng', 1)

    add_productcontent(content_product_cz, 'G6', '新中大电子政务软件(G6)')
    add_productcontent(content_product_cz, 'G3', '新中大事行财务软件(G3)')

    content_product_gh = add_producttype('gh', '智慧工会', 'zhihuisannong', 2)

    add_productcontent(content_product_gh, 'G6H', '新中大工会财务集中管控管理软件(G6H)')
    add_productcontent(content_product_gh, 'GH', '新中大工会财务管理软件(GH)')
    add_productcontent(content_product_gh, 'GHE', '工会e家(GHE)')

    content_product_nj = add_producttype('nj', '数字农经', 'shuzinongjing', 3)

    add_productcontent(content_product_nj, 'N3', '新中大农村经营管理软件(N3)')
    add_productcontent(content_product_nj, 'N3H', '新中大农村专业合作社管理软件(N3H)')

    # PlanType表的初始化创建（方案类别）


    content_Plan_cz = add_plantype('cz', '数字财政', 'shuzicaizheng', 1)

    add_plancontent(content_Plan_cz, 'cz_1', '公共财政一体化解决方案')
    add_plancontent(content_Plan_cz, 'cz_2', '行政事业单位内控管理解决方案')
    add_plancontent(content_Plan_cz, 'cz_3', '新政府会计制度解决')

    content_Plan_gh = add_plantype('gh', '智慧工会', 'zhihuisannong', 2)

    add_plancontent(content_Plan_gh, 'gh_1', '工会财务大数据管理应用平台解决方案')
    add_plancontent(content_Plan_gh, 'gh_2', '智慧工会解决方案')

    content_Plan_nj = add_plantype('nj', '数字农经', 'shuzinongjing', 3)

    add_plancontent(content_Plan_nj, 'nj_1', '农村经营管理决定方案')
    add_plancontent(content_Plan_nj, 'nj_2', '农民专业合作社管理解决方案')

    # CaseType表的初始化创建（案例类别）
    add_casetype('lc', '数字财政')
    add_casetype('gh', '智慧工会')
    add_casetype('n3', '数字农经')

    # LeagueContent表的初始化创建
    add_leaguecontent('申请加盟', '申请加盟', 1)
    add_leaguecontent('支持保障', '支持保障', 2)
    add_leaguecontent('伙伴体系', '伙伴体系', 3)
    add_leaguecontent('伙伴招聘', '伙伴招聘', 4)


def add_category(code, name):
    c = ArticleCategory.objects.get_or_create(Code=code, Name=name)[0]
    return c


def add_type(code, name):
    c = ArticleType.objects.get_or_create(Code=code, Name=name)[0]
    return c


def add_producttype(code, name, englishname, num):
    c = ProductType.objects.get_or_create(Code=code, Name=name, EnglishName=englishname, SeqNumber=num)[0]
    return c


def add_productcontent(typeid, producttype, title):
    p = ProductContent.objects.get_or_create(TypeID=typeid, ProductType=producttype, Title=title, IsPublish=True,
                                             Content=" ")[0]
    return p


def add_leaguecontent(contentType, title, seq):
    c = LeagueContent.objects.get_or_create(ContentType=contentType, Title=title, SeqNumber=seq, IsPublish=True)[0]
    return c


def add_plantype(code, name, englishname, num):
    c = PlanType.objects.get_or_create(Code=code, Name=name, EnglishName=englishname, SeqNumber=num)[0]
    return c


def add_plancontent(typeid, producttype, title):
    p = \
    PlanContent.objects.get_or_create(TypeID=typeid, ProductType=producttype, Title=title, IsPublish=True, Content=" ")[
        0]
    return p


def add_casetype(code, name):
    c = CaseType.objects.get_or_create(Code=code, Name=name)[0]
    return c


# Start execution here!
if __name__ == '__main__':
    print u"开始初始化数据..."
    createuser()
    populate()
    print u"完成初始化数据."
