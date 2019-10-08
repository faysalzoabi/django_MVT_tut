from django.urls import path
from .views import list_posts, post_detail, post_create, post_update, post_delete

urlpatterns = [
    path('', list_posts),
    path('create/', post_create),
    path('<id>/', post_detail),
    path('<id>/update/', post_update),
    path('<id>/delete/', post_delete)
    
]
