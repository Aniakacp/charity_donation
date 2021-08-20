from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView,ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json


from accounts.forms import LoginForm, RegisterForm
from used.forms import AdressForm, CategoryForm, CollectForm, InstitutionForm, BagsForm
from used.models import Institution, Donation, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from used.permission_mixin import MyTestUserPassesTest

class LandingPageView(View):
    def get(self, request):
        foundations = Institution.objects.all().filter(type=1)
        non_gov_organizations = Institution.objects.all().filter(type=2)
        collections = Institution.objects.all().filter(type=3)
        all_institutions_= Institution.objects.all().count()
        all_institutions=Donation.objects.all().distinct('institution').count()
        all_donations = Donation.objects.all().count()
        paginate_by = 2

        foundations_paginator = Paginator(foundations.order_by('categories'), paginate_by)  # Show 2 contacts per page

        page = request.GET.get('page', 1)
        page_obj= foundations_paginator.get_page(page)

        try:
            founds = foundations_paginator.page(page)
        except PageNotAnInteger:
            founds = foundations_paginator.page(1)
        except EmptyPage:
            founds = foundations_paginator.page(foundations_paginator.num_pages)

        return render(request,'index.html', {'foundations': foundations, 'non_gov_organizations':non_gov_organizations,
                                             'collections': collections, 'all_institutions': all_institutions,
                                             'all_donations':all_donations, 'founds': founds, 'page_obj':page_obj })

class AddDonationView(MyTestUserPassesTest, View):
    def get(self, request):
        category_form= CategoryForm()
        address_form = AdressForm()
        collect_form= CollectForm()
        instutution_form= InstitutionForm()
        bags_form=BagsForm()
        return render(request,'form.html', {'address_form':address_form, 'category_form':category_form, 'collect_form':collect_form, 'instutution_form':instutution_form, 'bags_form':bags_form})

    def post(self, request):
        category_form = CategoryForm(request.POST)
        address_form = AdressForm(request.POST)
        collect_form = CollectForm(request.POST)
        instutution_form= InstitutionForm(request.POST)
        bags_form = BagsForm(request.POST)
        if category_form.is_valid():
            categories = category_form.cleaned_data['name']
            selected_industries= Institution.objects.filter(categories__in= categories).distinct('name')
            json_dict= {'istitution': []}
            for industry in selected_industries:
                json_dict['istitution'].append({'selected': industry.name})
            print(json_dict)
            send_json(json_dict)
            # {'istitution': [{'selected': 'Children'}, {'selected': 'European Decent Life'}, {'selected': 'Garage charaty event'}, {'selected': 'new found'}]}

        if category_form.is_valid() and address_form.is_valid() and collect_form.is_valid() and instutution_form.is_valid() and bags_form.is_valid():

            categories = category_form.cleaned_data['name'] # <QuerySet [<Category: AGD>, <Category: Toys>]>

            quantity = bags_form.cleaned_data['bags']
            institution = instutution_form.cleaned_data['radio']
            address = address_form.cleaned_data['street']
            phone_number = address_form.cleaned_data['phone']
            city = address_form.cleaned_data['city']
            zip_code = address_form.cleaned_data['post_code']
            pick_up_date = collect_form.cleaned_data['date']
            pick_up_time = collect_form.cleaned_data['time']
            pick_up_comment = collect_form.cleaned_data['notes']
            user = request.user
            Donation.objects.create(quantity=quantity, institution=institution, address=address, phone_number=phone_number, city=city, zip_code=zip_code,
                                    pick_up_date=pick_up_date, pick_up_time=pick_up_time, pick_up_comment=pick_up_comment, user=user).categories.set(categories)
            return redirect('confirmation')

        return render(request, 'form.html', {'address_form':address_form, 'category_form':category_form, 'collect_form':collect_form, 'instutution_form':instutution_form, 'bags_form':bags_form})

class ConfirmationView(View):
    def get(self, request):
        return render(request,'form-confirmation.html')

class LoginView(View):
    def get(self, request):
        form=LoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
            else:
                return redirect('register')
            return redirect('index')
        return render(request, 'login.html', {'form': form})

class RegisterView(CreateView):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid() :
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class SettingsView(MyTestUserPassesTest, View):
    def get(self, request):
        return render(request, 'settings.html')

class SelectedInstitutionView(View):
    def get(self, request):
        selected_institutions= Institution.objects.filter(name='Restaurant For a Day')
        return JsonResponse({selected_institutions: selected_institutions})


def send_json(json_dict):
   # pass
    return JsonResponse(json_dict)
    #return HttpResponse(json.dumps(json_dict), mimetype="application/json")

class CatView(MyTestUserPassesTest, View):
    def post(self, request):
        category_form= CategoryForm()

        if category_form.is_valid():
            categories = category_form.cleaned_data['name']
            selected_industries= Institution.objects.filter(categories__in= categories).distinct('name')
            json_dict= {'istitution': []}
            for industry in selected_industries:
                json_dict['istitution'].append({'selected': industry.name})
            print(json_dict)

        return JsonResponse(json_dict)