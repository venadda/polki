from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from vendor.models import (Customer, VendorRegistration, VendorRegistrationFollowUp,
                           Vendor, VendorMasterFollowUps, Product, SubProduct, ProductCategory, Gender)

admin.site.site_header = "Polki-Dolki Admin"
admin.site.site_title = "Polki-Dolki Admin Portal"
admin.site.index_title = "Welcome to Polki-Dolki  Portal"
# Register your models here.
'''
@admin.action(description='Customer Enquire been registered')
    def make_published(self, request, queryset):
        queryset.update(cust_status='registered')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
'''


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'cust_firstname', 'cust_lastname', 'cust_email', 'cust_phone']
    ordering = ['id']

    def make_published(self, request, queryset):
        self.message_user(request, ngettext(
            'story was successfully marked as published.',
            ' stories were successfully marked as published.',
        ), messages.SUCCESS)


admin.site.register(Customer, CustomerAdmin)


class VendorRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'company', 'company_phone', 'company_email', 'created_date']
    ordering = ['id', 'first_name', 'last_name']


admin.site.register(VendorRegistration, VendorRegistrationAdmin)


class OnlineRegistrationFollowUpAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendor_id', 'first_name', 'middle_name', 'last_name', 'primary_no', 'secondary_no',
                    'company_email_id', 'company_name', 'content', 'website_url', 'product', 'reference', 'comments',
                    'created_at']
    ordering = ['id', 'vendor_id']


admin.site.register(VendorRegistrationFollowUp, OnlineRegistrationFollowUpAdmin)


class VendorMasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'middle_name', 'last_name', 'contact_no', 'email_id', 'company', 'content',
                    'website_url', 'company_phone', 'company_email', 'product', 'prod_specialize', 'prod_price_range',
                    'company_gst']
    ordering = ['id']


admin.site.register(Vendor, VendorMasterAdmin)


class VendorMasterFollowUpAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendor_id', 'first_name', 'middle_name', 'last_name', 'primary_no', 'secondary_no',
                    'company_email_id', 'company_name', 'content', 'website_url', 'product', 'reference', 'comments']
    ordering = ['id', 'vendor_id']


admin.site.register(VendorMasterFollowUps, VendorMasterFollowUpAdmin)

# class ProducctAdmin(admin.ModelAdmin):
#     list_display = ['id','vendor_id','type','status']
#     ordering = ['id','vendor_id']
# admin.site.register(Product, ProducctAdmin)
#
# class SubProductAdmin(admin.ModelAdmin):
#     list_display = ['id','product_id','sub_product_type','status']
#     ordering = ['id','product_id']
# admin.site.register(SubProduct, SubProductAdmin)
#
# class ProductCategroyAdmin(admin.ModelAdmin):
#     list_display = ['id','product_id','category_type','status']
#     ordering = ['id','product_id']
# admin.site.register(ProductCategory, ProductCategroyAdmin)
#
# class GenderMasterAdmin(admin.ModelAdmin):
#     list_display = ['id','product_id','gender']
#     ordering = ['id','product_id']
# admin.site.register(Gender, GenderMasterAdmin)
#
#
