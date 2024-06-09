from typing import Any

from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView

from users.forms import LoginForm, SignupForm
from users.models import CustomUser


# Create your views here.
class SignupView(CreateView):
    template_name = "users/signup.html"
    form_class = SignupForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        user = form.save()
        user.save()
        login(request, user)
        return redirect("chat")


class LoginView(ListView):
    template_name = "users/login.html"
    form_class = LoginForm
    model = CustomUser

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(data=request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})

        user = authenticate(
            request,
            email=form.cleaned_data.get("email"),
            password=form.cleaned_data.get("password"),
        )
        if not user:
            return render(request, self.template_name, {"form": form})
        login(request, user)
        return redirect("chat")
