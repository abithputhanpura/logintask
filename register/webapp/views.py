from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, SignupForm
from . models import Userdata
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .serializers import RegisterSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


def index(request):
    data = Userdata.objects.all()
    return render(request, 'index.html',{'data':data})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Credential Invalid')
                return redirect('login')
    else:
        return render(request, 'login.html', {'form': form})

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # date_of_birth = form.cleaned_data['date_of_birth']
            username = form.cleaned_data['username']
            # address = form.cleaned_data['address']
            email_id = form.cleaned_data['email_id']
            # phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            # global data
            # data=[first_name, last_name, date_of_birth, username, address, email_id, phone]
            user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                            username=username,
                                            email=email_id, password=password)
            user.save()
            form.save()
            return redirect('/')
            # if password == confirm_password:
            #     username1 = User.objects.all()
            #     print(username1)
            #     for user in username1:
            #         if user.username == username:
            #             messages.info(request, 'username already exist')
            #             return redirect('signup')
            #         else:

    else:
        context = {'form': form}
        return render(request, 'signup.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')

# class user_view(APIView):
#     def get(self,request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        details = Userdata.objects.all()
        serializer = RegisterSerializer(details, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




