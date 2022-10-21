from django.contrib import admin
from .models import Weight_distribution,Customer_Type,Product_Service,Juridictional_Risk,List_Matching,Profile_linkage,Transaction_Behavior
# Register your models here.
admin.site.register(Weight_distribution)
admin.site.register(Customer_Type)
admin.site.register(Product_Service)
admin.site.register(Juridictional_Risk)
admin.site.register(List_Matching)
admin.site.register(Profile_linkage)
admin.site.register(Transaction_Behavior)