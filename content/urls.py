from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# create a post/Update a post
# upload media
# view the post -post details/feed

# DETAILS:: every media will be uploaded individually
# DETAILS:: the post media won't be created until all the media are uploaded, \
#  the post object is create with no media/caption because it needed as reference
#  the get method to get the FEED /post/

#

router = DefaultRouter()
router.register('like', views.PostLikeViewSet, basename='post_like')
router.register('comment', views.PostCommentViewSet, basename='post_comment')

urlpatterns = [

    path('', views.UserPostCreateFeed.as_view(), name='user_post_view'),
    path('media/', views.PostMediaView.as_view(), name='post_media_view'),
    path('<int:pk>/', views.UserPostDetailsUpdateView.as_view(), name='post_details_update'),

    path('', include(router.urls))
]
