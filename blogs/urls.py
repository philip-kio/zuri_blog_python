from django.urls import path
from . views import BlogDeleteView, BlogListView,BlogDetailView,BlogCreateView, BlogUpdateView\
                    ,SignUpView, CommentFormView



urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('new_post/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name= 'delete_post'),
    path('signup/',SignUpView.as_view(), name='signup'),
    path('post/<int:pk>/comment/', CommentFormView.as_view(), name='add_comment'),

]