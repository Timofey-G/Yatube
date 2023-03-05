from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

from .forms import CreationForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("posts:index")
    template_name = "users/signup.html"


class UserUpdateView(UpdateView):
    model = User
    fields = (
        "first_name",
        "last_name",
        "username",
        "email",
        "profile_picture",
    )
    success_url = "/"

    def get_object(self):
        obj = super().get_object()
        if obj != self.request.user:
            raise PermissionDenied()
        return obj
