from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager
from login_app.models import *
import bcrypt

def index(request):
    # return redirect('/home')
    return render(request, 'index.html')
    # return redirect('/home')


def reg_page(request):
    return render(request, 'register_page.html')
def signin_page(request):
    return render(request, 'signin_page.html')

def register_user(request):
    errors = User.objects.validator(request.POST)

    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        request.session['message_status'] = "error"
        return redirect('/login/register-page')
        
    elif len(User.objects.all()) < 1:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            level=9,
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        messages.info(request, "Welcome to the ticket app!  Please login! ")
        request.session['message_status'] = "success"
        return redirect('/login/signin')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            level = 1,
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        messages.info(request, "Welcome to the ticket app!  Please login! ")
        request.session['message_status'] = "success"
        return redirect('/login/signin')

def login(request):
    try:
        user = User.objects.get(email = request.POST['email'])
    except:
        request.session['message_status'] = "error"
        messages.error(request, "Incorrect email address or password")
        return redirect('/login/signin')
    
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['user_id'] = user.id
        # request.session['user_first_name'] = user.first_name
        # request.session['user_last_name'] = user.last_name
        # request.session['user_email'] = user.email
        # request.session['user_created_at'] = user.created_at
        if user.level == 1:
            return redirect('/home')
        elif user.level == 2:
            return redirect('/management')
        elif user.level == 9:
            return redirect('/admin')
    else:
        request.session['message_status'] = "error"
        messages.error(request, "Incorrect email address or password")
        return redirect('/login/signin')

def logout(request):
    # request.sessions.clear()
    # the above would work, but the below is specific (maybe I don't wanna end ALL sessions)
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user_first_name' in request.session:
        del request.session['user_first_name']
    if 'user_last_name' in request.session:
        del request.session['user_last_name']
    if 'user_email' in request.session:
        del request.session['user_email']
    
    return redirect('/')


# def profile(request, quote_user_id):
#     user = User.objects.get(id=request.session['user_id'])
#     poster = User.objects.get(id=quote_user_id)
#     context = {
#         'all_quotes':poster.quotes.all(),
#         'poster':poster,
#         'user':user
#     }
#     return render(request, 'profile.html', context)

# def delete_quote(request, quote_id):
#     quote = Quote.objects.get(id=quote_id)
#     quote.delete()
#     return redirect('/quotes')

# def edit_page(request, user_id):
#     user_id = request.session['user_id']

#     context = {
#         'user': User.objects.get(id=user_id)
#     }
#     return render(request,'edit.html', context)

# def update_user(request, user_id):
#     errors = User.objects.update_validator(request.POST)
#     user = User.objects.get(id=user_id)
#     e_len = len(request.POST['email'])
#     f_len = len(request.POST['first_name'])
#     l_len = len(request.POST['last_name'])
#     keep_names = len(request.POST['first_name']) == 0 and len(request.POST['last_name']) == 0
#     keep_f_e = len(request.POST['first_name']) == 0 and len(request.POST['email']) == 0
#     keep_l_e = len(request.POST['last_name']) == 0 and len(request.POST['email']) == 0
#     keep_first = len(request.POST['first_name']) == 0 and len(request.POST['last_name']) > 1
#     keep_last = len(request.POST['last_name']) == 0 and len(request.POST['first_name']) > 1
#     keep_email = len(request.POST['email']) == 0 and len(request.POST['first_name']) > 1
#     gt1 = e_len > 1 and f_len > 1
#     lt1 = e_len ==0 and f_len ==0
    
#     if errors:
#         for k, v in errors.items():
#             messages.error(request, v)
#         request.session['message_status'] = "error"
#         return redirect(f'/myaccount/{user.id}')

#     if keep_first and e_len >1:
#         user.first_name = user.first_name
#         user.last_name=request.POST['last_name']
#         user.email=request.POST['email']
#         user.save()
#         messages.info(request, "Thanks for updating your info!")
#         request.session['message_status'] = "success"
#         return redirect(f'/myaccount/{user.id}')

#     if keep_names and e_len >1:
#         user.first_name = user.first_name
#         user.last_name=user.last_name
#         user.email=request.POST['email']
#         user.save()
#         messages.info(request, "Thanks for updating your info!")
#         request.session['message_status'] = "success"
#         return redirect(f'/myaccount/{user.id}')

#     if keep_last and e_len >1:
#         user.first_name = request.POST['first_name']
#         user.last_name=user.last_name
#         user.email=request.POST['email']
#         user.save()
#         messages.info(request, "Thanks for updating your info!")
#         request.session['message_status'] = "success"
#         return redirect(f'/myaccount/{user.id}')

#     if keep_email and l_len >1:
#         user.first_name = request.POST['first_name']
#         user.last_name= request.POST['last_name']
#         user.email=user.email
#         user.save()
#         messages.info(request, "Thanks for updating your info!")
#         request.session['message_status'] = "success"
#         return redirect(f'/myaccount/{user.id}')

#     if keep_f_e and l_len >1:
#         user.first_name = user.first_name
#         user.last_name= request.POST['last_name']
#         user.email=user.email
#         user.save()
#         messages.info(request, "Thanks for updating your info!")
#         request.session['message_status'] = "success"
#         return redirect(f'/myaccount/{user.id}')

#     if keep_l_e and f_len >1:
#         user.first_name = request.POST['first_name']
#         user.last_name= user.last_name
#         user.email=user.email
#         user.save()
#         messages.info(request, "Thanks for updating your info!")
#         request.session['message_status'] = "success"
#         return redirect(f'/myaccount/{user.id}')

#     if gt1 and l_len >1:
#         user.first_name=request.POST['first_name']
#         user.last_name=request.POST['last_name']
#         user.email=request.POST['email']
#         user.save()
#         messages.info(request, "Thanks for updating your info!")
#         request.session['message_status'] = "success"
#         return redirect(f'/myaccount/{user.id}')

#     elif lt1 and l_len ==0:
#         user.first_name=user.first_name
#         user.last_name=user.last_name
#         user.email=user.email
#         user.save()
#         messages.info(request, "Nothing to update? Okay!")
#         request.session['message_status'] = "success"
#         return redirect(f'/myaccount/{user.id}')


# def user_profile(request, ticket_sender_id):
#     sender = User.objects.get(id=ticket_sender_id)
#     # history = Ticket.objects.filter(sender=sender)
#     user=User.objects.get(id=request.session['user_id'])

#     context = {
#         'sender':sender,
#         # 'history': history,
#         # 'user_tix': User.objects.filter(tickets=history),
#         'user':user
#     }
#     return render(request, 'user_page.html', context)

