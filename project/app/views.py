from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

# def home(request):
#     return HttpResponse("'color:red' welcome")


# def data(request):
#     data1={"name":"mehak",
#            "age":32}
#     return JsonResponse (data1)
    
def register(request):
    return render(request,'register.html')