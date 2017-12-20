from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import UserRegistrationForm
from .forms import UserEditForm
from django.contrib import messages

@login_required
def homepage(request):
    return render(request,'account\homepage.html')

#登出    
def logout(request):
    auth.logout(request)
    return render(request,'registration\logged_out.html')

#注册
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})

#编辑个人信息
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,'Profile updates successfully!')
        else:
            messages.error(request,'Error updating your profile!')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request,'account/edit.html',{'user_form': user_form})