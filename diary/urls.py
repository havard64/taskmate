from django.urls import path
from diary import views
from django.conf.urls import url


urlpatterns = [
    path('', views.diary, name='diary'),
    path('log', views.log, name='log'),
    path('delete/<pk>', views.diary_delete, name='diary_delete'),
    path('edit/<pk>', views.diary_edit, name='diary_edit'),
#    path('diary_edit/<daypk>', views.diary_edit, name='diary_edit'),

    #    url(r'^diary_edit/(?P<pk>)/$', views.diary_edit, name='diary_edit')
]

# r'^diary_edit/(?P<pk>+)/$'