from django import forms
from django.forms import ModelForm
from vendor.models import  VendorRegistration,Customer
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import User


class CustomerRegistrationForm(ModelForm):
    id = forms.CharField(label='ID', widget=forms.TextInput(
        attrs={'class':"form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill", 'required':False}),required=False)
    cust_firstname=forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': True}), required=True)
    cust_lastname=forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': True}), required=False)
    cust_email=forms.CharField(label='Email', widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': True}), required=False)
    cust_phone=forms.CharField(label='Phone', widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': True}), required=False)
    class Meta:
        model = Customer
        fields = ['id','cust_firstname','cust_lastname','cust_email','cust_phone']

class VendorRegistrationForm(ModelForm):
    id = forms.CharField(label='ID',widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': False}), required=False)
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': True}), required=True)
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': True}), required=True)
    company_email = forms.CharField(label='Company Email',widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': True}), required=True)
    company_phone = forms.CharField(label='Company Phone', widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': True}), required=True)
    company = forms.CharField(label='Company Name',widget=forms.TextInput(
        attrs={
            'class': "form-control  mx-auto text-dark border-top-0 border-bottom-0 border border-right-0 border-danger bg-light rounded-pill",
            'required': True}), required=True)
    class Meta:
        model = VendorRegistration
        fields = ['id','first_name','last_name','company_email','company_phone','company']