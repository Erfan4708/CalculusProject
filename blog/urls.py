from django.urls import path
from .views import PostList, post_detail, add_favorite , FavoriteList
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('add_favorite/<str:user>/<int:post_id>', add_favorite, name='add_favorite'),
    # path('rem_favorite/<int:pk>/',remove_favorite,name='rem_favorite'),
    path('favorite-list/' , FavoriteList.as_view() , name ='favorite_list' ),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
