from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from professor.forms import SignInForm, SignUpForm


class SignInView(View):
    """ User registration view """

    template_name = "professor/signin.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            print("User:", user)  # Adicione esta linha
            if user:
                login(request, user)
                print("User authenticated successfully!")  # Adicione esta linha
                return redirect("calendarapp:calendar")
            else: 
                print("User authentication failed!")
        context = {"form": forms}
        return render(request, self.template_name, context)

class SignUpView(View):
    """ User registration view """

    template_name = "professor/signup.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("professor:signin")
        context = {"form": forms}
        return render(request, self.template_name, context)

def signout(request):
    logout(request)
    return redirect("professor:signin")
