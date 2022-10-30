from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

"""


Automagically doesn't sound like something django would do by default. It wouldn't force you to require a timestamp.

I'd build an abstract base class and inherit all models from it if you don't want to forget about the timestamp / fieldname, etc.

class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add=True)

     class Meta:
         abstract = True
"""
# Create your models here.

ONLINE_CUSTOMER_REGISTRATION_STATUS = (
    ('registered', 'Registered'),
    ('inprogress', 'In-Progress'),
    ('rejected', 'Rejected'),
    ('accepted', 'Accepted'),
    ('hold', 'In-Hold'),
)


class Customer(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', verbose_name='ID')
    cust_firstname = models.CharField(blank=False, max_length=20, null=False, db_column='cust_firstname',
                                      verbose_name='First Name')
    cust_lastname = models.CharField(blank=False, max_length=20, null=False, db_column='cust_lastname',
                                     verbose_name='Last Name')
    cust_email = models.CharField(blank=False, max_length=50, null=False, db_column='cust_email',
                                  verbose_name='Email Id')
    cust_phone = models.CharField(blank=False, max_length=20, null=False, db_column='cust_phone', verbose_name='Phone')
    cust_status = models.CharField(max_length=15, choices=ONLINE_CUSTOMER_REGISTRATION_STATUS, default='registered',
                                   db_column='cust_status', verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_column="created_at")

    class Meta:
        db_table = 'customer'
        verbose_name_plural = "Customer"

    def __str__(self):
        return f"{self.cust_firstname},{self.cust_lastname}"


class VendorRegistration(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', verbose_name='ID')
    first_name = models.CharField(blank=False, max_length=20, null=False, db_column='first_name',
                                  verbose_name='First Name')
    last_name = models.CharField(blank=False, max_length=20, null=False, db_column='last_name',
                                 verbose_name='Last Name')
    company = models.CharField(blank=False, max_length=100, null=False, db_column='company',
                               verbose_name='Company Name')
    created_date = models.DateField(auto_now_add=True, blank=True, null=True, db_column='created_date',
                                    verbose_name='Created Date', editable=True)
    company_phone = models.CharField(blank=False, max_length=15, null=False, db_column='company_phone',
                                     verbose_name='Company Phone')
    company_email = models.CharField(blank=False, max_length=50, null=False, db_column='company_email',
                                     verbose_name='Company Email')

    class Meta:
        db_table = 'vendor_registration'
        ordering = ['first_name']
        verbose_name_plural = 'Vendor Registration'


class VendorRegistrationFollowUp(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    vendor_id = models.ForeignKey(VendorRegistration, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    primary_no = models.CharField(max_length=15)
    secondary_no = models.CharField(max_length=15)
    company_email_id = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50, blank=True, null=True, db_column='company_name',
                                    verbose_name='Company Name')
    content = models.CharField(max_length=500)
    website_url = models.CharField(max_length=40)
    product = models.CharField(max_length=100)
    reference = models.CharField(max_length=20)
    prod_specialize = models.CharField(blank=False, max_length=500, null=False, db_column='prod_specialize',
                                       verbose_name='Product Specialize')
    prod_price_range = models.CharField(blank=False, max_length=50, null=False, db_column='prod_price_range',
                                        verbose_name='Price Range')
    company_gst = models.CharField(blank=False, max_length=500, null=False, db_column='company_gst', verbose_name='GST')

    comments = models.CharField(max_length=200)
    created_by = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.CharField(max_length=50)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'vendor_reg_follow_ups'
        verbose_name_plural = 'Vendor Registration Follow Up'


class Vendor(models.Model):
    id = models.PositiveIntegerField(primary_key=True, help_text='unique Id auto generates')
    first_name = models.CharField(blank=False, max_length=20, null=False, verbose_name='First Name',
                                  help_text='Vendor First Name')
    middle_name = models.CharField(blank=True, max_length=20, null=True, verbose_name='Middle Name',
                                   help_text='Vendor MMiddle Name')
    last_name = models.CharField(blank=False, max_length=20, null=False, verbose_name='Last Name',
                                 help_text='Vendor Last Name')
    contact_no = models.CharField(blank=False, max_length=15, null=False, verbose_name='Contact No',
                                  help_text='Vendor Contact Number')
    email_id = models.CharField(blank=False, max_length=50, null=False, verbose_name='Email Account',
                                help_text='Vendor Email Account eg:myemail@gamail.com')
    company = models.CharField(blank=False, max_length=100, null=False, verbose_name='Company Name',
                               help_text='Vendor Company Name')
    content = models.TextField(blank=True, max_length=500, null=True, verbose_name='Description',
                               help_text='Company Information')
    website_url = models.CharField(blank=False, max_length=100, null=False, verbose_name='Web URL',
                                   help_text='Company website URL')
    created_by = models.CharField(help_text='Employee created the record', db_column='created_by', max_length=50)
    created_date = models.DateField(blank=True, null=True, verbose_name='Created Date', help_text='Published Date',
                                    default=date.today)
    updated_by = models.CharField(help_text='Modified by employee details', db_column='updated_by', max_length=50)
    updated_date = models.DateField(blank=True, null=True, verbose_name='Updated Date', help_text='Last updated date')
    company_phone = models.CharField(blank=False, max_length=15, null=False, verbose_name='Company Phone',
                                     help_text='company phone number')
    company_email = models.CharField(blank=False, max_length=50, null=False, verbose_name='Company Email',
                                     help_text='company email account')
    product = models.CharField(blank=False, max_length=50, null=False, verbose_name='Product', help_text='Product Name')
    prod_specialize = models.CharField(blank=False, max_length=500, null=False, verbose_name='Product Specialize',
                                       help_text='Product Specialize details')
    prod_price_range = models.CharField(blank=False, max_length=50, null=False, verbose_name='Price Range',
                                        help_text='Product Price Rande details')
    company_gst = models.CharField(blank=False, max_length=500, null=False, verbose_name='GST',
                                   help_text='company GST details')

    class Meta:
        db_table = 'vendor'
        ordering = ['first_name']
        verbose_name_plural = 'Vendor Master'


class VendorMasterFollowUps(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, help_text='unique Id auto generates', db_column='id')
    first_name = models.CharField(max_length=20, db_column='first_name', blank=False, null=False,
                                  help_text='Contact Person First Name')
    middle_name = models.CharField(max_length=20, db_column='middle_name', blank=True, null=True,
                                   help_text='Contact Person Middle Name')
    last_name = models.CharField(max_length=20, db_column='last_name', blank=False, null=False,
                                 help_text='Contact Person Last Name')
    primary_no = models.CharField(max_length=15, db_column='primary_no', blank=False, null=False,
                                  help_text='Contact Person primary contact number')
    secondary_no = models.CharField(max_length=15, db_column='secondary_no', blank=True, null=True,
                                    help_text='Contact Person secondary contact number')
    company_email_id = models.CharField(max_length=100, db_column='company_email_id', blank=False, null=False,
                                        help_text='Contact Person Email Account')
    company_name = models.CharField(max_length=30, db_column='company_name', blank=False, null=False,
                                    help_text='Contact Person Company Name')
    content = models.CharField(max_length=200, db_column='content', blank=True, null=True,
                               help_text='Contact Person Company Details')
    website_url = models.CharField(max_length=40, db_column='website_url', blank=False, null=False,
                                   help_text='Contact Person Company Website Link details')
    product = models.CharField(max_length=15, db_column='product', blank=False, null=False,
                               help_text='company product details')
    reference = models.CharField(max_length=20, db_column='reference', blank=True, null=True,
                                 help_text='Person reference detai')
    comments = models.CharField(max_length=200, db_column='comments', blank=True, null=False,
                                help_text='Contact Person primary contact number')
    created_by = models.CharField(max_length=50, help_text='employee created by', db_column='created_by')
    created_date = models.DateTimeField(blank=True, null=True, verbose_name='created Date', help_text='created date',
                                        db_column='created_date', default=datetime.now)
    updated_by = models.CharField(max_length=50, help_text='Employee updated by', db_column='updated_by')
    updated_date = models.DateTimeField(blank=True, null=True, verbose_name='Updated Date',
                                        help_text='Last updated date', db_column='updated_date', default=None)
    vendor_id = models.ForeignKey(to=Vendor, on_delete=models.CASCADE, blank=False, null=False, db_column='vendor_id',
                                  help_text='Vendor reference id')

    class Meta:
        db_table = 'vendor_follow_ups'
        ordering = ['id', 'first_name']
        verbose_name_plural = 'Vendor Master Follow Up'


class Product(models.Model):
    vendor_id = models.ForeignKey(to=Vendor, related_name='+', on_delete=models.CASCADE, db_column='vendor_id',
                                  blank=False, null=False, help_text='Vendor reference ID')
    id = models.AutoField(auto_created=True, primary_key=True, help_text='unique Id auto generates', db_column='id')
    type = models.CharField(max_length=100, db_column='type', blank=False, null=False, help_text='Product Type')
    status = models.BooleanField(db_column='status', help_text='Product Status', default=True)
    created_by = models.CharField(max_length=50, db_column='created_by', blank=False, null=False,
                                  help_text='Product Created by')
    created_date = models.DateTimeField(db_column='created_date', blank=False, null=False,
                                        help_text='Product created date')
    updated_by = models.CharField(max_length=50, db_column='updated_by', blank=False, null=False,
                                  help_text='Product updated by')
    updated_date = models.DateTimeField(max_length=20, db_column='updated_date', blank=False, null=False,
                                        help_text='Product last update date')

    class Meta:
        db_table = 'product'
        ordering = ['vendor_id', 'id']
        verbose_name_plural = 'Product Master'


class SubProduct(models.Model):
    product_id = models.ForeignKey(to=Product, related_name='+', on_delete=models.CASCADE, db_column='product_id',
                                   blank=False, null=False, help_text='Sub Product reference ID')
    id = models.AutoField(auto_created=True, primary_key=True, help_text='unique Id auto generates', db_column='id')
    sub_product_type = models.CharField(max_length=50, db_column='sub_product_type', blank=False, null=False,
                                        help_text='Sub Product Type')
    status = models.BooleanField(db_column='status', help_text='Sub Product Status', default=True)
    created_by = models.CharField(max_length=50, blank=False, null=False, help_text='Sub Product Created by')
    created_date = models.DateTimeField(db_column='created_date', blank=False, null=False,
                                        help_text='Sub Product created date')
    updated_by = models.CharField(max_length=50, db_column='updated_by', blank=False, null=False,
                                  help_text='Sub Product updated by')
    updated_date = models.DateTimeField(max_length=20, db_column='updated_date', blank=False, null=False,
                                        help_text='Sub Product last update date')

    class Meta:
        db_table = 'sub_product'
        ordering = ['product_id', 'id', 'sub_product_type']
        verbose_name_plural = 'Sub Products'


class ProductCategory(models.Model):
    product_id = models.ForeignKey(to=Product, related_name='+', on_delete=models.CASCADE, db_column='product_id',
                                   blank=False, null=False, help_text='Category Product reference ID')
    id = models.AutoField(auto_created=True, primary_key=True, help_text='unique Id auto generates', db_column='id')
    category_type = models.CharField(max_length=50, db_column='category_type', blank=False, null=False,
                                     help_text='Category Type')
    status = models.BooleanField(db_column='status', help_text='Category Status', default=True)
    created_by = models.CharField(max_length=50, db_column='created_by', blank=False, null=False,
                                  help_text='Product Created by')
    created_date = models.DateTimeField(db_column='created_date', blank=False, null=False,
                                        help_text='Category created date')
    updated_by = models.CharField(max_length=50, db_column='updated_by', blank=False, null=False,
                                  help_text='Category updated by')
    updated_date = models.DateTimeField(max_length=20, db_column='updated_date', blank=False, null=False,
                                        help_text='Category last update date')

    class Meta:
        db_table = 'product_category'
        ordering = ['product_id', 'id', 'category_type']
        verbose_name_plural = 'Product Category'


class Gender(models.Model):
    product_id = models.ForeignKey(to=Product, related_name='+', on_delete=models.CASCADE, db_column='product_id',
                                   blank=False, null=False, help_text='Gender reference ID')
    id = models.AutoField(auto_created=True, primary_key=True, help_text='unique Id auto generates', db_column='id')
    gender = models.CharField(max_length=10, db_column='gender', blank=False, null=False, help_text='gender')
    created_by = models.CharField(max_length=50, db_column='created_by', blank=False, null=False,
                                  help_text='Gender Created by')
    created_date = models.DateTimeField(db_column='created_date', blank=False, null=False,
                                        help_text='Gender created date')
    updated_by = models.CharField(max_length=50, db_column='updated_by', blank=False, null=False,
                                  help_text='Gender updated by')
    updated_date = models.DateTimeField(max_length=20, db_column='updated_date', blank=False, null=False,
                                        help_text='Gender last update date')

    class Meta:
        db_table = 'gender'
        ordering = ['product_id', 'id', 'gender']
        verbose_name_plural = 'Gender Master'
