from django.conf.urls import url
from . import views

app_name = 'quill'

urlpatterns = [
    # 처음 텍스트 에디터 접속 page - post 새로 생성 (저장 or 발행)
    url('^write/$', views.write, name='write'),  # /write/

    # 저장된 post_list page
    url('^ready/$', views.ready_list, name='ready_list'),  # /ready/

    # 발행된 post_list page
    url('^published/$', views.published_list, name='published_list'),  # /published/

    # post_detail page
    url('^(?P<username>\w+)/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),  # /username/1/

    # post_edit page - 기존의 post 수정
    url('^(?P<username>\w+)/(?P<pk>\d+)/write/$', views.post_edit, name='post_edit'),  # /username/1/write
]
