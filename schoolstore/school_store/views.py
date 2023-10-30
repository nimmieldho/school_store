from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .forms import *
from .models import *
# Create your views here.
def demo(request):
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)

        return redirect('new_page')

    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        confirm_password = request.POST['Confirm Password']
        return redirect('login')
    return render(request, "register.html")

def new_page(request):
    return render(request, "new_page.html")
# def form(request):
#     if request.method=='POST':
#         Name=request.POST['Name']
#         DOB=request.POST['DOB']
#         Age=request.POST['Age']
#         Gender=request.POST['Gender']
#         Phone_number=request.POST['Phone number']
#         Email_id=request.POST['Email id']
#         Address=request.POST['Address']
#
#         user=auth.authenticate(Name=Name,DOB=DOB,Age=Age,Gender=Gender,Phone_number=Phone_number,Email_id=Email_id,Address=Address)
#         if user is not None:
#             confirmation_message = "Order Confirmed"
#             # return redirect('form')
#     return render(request, "form.html")





def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            # Process the form data here

            messages.info(request, "Your data has been processed")
            # return redirect('order')
        else:
            form = OrderForm()
    return render(request, 'order_form.html')



def logout(request):
    # auth.logout(request)
    return redirect('/')





def form_create_view(request):
    form = formCreationForm()
    if request.method == 'POST':
        form = formCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            messages.info(request,"Your data has been saved successfully.")
            # return redirect('form_add')
    return render(request, 'form/home.html', {'forms': form})


def form_update_view(request, pk):
    person = get_object_or_404(Form, pk=pk)
    form = formCreationForm(instance= Form)
    if request.method == 'POST':
        form = form_create_view(request.POST, instance=Form)
        if form.is_valid():
            form.save()
            return redirect('form_change', pk=pk)
    return render(request, 'form/home.html', {'form': form})

# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'form/course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
