from django.contrib import admin
from django.urls import path
from branches import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BankList.as_view(), name='bank-list'),
    path('banks/', views.BankList.as_view(), name='bank-list'),
    path('banks/<int:bank_id>/branches/', views.BankBranchesList.as_view(), name='bank-branches'),
    path('branches/<str:ifsc>/', views.BranchDetail.as_view(), name='branch-detail'),
]
