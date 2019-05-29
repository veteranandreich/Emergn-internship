from django.views.generic import RedirectView
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Handle the root url.
    path('', RedirectView.as_view(url='profiles/'), name='index'),

    # Accounts app
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # Profiles app
    path('profiles/', include('profiles.urls', namespace='profiles')),

    # Admin
    path('admin/', admin.site.urls),
]