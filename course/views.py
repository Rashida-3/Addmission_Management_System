from django.shortcuts import render,redirect
from . models import USerMaster
from django.http import HttpResponseBadRequest,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .models import USerMaster
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

#home page
def home_page(request):
    return render(request, 'login.html')


def navbar_and_sidebar(request):
    return render(request, 'sidebar.html')

def my_course(request):
    user = USerMaster.objects.get(id=request.user.id)
    return render(request, 'user.html', {'user': user})


#updateform page
def update(request):
    return render(request,'update.html')


def signup(request):
    choices = USerMaster.CHOICES
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        city = request.POST.get('city')
        my_field = request.POST.get('my_field', '')
        password = request.POST.get('password')
        user = USerMaster.objects.create_user(name=name, email=email, phone=phone, date_of_birth=date_of_birth, city=city, password=password,my_field=my_field)
        if user:
            return redirect('login')
        else:
            return HttpResponse('Failed to create user', status=400)
    return render(request,'signup.html',{'choices':choices})


def update1(request,pk):
    user1 = USerMaster.objects.get(pk=pk)
    alert=False
    if request.method == "POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        date_of_birth=request.POST.get('date_of_birth','')
        city=request.POST.get('city','')
        my_field=request.POST.get('my_field','')
        post = User.objects.filter(pk=pk).first()
        post.name=name
        post.email=email
        post.phone=phone
        post.date_of_birth=date_of_birth
        post.city=city
        post.my_field=my_field
        post.save()
        if post:
            alert=True
            request.session['user'] = alert
        return redirect('update')
    request.session['user'] = alert         
    post=USerMaster.objects.all()
    return render (request,'update1.html',{'post':post,'user':user1,'alert':alert})
    

# #to create a user
def add_user(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        city = request.POST.get('city')
        my_field = request.POST.get('my_field')

        # Check if any field is empty
        if not all([name, email, phone, date_of_birth, city, my_field]):
            error_message = 'Please fill all the fields'
            return render(request, 'add_stud.html', {'error_message': error_message})

        # Create an instance of your model and save it to the database
        user =USerMaster.objects.create(
            name=name,
            email=email,
            phone=phone,
            date_of_birth=date_of_birth,
            city=city,
            my_field=my_field
        )
        user.save()

        success_message = 'Form submitted successfully'
        return render(request, 'add_stud.html', {'success_message': success_message})
    else:
        return render(request, 'add_stud.html')

# login views

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='superuser').exists():
                return redirect('navbar_and_sidebar')
            ##admin page
            elif user.groups.filter(name='admin').exists():
                return redirect('navbar_and_sidebar')

            elif user.groups.filter(name='user').exists():
                return redirect('navbar_and_sidebar')
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        request.session.flush()
        return render(request, 'login.html')


#for updating user


def update_user(request):
    if request.method == 'POST':
        # Retrieve data from the form
        update_name = request.POST.get('update_name')
        update_email = request.POST.get('update_email')
        update_phone = request.POST.get('update_phone')
        update_city = request.POST.get('update_city')
        my_field= request.POST.get('my_field')
        user_id = request.POST.get('user_id')  # Assuming there's an input field named 'user_id' in your form

        # Get the user instance based on the provided user_id
        user_instance = USerMaster.objects.get(id=user_id)  

        # Update user fields with new values
        user_instance.name = update_name
        user_instance.email = update_email
        user_instance.phone = update_phone
        user_instance.city = update_city
        user_instance.my_field = my_field

        user_instance.save()
        messages.success(request, 'User updated successfully!')

    # If the request method is not POST, render the form page
    return render(request, 'update.html')

#for logout
def logout_user(request):
    logout(request)
    return redirect('home_page')


def search(request):
    choices = USerMaster.CHOICES
    if request.method == "POST":
        data=request.POST.get('my_field','')
        data1= request.POST.get('name', '') #rashida

        courses=USerMaster.objects.filter(my_field__icontains=data)
        courses=USerMaster.objects.filter(name__icontains=data1)

        return render(request,'dashboard.html',{'courses':courses})
    courses=USerMaster.objects.all()

    contact_list = USerMaster.objects.all()
    paginator = Paginator(contact_list, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    courses = paginator.get_page(page_number)

    return render(request,'dashboard.html',{'courses':courses,'choices':choices})


def delete_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(USerMaster, id=user_id)
        user.delete()
        messages.success(request, 'User deleted successfully.')
    return redirect('dashboard') 

