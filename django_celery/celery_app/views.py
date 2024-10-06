from django.shortcuts import render
from django_celery.celery import add
from celery.result import AsyncResult
# Create your views here.
def index(request):
    print("inside index")
    result = add.delay(1000890, 908786) # Enqueue Task
    print("REsult : ",result)
    return render(request, "celery_app/index.html", {"result":result})
    
def contact(request):
   return render(request, 'celery_app/contact.html')
    

def about(request):
    return render(request, 'celery_app/about.html')
    
def result(request, task_id):
    result_res = AsyncResult(task_id)
    print(result_res.state)
    print(result_res.result)
    return render(request, 'celery_app/result.html', {'result':result_res})