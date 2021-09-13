from django.urls import path
from Mixins_app import views

urlpatterns = [
    path('emp/',views.EmpListView.as_view()),
    path('emp/<int:pk>/',views.EmpDetailView.as_view()),

]