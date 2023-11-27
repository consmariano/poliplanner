from django.views.generic import View
from django.shortcuts import render, redirect

from professor.forms import SignUpForm


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
