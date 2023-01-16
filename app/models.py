from django.db import models
from django.contrib.auth import authenticate

# Create your models here.
class Ticket(models.Model):
    STATUS = (('0', 'Not Started'),
              ('1', 'In Progress'),
              ('2', 'Finished'),
              ('3', 'Aborted'))
    # I have changed the related name to stf and stf_assigned as it didn't like having related_name = model name

    staff_member = models.ForeignKey('Staff', null=False, related_name='stf_member', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now=True)
    issue_summary = models.CharField(max_length=70)
    issue_description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS, blank=True)
    staff_assigned = models.ForeignKey('Staff', null=False, related_name='stf_assigned', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.issue_summary


class Staff(models.Model):
    staff_member = models.CharField(max_length=80)
    department = models.ForeignKey('Department', null=False, on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'staff'

    def __str__(self):
        return self.staff_member


class Asset(models.Model):
    current_user = models.ForeignKey('Staff', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=60)
    computer_id = models.CharField(max_length=60)
    serial_no = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.current_user


class Department(models.Model):
    department = models.CharField(max_length=40)

    def __str__(self):
        return self.department



