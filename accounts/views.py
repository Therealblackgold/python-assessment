from django.shortcuts import redirect, render
# Auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UpdateCustomUserForm
from .models import CustomUser
from django.contrib import messages
from tasks.models import Task
from tasks.forms import TaskForm


# Register
def registerUser(request):

    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


# Login
def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')

        else:
            messages.info(request, 'Username Or Password is incorrect!')

    context = {}
    return render(request, 'accounts/login.html', context)


@login_required(login_url='login')
# Homepage
def homepage(request):
    user = request.user
    # tasks = Task.objects.filter(user=user)

    # # tasks
    # form = TaskForm()

    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    context = {'user': user}
    return render(request, 'accounts/homepage.html', context)


# Logout
def logoutUser(request):
    logout(request)
    return redirect('login')


# Update CustomUser
@login_required(login_url='login')
def updateUser(request, user_id):

    # Getting data from the form id=pk ,instance=form
    user = CustomUser.objects.get(id=user_id)
    form = UpdateCustomUserForm(instance=user)
    confirm = False

    if request.method == 'POST':
        form = UpdateCustomUserForm(request.POST or None,
                                    request.FILES or None,
                                    instance=user)

        if form.is_valid():
            form.save()
            confirm = True
            # return redirect('homepage')

    context = {'form': form, 'confirm': confirm}
    return render(request, 'accounts/user_form.html', context)