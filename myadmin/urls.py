from django.urls import path, include
from myadmin.views import *
from myadmin.sys_mgr_view import *
from myadmin.jingdian_mgr_view import *
from myadmin.wenzh_mgr_view import *
from myadmin.tongji_count_view import *
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
    path('qxgl/', QxglView.as_view()),
    # path('zsfj/', ZsfjView.as_view()),
    path('xttz/', XttzView.as_view()),
    path('order/', OrderInfoiew.as_view()),
    # path('jygl/', JyglView.as_view()),
    path('wzgl/', WzglView.as_view()),
    path('wzpl/', WzplView.as_view()),
    path('lunbt/', LunbtView.as_view()),
    path('user_count/', UserCountView.as_view()),
    path('view_count/', ScenicView.as_view()),
    # path('jdtj/', OrderView.as_view()),
    path('order_count/', OrderView.as_view()),
    path('yhquan/', YhquanView.as_view()),
    path('jifen/', JifenView.as_view()),


]