from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
import random

from used.models import Institution, Donation
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class LandingPageView(View):
    def get(self, request):
        foundations = Institution.objects.all().filter(type=1)
        non_gov_organizations = Institution.objects.all().filter(type=2)
        collections = Institution.objects.all().filter(type=3)
        all_institutions= Institution.objects.all().count()
        all_donations = Donation.objects.all().count()

        paginator = Paginator(foundations.order_by('categories'), 2)  # Show 2 contacts per page
        page = request.GET.get('page', 1)

        print(foundations.count()//paginator.num_pages)  # ile pelnych stron
        print(foundations.count() % paginator.num_pages) # ile dodatkowo

        try:
            founds = paginator.page(page)
        except PageNotAnInteger:
            founds = paginator.page(1)
        except EmptyPage:
            founds = paginator.page(paginator.num_pages)

        return render(request,'index.html', {'foundations': foundations, 'non_gov_organizations':non_gov_organizations, 'collections': collections, 'all_institutions': all_institutions, 'all_donations':all_donations, 'founds': founds  })

class AddDonationView(View):
    def get(self, request):
        return render(request,'form.html')

class ConfirmationView(View):
    def get(self, request):
        return render(request,'form-confirmation.html')

class LoginView(View):
    def get(self, request):
        return render(request,'login.html')

class RegisterView(CreateView):
    def get(self, request):
        return render(request, 'register.html')
