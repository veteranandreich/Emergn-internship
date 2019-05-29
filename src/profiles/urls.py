from django.urls import path

from .views import ProfileList, ProfileUpdate

app_name = 'notes'

urlpatterns = [
    path('', ProfileList.as_view(), name='index'),
    path('<int:pk>/edit/', ProfileUpdate.as_view(), name='update')
]