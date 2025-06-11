from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationFrom


class SignUpView(CreateView):
    """Sign up View"""

    form_class = CustomUserCreationFrom
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
