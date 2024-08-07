from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render,redirect , get_object_or_404
from .forms import CreateForm
from .models import User
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            return redirect('auth')
        else:
            return render(request, 'display.html', {'error': 'Email not registered'})
    return render(request, 'display.html')
def auth_view(request):
    context = {'authenticated':None}
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            context['authenticated'] = True
        else:
            context['authenticated'] = False
    return render(request,'auth.html',context)
def createUser(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display.html')
    else:
        form = CreateForm()
    return render(request,'create.html',{'form':form})
@login_required
def update(request):
    profile, created = User.objects.get_or_create(user=request.user.email)
    if request.method == 'POST':
        form = CreateForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form=CreateForm(instance=profile)
    return render(request, 'profile_update.html' , {'form':form})
User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(email=email)
                return render(request,'display.html') 
    else:
        form = UserRegistrationForm()
    return render(request,'register.html')





