from django.conf.urls import url
from siteManager import  views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.homepage, name='homepage'),
    url(r'^joinus/$', views.joinus, name='joinus'),
    url(r'^joinus/(?P<id>\d+)/$', views.joinusdetail, name='joinusdetail'),
    url(r'^channel/$', views.channel, name='channel'),
    url(r'^case/$', views.case, name='case'),
    url(r'^detail/(?P<tabletype>\w+)/$', views.view_options, name='options'),
    url(r'^detail/(?P<tabletype>\w+)/(?P<typecode>\w+)/$', views.view_list, name='list'),
    url(r'^detail/(?P<tabletype>\w+)/(?P<typecode>\w+)/(?P<contentid>\d+)/$', views.view_detail, name='content'),
    url(r'^getcontent/$', views.getContent_Ajax, name='content_ajax'),
    url(r'^getcase/$', views.getCase_Ajax, name='case_ajax'),
    url(r'^getarea/$', views.getArea_Ajax, name='area_ajax'),
    url(r'^download/$', views.download, name='download_1'),
    url(r'^league/$', views.league, name='league'),
    url(r'^hero/$', views.getHero_Ajax, name='hero_ajax'),
    url(r'^leaguecontent/$', views.getLeagueContent_Ajax, name='leaguecontent_ajax'),
    url(r'^league/(?P<typecode>\w+)/$', views.view_leaguedetail, name='leaguedetail'),
    url(r'^joinusajax/$', views.getjoinus_Ajax, name='joinus_ajax'),

   url(r'^article/(?P<category>\w+)/$', views.view_article, name='article'),
   url(r'^about/$', views.view_about, name='about'),
   url(r'^article/(?P<category>\w+)/(?P<typecode>\w+)/(?P<contentid>\d+)/$', views.view_articledetail, name='articledetail'),
]

