from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from signin.models import User
from django.http import JsonResponse # JSON 응답
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        # 회원정보 조회
        userID = request.POST.get('userID')
        userPassword = request.POST.get('userPassword')

        try:
            # select * from user where email=? and pwd=?
            user = User.objects.get(userID=userID, userPassword=userPassword)
            # 정보표시
            request.session['userID'] = userID
            return render(request, 'signin_success.html')
        except:
            return render(request, 'signin_fail.html')

    return render(request, 'signin.html')

def signup(request):
    
    userID = request.POST.get("userID")
    userPassword = request.POST.get("userPassword")
    userName = request.POST.get("userName")
    userEmail = request.POST.get("userEmail")
    userGender = request.POST.get("userGender")

    if User.objects.filter(userID=userID).exists():
        return HttpResponse('이미 사용중입니다.')

    return render(request, 'signup.html')
  
