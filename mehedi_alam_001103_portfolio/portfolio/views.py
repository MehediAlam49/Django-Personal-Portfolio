from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from portfolio.models import *
from portfolio.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('registerPage')

        # Check if username exists
        if CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('registerPage')

        # Check if email exists
        if CustomUserModel.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('registerPage')

        # Create user
        user = CustomUserModel.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        if user:
            ProfileModel.objects.create(
                user = user,
            )
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('loginPage')

    return render(request, 'registerPage.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('profile')  
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'loginPage.html')


def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def home(request):
    return render(request,'home.html')



@login_required
def changePassword(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, "Current password is incorrect.")
            return render(request, 'changePasswordPage.html')

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return render(request, 'changePasswordPage.html')

        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)

        messages.success(request, "Password changed successfully.")
        return redirect('profile') 

    return render(request, 'changePasswordPage.html')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def updateProfile(request):
    profile = request.user.profile 

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile') 
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'updateProfile.html', {'form': form})




@login_required
def addResume(request):
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewResumeList') 
    else:
        form = ResumeForm()
        
    context={
            'form':form
        }
        
    return render(request,"addResumeField.html",context)

@login_required
def viewResumeList(request):
    
    resume=ResumeModel.objects.all()
    
    context={
        'resumes':resume
    }
    
    return render(request,"viewResumeList.html",context)

@login_required
def resume_detail(request,id):
    resume=ResumeModel.objects.get(id=id)
    
    
    return render(request,"resume_detail.html",{'resume':resume})


@login_required
def resume_edit(request, id):
    
    resume = get_object_or_404(ResumeModel, id=id)
    
    if request.method == 'POST':
        
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('resume_detail', id=resume.id) 
    else:
        form = ResumeForm(instance=resume)
    
    return render(request, 'resume_edit.html', {'form': form, 'resume': resume})

@login_required
def resume_delete(request,id):
    
    resume=ResumeModel.objects.get(id=id).delete()
    
    return redirect("viewResumeList")

@login_required
def contact_view(request):
    if  request.method  == "POST":
        form=ContactForm(request.POST)
        
        if form.is_valid():
            form.save()

        return redirect('home')

    else:
        form=ContactForm()   
    return  render(request , 'contactpage.html',{'form':form})