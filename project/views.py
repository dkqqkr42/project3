from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from signin.models import *
from map.models import Point
from django.http import JsonResponse # JSON 응답
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.paginator import Paginator
import smtplib
from email.mime.text import MIMEText


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
            request.session['id'] = user.id
            return HttpResponseRedirect('/index/')
            # return render(request, 'index.html')
        except:
            # messages.info(request, '아이디나 비밀번호가 다릅니다.')
            return HttpResponse('<script>alert("아이디나 비밀번호가 다릅니다.");history.back()</script>')

    return render(request, 'signin.html')

def map(request):
    return render(request, 'map.html')              # map 생성

 
def signup(request):
    if request.method == 'POST':
        userID = request.POST.get("userID")
        userPassword = request.POST.get("userPassword")
        userName = request.POST.get("userName")
        userEmail = request.POST.get("userEmail")
        userGender = request.POST.get("userGender")
        user = User(userID=userID, userPassword=userPassword, userName=userName, userEmail=userEmail, userGender=userGender)
        user.save()

        user = User.objects.get(userID=userID)
        mon1 = request.POST.get("mon1")
        mon2 = request.POST.get("mon2")
        mon3 = request.POST.get("mon3")
        mon4 = request.POST.get("mon4")
        mon5 = request.POST.get("mon5")
        mon6 = request.POST.get("mon6")
        mon7 = request.POST.get("mon7")
        mon8 = request.POST.get("mon8")
        monday = Monday(class1=mon1, class2=mon2, class3=mon3, class4=mon4, class5=mon5, class6=mon6, class7=mon7, class8=mon8, user=user)
        monday.save()

        tue1 = request.POST.get("tue1")
        tue2 = request.POST.get("tue2")
        tue3 = request.POST.get("tue3")
        tue4 = request.POST.get("tue4")
        tue5 = request.POST.get("tue5")
        tue6 = request.POST.get("tue6")
        tue7 = request.POST.get("tue7")
        tue8 = request.POST.get("tue8")
        tuesday = Tuesday(class1=tue1, class2=tue2, class3=tue3, class4=tue4, class5=tue5, class6=tue6, class7=tue7, class8=tue8, user=user)
        tuesday.save()

        wed1 = request.POST.get("wed1")
        wed2 = request.POST.get("wed2")
        wed3 = request.POST.get("wed3")
        wed4 = request.POST.get("wed4")
        wed5 = request.POST.get("wed5")
        wed6 = request.POST.get("wed6")
        wed7 = request.POST.get("wed7")
        wed8 = request.POST.get("wed8")
        wednesday = Wednesday(class1=wed1, class2=wed2, class3=wed3, class4=wed4, class5=wed5, class6=wed6, class7=wed7, class8=wed8, user=user)
        wednesday.save()

        thu1 = request.POST.get("thu1")
        thu2 = request.POST.get("thu2")
        thu3 = request.POST.get("thu3")
        thu4 = request.POST.get("thu4")
        thu5 = request.POST.get("thu5")
        thu6 = request.POST.get("thu6")
        thu7 = request.POST.get("thu7")
        thu8 = request.POST.get("thu8")
        thursday = Thursday(class1=thu1, class2=thu2, class3=thu3, class4=thu4, class5=thu5, class6=thu6, class7=thu7, class8=thu8, user=user)
        thursday.save()

        fri1 = request.POST.get("fri1")
        fri2 = request.POST.get("fri2")
        fri3 = request.POST.get("fri3")
        fri4 = request.POST.get("fri4")
        fri5 = request.POST.get("fri5")
        fri6 = request.POST.get("fri6")
        fri7 = request.POST.get("fri7")
        fri8 = request.POST.get("fri8")
        friday = Friday(class1=fri1, class2=fri2, class3=fri3, class4=fri4, class5=fri5, class6=fri6, class7=fri7, class8=fri8, user=user)
        friday.save()

        return HttpResponse('<script>alert("회원가입이 완료되었습니다. 가입한 아이디로 로그인 해주세요.");location.href="/signin/";</script>')
    # if User.objects.filter(userID=userID).exists():
    #     return HttpResponse('이미 사용중입니다.')

    return render(request, 'signup.html')

def board(request):
    type = request.GET.get('type')
    q = request.GET.get('q')
    if type == 'title':
        article_list = Article.objects.filter(title__contains=q).order_by('-id')
    # article_list = Article.objects.all().order_by('-id')
    else:
        if not q:
            q = ''
        article_list = Article.objects.filter(content__contains=q).order_by('-id')
    paginator = Paginator(article_list, 5)
    page = int(request.GET.get('p', 1))
    posts = paginator.get_page(page)
    return render(request, "board.html", {'article_list' : article_list, 'posts' : posts})

def write(request):
    if not request.session.session_key:
        return HttpResponse('<script>alert("권한이 없습니다.");history.back()</script>')
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        try:
            userID = request.session['userID']
            # select * from user where email = ?
            user = User.objects.get(userID=userID)

            # insert into article (title, content, user_id) values (?, ?, ?)
            article = Article(title=title, content=content, user=user)
            article.save()
            return HttpResponse('<script>alert("글 작성을 완료하였습니다.");location.href="/article/board/";</script>')
        except:
            return HttpResponse('<script>alert("로그인 후 이용해주세요.");history.back()</script>')
    return render(request, 'write.html')


def detail(request, id):

    # select * from article where id = ?
    article = Article.objects.get(id=id)
    context = {
    'article' : article
    }
    return render(request, 'detail.html', context)

def update(request, id):

    # select * from article where id = ?
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            # update article set title = ?, content = ? where id = ?
            article.title = title
            article.content = content
            article.save()
            return HttpResponse('<script>alert("수정하였습니다.");location.href="/article/board/";</script>')
        except:
            return HttpResponse('<script>alert("수정할 수 없습니다.");history.back()</script>')
    context = {
        'article' : article
    }
    return render(request, 'update.html', context)

def delete(request, id):
    try:
        # select * from article where id = ?
        article = Article.objects.get(id=id)
        article.delete()
        return HttpResponse('<script>alert("삭제되었습니다.");location.href="/article/board/";</script>')
    except:
        return HttpResponse('<script>alert("삭제할 수 없습니다.");history.back()</script>')

def signout(request):
    del request.session['userID'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return HttpResponse('<script>alert("로그아웃 되었습니다.");history.back()</script>')
  
def map_data(request):
    list = Point.objects.all()
    data = []
    for li in list:
        li = model_to_dict(li)
        data.append(li)
    return JsonResponse(data, safe=False)


def help(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        email = 'chojaelong@gmail.com'
        # 발신자주소, 수신자주소, 메시지
        send_mail(email, title, comment)
        return HttpResponse('<script>alert("메일이 전송되었습니다 소중한 의견 감사합니다.");history.back()</script>')
    return render(request, 'help.html')

def send_mail(email, title, msg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # SMTP 설정
    smtp.login(email, 'lpzloitdranbjwro')  # 인증정보 설정
    msg = MIMEText(msg)
    msg['Subject'] = '[웹페이지 문의사항]' + title  # 제목
    msg['To'] = email  # 수신 이메일
    smtp.sendmail(email, email, msg.as_string())
    smtp.quit()

def schedule(request):
    if not request.session.session_key:
        return HttpResponse('<script>alert("로그인 후 이용해 주세요.");history.back()</script>')
    context = {}
    try:
        id = request.session['id']
        if id:
            mon = Monday.objects.get(user_id=id)
            tue = Tuesday.objects.get(user_id=id)
            wed = Wednesday.objects.get(user_id=id)
            thu = Thursday.objects.get(user_id=id)
            fri = Friday.objects.get(user_id=id )
            context['mon'] = mon
            context['tue'] = tue
            context['wed'] = wed
            context['thu'] = thu
            context['fri'] = fri
    except:
        pass
    
    return render(request, 'schedule.html', context)
