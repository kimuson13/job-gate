from django.urls import path
from app import views

urlpatterns = [
    path('home', views.homeView.as_view(), name='home'),
    path('home/question-description', views.QuestionDescriptionView.as_view(), name='question_description'),
    path('home/elementary-school', views.ElementarySchoolView.as_view(), name='elementary-school'),
    path('home/junior-high-school', views.JuniorHighSchoolView.as_view(), name='junior-high-school'),
    path('home/high-school', views.HighSchoolView.as_view(), name='high-school'),
    path('home/university', views.UniversityView.as_view(), name='university'),
    # path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    # path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    # path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    # path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
