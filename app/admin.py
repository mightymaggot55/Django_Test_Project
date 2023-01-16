from django.contrib import admin
from app.models import Department, Ticket, Asset, Staff


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['staff_member', 'submission_date', 'issue_summary', 'issue_description', 'status', 'staff_assigned']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staff_member', 'department', 'email']


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['current_user', 'user_name', 'computer_id', 'serial_no']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department']
