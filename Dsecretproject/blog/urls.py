<<<<<<< HEAD
from django.urls import path
from .views import *
from .templates import *

app_name = 'blog'

urlpatterns = [
    # REST
    path('list/', PostList.as_view(), name='post_list_api'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail_api'),

    # HTML웹
    path('page/', post_list_page, name='post_list_page'),
    path('create/', post_create_form, name='post_create_form'), 
    path('page/<int:pk>/', post_detail_page, name='post_detail_page'),
    path('page/<int:pk>/edit/', post_edit_form, name='post_edit_form'),
    path('page/<int:pk>/delete/', post_delete, name='post_delete'), 
]
=======
# from django.urls import path
# from .views import *

# app_name = 'blog'

# urlpatterns = [
    
# ]
>>>>>>> upstream/main
