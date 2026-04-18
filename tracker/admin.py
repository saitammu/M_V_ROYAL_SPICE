from django.contrib import admin
from .models import (Vendor, SubCategory, DailyEntry, DailyFinance,
                     Staff, StaffPayment, IncentiveName, DailyIncentive, VendorPayment)

admin.site.register(Vendor)
admin.site.register(SubCategory)
admin.site.register(DailyEntry)
admin.site.register(DailyFinance)
admin.site.register(Staff)
admin.site.register(StaffPayment)
admin.site.register(IncentiveName)
admin.site.register(DailyIncentive)
admin.site.register(VendorPayment)
