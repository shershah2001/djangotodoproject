from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import TodoModel
import logging
logger = logging.getLogger(__name__)
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_num = request.POST.get('roll_num')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        father_image = request.FILES.get('father_image')
        mother_image = request.FILES.get('mother_image')
        student_image = request.FILES.get('student_image')
        todoModel = TodoModel(name=name,roll_num=roll_num,father_name=father_name,mother_name=mother_name,phone=phone,email=email,address=address,gender=gender,father_image=father_image,mother_image=mother_image,student_image=student_image)
        todoModel.save()
    return render(request,'todolist/home.html')

def Read_Data(request):
    all_data = TodoModel.objects.all()
    data={
        'res_data':all_data,
    }
    return render(request,'todolist/readdata.html',data)

def Request_Data(request,task_id):
    viewData =  TodoModel.objects.get(id=task_id)
    print(viewData)    
    data={
        'popdata':viewData
    }
    
    return render(request,'todolist/readdata.html',data)
            

def Delete_Data(request,task_id):
    task = TodoModel.objects.get(id=task_id);
    if task:
        task.delete ()
    
    return redirect('readdata')

import logging
logger = logging.getLogger(__name__)

def Updata_Data(request, task_id):
    task = TodoModel.objects.get(id=task_id)
    if request.method == 'POST':
        task.name = request.POST.get('name')
        task.roll_num = request.POST.get('roll_num')
        task.father_name = request.POST.get('father_name')
        task.mother_name = request.POST.get('mother_name')
        task.phone = request.POST.get('phone')
        task.email = request.POST.get('email')
        task.address = request.POST.get('address')
        task.gender = request.POST.get('gender')
        task.father_image = request.FILES['father_image']
        task.mother_image = request.FILES['mother_image']
        task.student_image = request.FILES['student_image']
        task.save()
        return redirect('/readdata/')
    return render(request, 'todolist/update.html', {'data': task})
     
    
    


 






