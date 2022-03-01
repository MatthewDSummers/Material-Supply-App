from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import User
import bcrypt
# Create your views here.

def index(request):

    return redirect('/login')

def user_page(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
    }
    return render(request, 'user-page.html', context)

def admin_page(request):

    return render(request, 'admin-page.html')

def mgmt_page(request):

    return render(request, 'mgmt-page.html')

# def create_manager(request):
#     errors = Manager.objects.validator(request.POST)

#     if errors:
#         for k, v in errors.items():
#             messages.error(request, v)
#         request.session['message_status'] = "error"
#         return redirect('/login/register-page')
#     else:
#         pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
#         Manager.objects.create(
#             level = 2,
#             first_name = request.POST['first_name'],
#             last_name = request.POST['last_name'],
#             email = request.POST['email'],
#             password = pw_hash
#         )
#         messages.info(request, "Welcome to the ticket app!  Please login! ")
#         request.session['message_status'] = "success"
#         return redirect('/login/signin')