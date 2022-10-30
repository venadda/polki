from django.shortcuts import render,redirect
from siteapp.forms import CustomerRegistrationForm,VendorRegistrationForm
from vendor.models import VendorRegistration,Customer
from django.views.generic import ListView, CreateView
from django.contrib import messages
# Create your views here.
class home(CreateView):
    template_name = "welcome.html"

    def get(self, request, *args, **kw):
        c_ob = Customer()
        self.customer = CustomerRegistrationForm(instance = c_ob)
        v_ob = VendorRegistration()
        self.vendor = VendorRegistrationForm(instance=v_ob)
        return render(request, self.template_name, {'customer':self.customer,'vendor':self.vendor,'msg':''})

    def post(self, request, *args, **kw):
        print(request.POST)
        if request.POST.get('customer_submit') != None:
            try:

                cust = Customer()
                cust.cust_lastname = request.POST.get('cust_lastname')
                cust.cust_firstname = request.POST.get('cust_firstname')
                cust.cust_email = request.POST.get('cust_email')
                cust.cust_phone = request.POST.get('cust_phone')
                cust.cust_status = 'registered'
                cust.save()
                messages.success(request, 'Contact request submitted successfully.')
            except Exception as e:
                messages.error(request, 'Invalid form submission.')
                messages.error(rquest,form.errors)
                print('err',e)
        if request.POST.get('vendor_submit') != None:

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            company = request.POST.get('company')
            company_email = request.POST.get('company_email')
            company_phone = request.POST.get('company_phone')
            obj = VendorRegistration()
            obj.company = company
            obj.company_email = company_email
            obj.company_phone = company_phone
            obj.first_name = first_name
            obj.last_name = last_name
            obj.save()
            # try:
            #     if obj.is_valid():
            #         obj.save()
            #     else:
            #         print('insufficient')
            # except Exception as e :
            #     print("error",e)

        return redirect("home")

def disclaimer(request):
    return render(request,'disclaimer.html',{})
def termsConditions(request):
    return render(request,'terms_conditions.html',{})
def codeOfEthics(request):
    return render(request,'codeofethics.html',{})