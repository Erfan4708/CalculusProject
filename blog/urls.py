from django.urls import path
from .views import PostList ,FavoriteList , post_detail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/',post_detail , name='post_detail'),
    path('favorite/', FavoriteList.as_view(), name='post_favorite'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
