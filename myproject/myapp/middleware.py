from django.http import HttpResponse
import time

class Mymiddleware: #Middelware --> before view goes to middleware , can check in settings.py (alreay has 7)
#middelware works when server gets start , calls when browser make request before view function 
    def __init__(self,get_response):
        self.get_response = get_response
        print("Middleware initialized...")
    
    # def __call__(self,Request):
    #     print("Before view(Request Intercepted)")
    #     response = self.get_response(Request)
    #     print("After view(Request going to browser)")
    #     return response
    
    #To calculate the request and response time of a route
    def __call__(self,Request):
        start_time = time.perf_counter()
        print("start_time :",time.perf_counter())
        response = self.get_response(Request)
        total_time = time.perf_counter() - start_time
        print(f"The total_time is Total_time :{total_time:.2f}") 
        return response