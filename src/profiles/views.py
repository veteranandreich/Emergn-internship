from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import ProfileForm
from accounts.models import User


class ProfileList(LoginRequiredMixin, ListView):
    template_name = 'profiles/index.html'
    context_object_name = 'profiles_list'

    def get_queryset(self):
        return User.objects.all()


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'profiles/form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profiles:index')

