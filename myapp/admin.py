from django.contrib import admin
from .models import UserModel, ShopModel, BranchModel, ProductModel, CheckModel, InstallmentModel


admin.site.register(UserModel)
admin.site.register(ShopModel)
admin.site.register(BranchModel)
admin.site.register(ProductModel)
admin.site.register(CheckModel)
admin.site.register(InstallmentModel)