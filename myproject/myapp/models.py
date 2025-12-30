from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Students(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_age = models.IntegerField()
    stu_num = models.IntegerField()

# Models should be in the models page

# class Department(models.Model):
#     name = models.CharField(max_length=50)

# class Employee(models.Model):
#     name = models.CharField(max_length=50)
#     department = models.ForeignKey(Department, on_delete= models.CASCADE)

     #on_delete  (CASCADE) deletes the data from the main table along with foregin key table's data matching the department id of the main table --> the complete data will be deleted
     #i.e.,  If two employess belong to HR  foreign key table id =1, and 2 belongs to IT foreignkey table id =2 ,
     # if deleting the foreign key table id 1 , it will automatically deletes the main table id matcing those departments 
     #data or a record  gets deleted when the record in main table is selected to delete    

# serilization:
class Student_ser(models.Model):
    name = models.CharField(max_length =50)
    age = models.IntegerField()
    course =  models.CharField(max_length =50)

    def __str__(self):
        return self.name
    
#Signals:
class Student_Signals(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

