from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"i am shan"    }
    return render(request, 'index.html',context)
#         return HttpResponse("this is home page")
def about(request):
    
        # return HttpResponse("this is about page")
    return render(request, 'base.html')