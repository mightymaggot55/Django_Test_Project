from rest_framework import viewsets
from .serializers import TicketSerializer, StaffSerializer, AssetSerializer, DepartmentSerializer
from app.models import Department, Ticket, Staff, Asset


# retrieves all data from Ticket and sends it to the ticket serializer
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    # Needed to return an instance from data
    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.staff_member = validated_data.get('staff_member', instance.staff_member)
        instance.submission_date = validated_data.get('submission_date', instance.submission_date)
        instance.issue_summary = validated_data.get('issue_summary', instance.issue_summary)
        instance.issue_description = validated_data.get('issue_descripiton', instance.issue_descripiton)
        instance.ticket_status = validated_data.get('ticket_status', instance.ticket_status)
        instance.staff_assigned = validated_data.get('staff_assigned', instance.staff_assigned)
        instance.save()
        return instance


# retrieves all data from Staff and sends it to the staff serializer
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('staff_member')
    serializer_class = StaffSerializer

    # Needed to return an instance from data
    def create(self, validated_data):
        return Staff.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.staff_member = validated_data.get('staff_member', instance.staff_member)
        instance.department = validated_data.get('department', instance.department)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


# retrieves all data from user and sends it to the Asset serializer
class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def create(self, validated_data):
        return Asset.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.current_user = validated_data.get('current_user', instance.current_user)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.computer_id = validated_data.get('computer_id', instance.computer_id)
        instance.serial_no = validated_data.get('serial_no', instance.serial_no)
        instance.save()
        return instance


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.department = validated_data.get('department', instance.department)
        instance.save()
        return instance
