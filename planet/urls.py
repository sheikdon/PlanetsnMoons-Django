from django.urls import path
from .views import InnersView, InnersDetailViews

urlpatterns = [
    path('', InnersView.as_view(), name='inners'),
    path('<int:pk>/', InnersDetailViews.as_view(), name='Inner')

]