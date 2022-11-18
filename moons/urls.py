from django.urls import path
from .views import OutersView, OutersDetailViews

urlpatterns = [
    path('', OutersView.as_view(), name='outers'),
    path('<int:pk>/', OutersDetailViews.as_view(), name='Outer')

]