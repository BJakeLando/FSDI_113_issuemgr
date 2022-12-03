from django.urls import path
from issues import views

urlpatterns = [
    path('', views.BoardView.as_view(), name='board'),
    path('<int:pk>', views.IssueDetailView.as_view(), name='issue_detail'),
    path('new/', views.IssueCreateView.as_view(), name='new_issue'),
    path('<int:pk>/edit/', views.IssueUpdateView.as_view(), name='edit_issue'),
    path('<int:pk>/delete/', views.IssueDeleteView.as_view(), name='delete_issue'),
    path('success/', views.SuccessView.as_view(), name='success'),
]