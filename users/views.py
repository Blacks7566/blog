from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm,UserUpdateForm,ProfileUdateForm

# message.debug
# message.info
# message.success
# message.warning
# message.error


# Create your views here.


def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Account created for {username}!')
            return redirect('login')            
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request,'Your account is updated..!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm()
        p_form = ProfileUdateForm()

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'users/profile.html',context)