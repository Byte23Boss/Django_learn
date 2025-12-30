# mentioning which table is changed to json format(jsonify), all the values in the table will be changed to json format
from rest_framework import serializers
from .models import Student_ser
class StudentSerializer(serializers.ModelSerializer): #--> This class is to change in to json which is serializer
    class Meta: # 
        model =  Student_ser
        fields = '__all__' #--> makes all the fields in the table are converted into json
        # next step is to create a view set so go to views.py