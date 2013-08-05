from django.conf.urls import patterns, include, url
#from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buglist.views.home', name='home'),
    # url(r'^buglist/', include('buglist.foo.urls')),

    url(r'^mine/$', 'buglist.views.view_list',{'list_slug':'mine'},name="buglist-mine"),
    url(r'^(?P<list_id>\d{1,4})/(?P<list_slug>[\w-]+)/delete$', 'buglist.views.del_list',name="buglist-del_list"),
    url(r'^task/(?P<task_id>\d{1,6})$', 'buglist.views.view_task', name='buglist-task_detail'),
    url(r'^(?P<list_id>\d{1,4})/(?P<list_slug>[\w-]+)$', 'buglist.views.view_list', name='buglist-incomplete_tasks'),
    url(r'^(?P<list_id>\d{1,4})/(?P<list_slug>[\w-]+)/completed$', 'buglist.views.view_list', {'view_completed':1},name='buglist-completed_tasks'),
    url(r'^add_list/$', 'buglist.views.add_list',name="buglist-add_list"),
    url(r'^search/$', 'buglist.views.search',name="buglist-search"),
    url(r'^$', 'buglist.views.list_lists',name="buglist-lists"),

    # View reorder_tasks is only called by JQuery for drag/drop task ordering   
    url(r'^reorder_tasks/$', 'buglist.views.reorder_tasks',name="buglist-reorder_tasks"),

    url(r'^ticket/add/$', 'buglist.views.external_add',name="buglist-external-add"), 
    
    url(r'^recent/added/$', 'buglist.views.view_list',{'list_slug':'recent-add'},name="buglist-recently_added"),
    url(r'^recent/completed/$', 'buglist.views.view_list',{'list_slug':'recent-complete'},name="buglist-recently_completed"),

    url(r'^bugapp/', include('buglist.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
