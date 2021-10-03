from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


def home(request):
    return render(request, "base/home.html", {})


class RegisterUser(FormView):
    template_name = "base/register.html"
    success_url = reverse_lazy("base:home")
    redirect_authenticated_user = True
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("base:home")
        return super(RegisterUser, self).get(*args, **kwargs)


class LoginUser(LoginView):
    template_name = "base/login.html"
    redirect_authenticated_user = True
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse_lazy("base:home")
