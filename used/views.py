from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    def get(self, request):
        return render(request,'index.html')

class AddDonationView(View):
    def get(self, request):
        return render(request,'form.html')

class ConfirmationView(View):
    def get(self, request):
        return render(request,'form-confirmation.html')

class LoginView(View):
    def get(self, request):
        return render(request,'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request,'register.html')