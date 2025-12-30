from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
#(or)
from myapp.models import Employee

from rest_framework import viewsets
from .models import Student_ser
from .serialize import StudentSerializer
from .models import Student_Signals

# from .models import Students
# or
# from myapp.models import Students

#(.)Dot --> current file or folder

# Create your views here.
# create you rviews here
# def home(request):
    # return HttpResponse ("welcome to django...")

# Employee.objects.create(name = "Arul",age="23") # table record are defaultly in the form of obejct in order take that object this is used

# Students.objects.create(stu_name = "Arun",stu_age ="25",stu_num ="001")
# Students.objects.create(stu_name="kamal",stu_age ="26",stu_num="002")

def home(request):
    return HttpResponse ("Welcome to Django..")

#ORM :
#Queryset : Changing a Table's record to object format assigning it to a variable 
# inoder to fetch the data 1st the data should be imported in this views.py

data = Employee.objects.all() #queryset
# for i in data:
#     print(i.name)
# print("data :",data)

#Insert 
# Employee.objects.create(name="Raju",age=23)


#select * from Employee where age=23
# age=Employee.objects.filter(age=23)
# print(age)

#Update:
# data = Employee.objects.get(id =7) # get --> one record , filter --> multiple records 
# data.age=23
# data.save()

#Delete:
# data = Employee.objects.get(id=4)
# data.delete()
# To delete all the records --> Employee.objects.all()


# Join Types:
#OneToOne - one main table  to one table
#OneToMany - one main table to many child table
#ManyToOne - many main table to one child table
#ManyToMany - many main table to many child table

#2. Select Related:

 #select_related() performs a SQL JOIN and fetches related objects in one single query

 #Use it when:
    # * You have ForeignKey
    # * You have OneToOneField  
    

# emp = Employee.objects.all() #select * from Employee
# for e in emp:
#     print(e.department.name) #select * from department where id = 1 ;prints the department name matching the employee id from the department table ; --> the employees data(which has name and id ) are stored as e , where the department data(has dept id) as stored in department 
# so it matches the department id (foreignkey table) to the employee id and prints the department name 
                             #select * from department where id = 2;
                             #select * from department where id = 3;
                            # N+1 Queries
# Total  = 1 +N ueries(no.of.employyees)

#output:
#Ravi(dept_id=1) developer
#Kumar (dept_id=1) developer
#Arjun(dept_id=2) sales clerk

# data = Employee.objects.select_related('department').all()  # Explanation below
# for e in data:
#     print(e.department.name)
    
#select_related work flow

#select Employee.*,Department.*
# From Employee
# inner join Department
# on Employee.department.id = department.id;


# for e in employees:
#     print(e.department.name)
    
# Browser
#   ↓
# Employee + Department JOIN Query ───► 1 query
#   ↓
# Loop prints data (NO DB calls)
#Prefetch --> for many to many tables
 #Without Prefetch related:

#     Browser / View
#       |
#       |---- Query 1 ----> Book Table
#       |
#       |---- Query 2 ----> Author Table (Book 1)
#       |
#       |---- Query 3 ----> Author Table (Book 2)
#       |
#       |---- Query 4 ----> Author Table (Book 3)
      
# Total Queries = 1 + N


# with prefetch_related :

# Browser / View
#       |
#       |---- Query 1 ----> Book Table
#       |
#       |---- Query 2 ----> Author + M2M Table
#       |
#       |---- Python Memory Join
#       |
#       |---- Loop prints data (NO DB CALLS)
      
# Total Queries = 2

# books = Book.objects.all() #1 query for books (select * from book;)
# for b in books:
#     print(b.authors.all()) #N queries for each book’s authors
    
    # SELECT * FROM author WHERE book_id = 1;
    # SELECT * FROM author WHERE book_id = 2;
    # SELECT * FROM author WHERE book_id = 3;
    
    
# books = Book.objects.prefetch_related('authors') --> prefetched related
# for b in books:
#     print(b.authors.all())
    
#    1. SELECT * FROM book;
#    2. SELECT * FROM author 
#       INNER JOIN book_authors
#       WHERE book_id IN (1, 2, 3);

# ✔ Only 2 queries
# ✔ No DB hit inside loop 
   
# Without Prefetch Example
# books = Book.objects.all() #1 query for books (select * from book;)
# for b in books:
#     print(b.authors.all()) #N queries for each book’s authors023
    
    # SELECT * FROM author WHERE book_id = 1;
    # SELECT * FROM author WHERE book_id = 2;
    # SELECT * FROM author WHERE book_id = 3;
    
    
# books = Book.objects.prefetch_related('authors')
# for b in books:
#     print(b.authors.all())
    
#    1. SELECT * FROM book;
#    2. SELECT * FROM author 
#       INNER JOIN book_authors
#       WHERE book_id IN (1, 2, 3);

# ✔ Only 2 queries
# ✔ No DB hit inside loop

####DRF - Django Rest Framework is an extension of Django that makes building API's easier.
# It helps to convert Django models into RESTFUL APIs that can be used by web apps, 
# mobile apps, or other services


##Serilization: Converts complex data , such as Django models or queryset , into JSon or XMl format

# Viewsets : Define views that handle API requests and responses.

#Serilization: check in model.py page
class StudentViewSet(viewsets.ModelViewSet): #to change the class  into viewset modelviewset is inherited
    # '''(table la iruntha value la edukarom na athuku name queryset)''' 
    queryset = Student_ser.objects.all() #--> import Student_ser for reading all the data(Display)
    serializer_class = StudentSerializer #import StudentSerializer
    
    # next set create an URL route in urls.py
    
#For pagination need to set it in the settings.py refer the line rest framework where pagination
#along with the display count of data also set

# Signals:
 #used to notify when something happens 
 # add a table for this , check models.py table name --> student_signs --> table created next create python file --> signlas.py

 #Signals value Inserted: Creating a new object it gets inserted into the database which has been created in myapp_student_signals
Student_Signals.objects.create(name="Bijoye",age=50)

# this is a test data