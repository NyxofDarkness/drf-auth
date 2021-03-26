from django.urls import path
from .views import OpinionList, OpinionDetail

urlpatterns = [
   path("<int:pk>/", OpinionDetail.as_view()),
   path("", OpinionList.as_view()),
]
