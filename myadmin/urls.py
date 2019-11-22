from django.urls import path, include
from myadmin.views import *
from myadmin.sys_mgr_view import *
from myadmin.jdian_mgr_view import *
from myadmin.user_mgr_view import *
from myadmin.info_count_view import *
from myadmin.order_mgr_view import *

app_name = 'myadmin'

urlpatterns = [
    path('', index_view, name='index'),
    # path('regist/', regist_view, name='regist'),
    path('login/', to_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('role/', RoleView.as_view()),
    path('user/', UserView.as_view()),
    path('authority/', AuthorityView.as_view()),
    path('caidan/', CaidanView.as_view()),
    path('info/', InfoView.as_view()),
    path('pl/', PlView.as_view()),
    path('tj/', TjView.as_view()),
    path('zsfj/', ZsfjView.as_view()),
    path('jptj/', JptjView.as_view()),
    path('jygl/', JyglView.as_view()),
    path('wzgl/', WzglView.as_view()),
    path('wzpl/', WzplView.as_view()),
    path('user_count/', UserCountView.as_view()),
    path('order_count/', DingdCountiew.as_view()),
    path('jingdian_count/', DingdCountiew.as_view()),
    path('order_info/', OrderView.as_view()),
    path('yhquan/', YhquanView.as_view()),
    path('jifen/', JifenView.as_view()),


]