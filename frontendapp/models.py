from django.db import models
from datetime import date,datetime
class ApplyLeave(models.Model):
    leave_id = models.IntegerField(primary_key=True)
    employee = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    leave_reason = models.CharField(max_length=500, blank=True, null=True)
    leave_date = models.DateField(blank=True, null=True)
    leave_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apply_leave'



class BranchDetails(models.Model):
    branch_address = models.CharField(max_length=500, blank=True, null=True)
    total_payout = models.IntegerField(blank=True, null=True)
    total_number_of_employee = models.IntegerField(blank=True, null=True)
    branch = models.OneToOneField('BranchManager', models.DO_NOTHING, primary_key=True)
    head_manager = models.ForeignKey('HeadManager', models.DO_NOTHING)
    branch_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch_details'


class BranchManager(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    branch_manager_id = models.IntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=300, blank=True, null=True)
    contact_number = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch_manager'


class Calculation(models.Model):
    salary_id = models.IntegerField(primary_key=True)
    employee = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    allowance = models.IntegerField(blank=True, null=True)
    deduction = models.IntegerField(blank=True, null=True)
    total_calculated_salary = models.IntegerField(blank=True, null=True)
    working_hours = models.IntegerField(blank=True, null=True)
    total_leaves = models.IntegerField(blank=True, null=True)
    branch = models.ForeignKey(BranchManager, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calculation'




class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    working_hours = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    job_type = models.CharField(max_length=300, blank=True, null=True)
    contact_number = models.BigIntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    total_leaves = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeLeaveManagement(models.Model):
    leave_id = models.IntegerField(primary_key=True)
    employee_id = models.IntegerField(blank=True, null=True)
    leave_reason = models.CharField(max_length=500, blank=True, null=True)
    leave_date = models.DateField(blank=True, null=True)
    leave_status = models.CharField(max_length=500, blank=True, null=True)
    branch = models.ForeignKey(BranchManager, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_leave_management'


class GeneralService(models.Model):
    general_service_id = models.IntegerField(blank=True, null=True)
    expenses = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    branch = models.ForeignKey(BranchManager, models.DO_NOTHING, blank=True, null=True)
    PK = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'general_service'


class HeadManager(models.Model):
    head_manager_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    head_branch_address = models.CharField(max_length=500, blank=True, null=True)
    head_branch_id = models.IntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=300, blank=True, null=True)
    contact_number = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'head_manager'


class Login(models.Model):
    user_id = models.IntegerField(primary_key=True)
    password = models.CharField(db_column='PASSWORD', max_length=30)  # Field name made lowercase.
    role = models.CharField(db_column='ROLE', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'login'


class PastUserRecords(models.Model):
    employee = models.OneToOneField('Resignation', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    working_hours = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    job_type = models.CharField(max_length=300, blank=True, null=True)
    contact_number = models.BigIntegerField(blank=True, null=True)
    leaving_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    total_leaves = models.IntegerField(blank=True, null=True)
    branch = models.ForeignKey(BranchManager, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'past_user_records'


class ProductDetails(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    branch = models.ForeignKey(BranchManager, models.DO_NOTHING, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    PK = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'product_details'


class Resignation(models.Model):
    employee = models.OneToOneField(Employee, models.DO_NOTHING, primary_key=True)
    resign_reason = models.CharField(max_length=500, blank=True, null=True)
    resign_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resignation'