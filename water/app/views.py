from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .models import logi,price,employee,detail,orders,cancel,concent,product
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
import datetime
# Create your views here.
#index
def display(request):
    d1 = product.objects.all()
    return render(request, 'index.html', {'r': d1})
def display1(request):
    d1 = product.objects.all()
    return render(request, 'index1.html', {'r': d1})



#about
def about(request):
    return render(request,'about.html')
def about1(request):
    return render(request,'about1.html')

#contact
def contact(request):
    return render(request,'contact.html')
def contact1(request):
    return render(request,'contact1.html')


#shop
def shopp(request):
    d1 = product.objects.all()
    return render(request,'shop.html',{'r':d1})
def shop1(request):
    d1 = product.objects.all()
    return render(request, 'shop.html', {'r': d1})


def checkout1(request):
    a = request.session['id']
    d2=price.objects.filter(name=a,payment='pending')

    return render(request,'checkout1.html',{'r':d2})
# def single(request):
#     return render(request,'single-product.html')


#login
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'reg.html')

def reg(request):
    if request.method == 'POST':
        a = user.objects.all()
        x = request.POST['n1']
        y = request.POST['n2']
        z = request.POST['n3']
        w = request.POST['n4']
        s = 'username already exist'
        f=0
        for i in a:
            if i.name == x:
                f+=1
                return render(request, 'reg.html', {'r': s})
            elif i.emaill == y:
                f+=1
                return render(request, 'reg.html', {'t':'email already exist' })

        if f == 0:
            if z == w:
                d = user.objects.create(name=x,emaill=y,pswd=z,cpswd=w,status=1)
                d.save()
                d1 = logi.objects.create(name=x, pswd=z,status=1)
                d1.save()
                return render(request, 'login.html')
            else:
                return render(request, 'reg.html', {'a': 'password do not match'})

    else:
        return render(request,'reg.html')

def profile(request):
    if 'id' in request.session:
        u=request.session['id']
        d = logi.objects.get(name=u)
        if d.status == 1:
            d1 = product.objects.all()
            return render(request, 'index1.html', {'r': d1})
        elif d.status == 2:
            d = detail.objects.all()
            return render(request,'order1.html',{'r':d})
        else:
            d = employee.objects.all()
            return render(request, 'admn.html',{'r':d})
    else:
        d1 = product.objects.all()
        return render(request, 'index.html', {'r': d1})

def login1(request):
    if request.method == 'POST':
        x = request.POST['n1']
        y = request.POST['n2']
        z = 'incorrect password'
        w = 'user not found'
        try:
            d = logi.objects.get(name=x)
            if d.pswd == y:
                request.session['id'] = x
                if d.status == 1:

                    return redirect(profile)
                elif d.status == 2:
                    return redirect(profile)


                else:
                    return redirect(profile)
            else:
                return render(request, 'login.html',{'r':z})
        except Exception:
            return render(request, 'login.html', {'r': w})
#logout

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request,'index.html')
#cart

def cart(request):
    return render(request,'cart.html')
def cart1(request):
    a = request.session['id']
    d=price.objects.all()
    f=0
    for i in d:
        if a == i.name and i.payment == 'pending':
            f+=1
    if f==0:
        d1 = price.objects.create(n1=0, n2=0, n3=0, n4=0, q1=1, q2=1, q3=1, q4=1, p1='1 Litre', p2='2 Litre',
                                  p3='5 Litre', p4='20 litre', name=a, amt=0, total=0, action='pending',
                                  payment='pending')
        d1.save()
        d1 = price.objects.filter(name=a, amt=0, total=0)
        return render(request, 'cart1.html', {'r': d1})

    else:

        d1 = price.objects.filter(name=a, action='pending', payment='pending')

        return render(request, 'cart1.html', {'r': d1})

def cart2(request):
    if request.method == 'POST':
        a = int(request.POST['n1'])
        b = int(request.POST['n2'])
        c = int(request.POST['n3'])
        d = int(request.POST['n4'])
        e = request.session['id']
        a1=a * 15
        a2=b * 30
        a3=c * 45
        a4=d * 70
        f = 0
        g=0
        f = (a * 15) + (b * 30) + (c * 45) + (d * 70)
        g = f + 10
        d2 = price.objects.all()
        n = 0
        for i in d2:
            if i.name == e and i.payment == 'pending':
                n += 1
                break
            else:
                pass
        if n == 0:
            d1 = price.objects.create(n1=a1, n2=a2, n3=a3, n4=a4, q1=a, q2=b, q3=c, q4=d, p1='1 Litre', p2='2 Litre',
                                      p3='5 Litre', p4='20 litre', name=e, amt=f, total=g, action='pending',
                                      payment='pending')
            d1.save()
            d1 = price.objects.filter(name=e, action='pending', payment='pending')
            return render(request, 'cart1.html', {'r': d1})

        else:
            d1 = price.objects.filter(name=e, payment='pending')
            d1.update(n1=a1, n2=a2, n3=a3, n4=a4, q1=a, q2=b, q3=c, q4=d, amt=f, total=g)

            return render(request, 'checkout1.html', {'r': d1})

def crt1(request):
    a = request.session['id']
    d=price.objects.all()
    f=0
    b=0
    c=0
    e=0
    g=0
    for i in d:
        if a == i.name and i.payment == 'pending' :
            f+=1
    if f==0:
        d1 = price.objects.create(n1=15, n2=0, n3=0, n4=0, q1=1, q2=0, q3=0, q4=0, p1='1 Litre', p2='2 Litre',
                                  p3='5 Litre', p4='20 litre', name=a, amt=15, total=25, action='pending',
                                  payment='pending')
        d1.save()
        d1 = price.objects.filter(name=a,payment='pending')
        return render(request, 'shop1.html', {'r': d1})

    else:
        d1 = price.objects.filter(name=a, action='pending', payment='pending')
        for i in d1:
            b = i.q1 + 1
            c = i.n1 + 15
            e = i.amt + 15
            g = e+10
        d1.update(n1=c, q1=b, amt=e, total=g)

        return render(request, 'shop1.html', {'r': d1})
def crt2(request):
    a = request.session['id']
    d=price.objects.all()
    f=0
    b=0
    c=0
    e=0
    g=0
    for i in d:
        if a == i.name:
            f+=1
    if f==0:
        d1 = price.objects.create(n1=0, n2=30, n3=0, n4=0, q1=0, q2=1, q3=0, q4=0, p1='1 Litre', p2='2 Litre',
                                  p3='5 Litre', p4='20 litre', name=a, amt=30, total=40, action='pending',
                                  payment='pending')
        d1.save()
        d1 = price.objects.filter(name=a,payment='pending')
        return render(request, 'shop1.html', {'r': d1})

    else:
        d1 = price.objects.filter(name=a, action='pending', payment='pending')
        for i in d1:
            b = i.q2 + 1
            c = i.n2 + 30
            e = i.amt + 30
            g = e+10
        d1.update(n2=c, q2=b, amt=e, total=g)

        return render(request, 'shop1.html', {'r': d1})
def crt3(request):
    a = request.session['id']
    d=price.objects.all()
    f=0
    b=0
    c=0
    e=0
    g=0
    for i in d:
        if a == i.name:
            f+=1
    if f==0:
        d1 = price.objects.create(n1=0, n2=0, n3=45, n4=0, q1=0, q2=0, q3=1, q4=0, p1='1 Litre', p2='2 Litre',
                                  p3='5 Litre', p4='20 litre', name=a, amt=45, total=55, action='pending',
                                  payment='pending')
        d1.save()
        d1 = price.objects.filter(name=a,payment='pending')
        return render(request, 'shop1.html', {'r': d1})

    else:
        d1 = price.objects.filter(name=a, action='pending', payment='pending')
        for i in d1:
            b = i.q3 + 1
            c = i.n3 + 45
            e = i.amt + 45
            g = e + 10
        d1.update(n3=c, q3=b, amt=e, total=g)

        return render(request, 'shop1.html', {'r': d1})
def crt4(request):
    a = request.session['id']
    d=price.objects.all()
    f=0
    b=0
    c=0
    e=0
    g=0
    for i in d:
        if a == i.name:
            f+=1
    if f==0:
        d1 = price.objects.create(n1=0, n2=0, n3=0, n4=70, q1=0, q2=0, q3=0, q4=1, p1='1 Litre', p2='2 Litre',
                                  p3='5 Litre', p4='20 litre', name=a, amt=70, total=80, action='pending',
                                  payment='pending')
        d1.save()
        d1 = price.objects.filter(name=a,payment='pending')
        return render(request, 'shop1.html', {'r': d1})

    else:
        d1 = price.objects.filter(name=a, action='pending', payment='pending')
        for i in d1:
            b = i.q4 + 1
            c = i.n4 + 70
            e = i.amt + 70
            g = i.total + 70
        d1.update(n4=c, q4=b, amt=e, total=g)

        return render(request, 'shop1.html', {'r': d1})


def crt11(request):
    a = request.session['id']
    d=price.objects.all()
    f=0
    b=0
    c=0
    e=0
    g=0
    for i in d:
        if a == i.name and i.payment == 'pending' :
            f+=1
    if f==0:
        d1 = price.objects.create(n1=15, n2=0, n3=0, n4=0, q1=1, q2=0, q3=0, q4=0, p1='1 Litre', p2='2 Litre',
                                  p3='5 Litre', p4='20 litre', name=a, amt=15, total=25, action='pending',
                                  payment='pending')
        d1.save()
        d1 = price.objects.filter(name=a,payment='pending')
        return render(request, 'cart1.html', {'r': d1})

    else:
        d1 = price.objects.filter(name=a, action='pending', payment='pending')
        for i in d1:
            b = i.q1 + 1
            c = i.n1 + 15
            e = i.amt + 15
            g = e+10
        d1.update(n1=c, q1=b, amt=e, total=g)

        return render(request, 'cart1.html', {'r': d1})
def crt21(request):
    a = request.session['id']
    d=price.objects.all()
    f=0
    b=0
    c=0
    e=0
    g=0
    for i in d:
        if a == i.name:
            f+=1
    if f==0:
        d1 = price.objects.create(n1=0, n2=30, n3=0, n4=0, q1=0, q2=1, q3=0, q4=0, p1='1 Litre', p2='2 Litre',
                                  p3='5 Litre', p4='20 litre', name=a, amt=30, total=40, action='pending',
                                  payment='pending')
        d1.save()
        d1 = price.objects.filter(name=a,payment='pending')
        return render(request, 'cart1.html', {'r': d1})

    else:
        d1 = price.objects.filter(name=a, action='pending', payment='pending')
        for i in d1:
            b = i.q2 + 1
            c = i.n2 + 30
            e = i.amt + 30
            g = e+10
        d1.update(n2=c, q2=b, amt=e, total=g)

        return render(request, 'cart1.html', {'r': d1})
def crt31(request):
    a = request.session['id']
    d=price.objects.all()
    f=0
    b=0
    c=0
    e=0
    g=0
    for i in d:
        if a == i.name:
            f+=1
    if f==0:
        d1 = price.objects.create(n1=0, n2=0, n3=45, n4=0, q1=0, q2=0, q3=1, q4=0, p1='1 Litre', p2='2 Litre',
                                  p3='5 Litre', p4='20 litre', name=a, amt=45, total=55, action='pending',
                                  payment='pending')
        d1.save()
        d1 = price.objects.filter(name=a,payment='pending')
        return render(request, 'cart1.html', {'r': d1})

    else:
        d1 = price.objects.filter(name=a, action='pending', payment='pending')
        for i in d1:
            b = i.q3 + 1
            c = i.n3 + 45
            e = i.amt + 45
            g = e + 10
        d1.update(n3=c, q3=b, amt=e, total=g)

        return render(request, 'cart1.html', {'r': d1})
def crt41(request):
    a = request.session['id']
    d=price.objects.all()
    f=0
    b=0
    c=0
    e=0
    g=0
    for i in d:
        if a == i.name:
            f+=1
    if f==0:
        d1 = price.objects.create(n1=0, n2=0, n3=0, n4=70, q1=0, q2=0, q3=0, q4=1, p1='1 Litre', p2='2 Litre',
                                  p3='5 Litre', p4='20 litre', name=a, amt=70, total=80, action='pending',
                                  payment='pending')
        d1.save()
        d1 = price.objects.filter(name=a,payment='pending')
        return render(request, 'cart1.html', {'r': d1})

    else:
        d1 = price.objects.filter(name=a, action='pending', payment='pending')
        for i in d1:
            b = i.q4 + 1
            c = i.n4 + 70
            e = i.amt + 70
            g = i.total + 70
        d1.update(n4=c, q4=b, amt=e, total=g)

        return render(request, 'cart1.html', {'r': d1})


def cancel1(request):
    a=request.session['id']
    a2=0
    a3=0
    a4=0
    f=0
    g=0
    d=price.objects.filter(name=a,payment='pending')
    for i in d :
        a2=i.q2*30
        a3=i.q3*45
        a4=i.q4*70
        f=a2+a3+a4
        g=f+10
    d.update(n1=0,q1=0,amt=f,total=g)
    d = price.objects.filter(name=a, payment='pending')
    return render(request,'cart1.html',{'r':d})

def cancel2(request):
    a=request.session['id']
    a2=0
    a3=0
    a4=0
    f=0
    g=0
    d=price.objects.filter(name=a,payment='pending')
    for i in d :
        a2=i.q1*15
        a3=i.q3*45
        a4=i.q4*70
        f=a2+a3+a4
        g=f+10
    d.update(n2=0,q2=0,amt=f,total=g)
    d = price.objects.filter(name=a, payment='pending')
    return render(request,'cart1.html',{'r':d})

def cancel3(request):
    a=request.session['id']
    a2=0
    a3=0
    a4=0
    f=0
    g=0
    d=price.objects.filter(name=a,payment='pending')
    for i in d :
        a2=i.q2*30
        a3=i.q1*15
        a4=i.q4*70
        f=a2+a3+a4
        g=f+10
    d.update(n3=0,q3=0,amt=f,total=g)
    d = price.objects.filter(name=a, payment='pending')
    return render(request,'cart1.html',{'r':d})

def cancel4(request):
    a=request.session['id']
    a2=0
    a3=0
    a4=0
    f=0
    g=0
    d=price.objects.filter(name=a,payment='pending')
    for i in d :
        a2=i.q2*30
        a3=i.q3*45
        a4=i.q1*15
        f=a2+a3+a4
        g=f+10
    d.update(n4=0,q4=0,amt=f,total=g)
    d = price.objects.filter(name=a, payment='pending')
    return render(request,'cart1.html',{'r':d})


#endcart


# employee register
def empreg(request):
    return render(request,'empreg.html')
def empreg1(request):
    if request.method == 'POST':
        data=logi.objects.all()
        a = request.POST['n1']
        s = 'username already exist'
        n = 0
        for i in data:
            if i.name == a:
                n += 1

        if n ==0:
            b = request.POST['n2']
            c = request.POST['n3']
            d = request.FILES['n4']
            e = request.POST['n5']
            f = request.POST['n6']
            if e == f:
                d2 = employee.objects.create(name=a,phone=b,emaill=c,proof=d,pswd=e,cpswd=f,status=1,action='pending',deliver=0)
                d2.save()
                d1 = logi.objects.create(name=a, pswd=e,status=1)
                d1.save()
                return render(request,'login.html')
            else:
                return render(request, 'empreg.html', {'a': 'password do not match'})

        else:
            return render(request, 'empreg.html', {'r': s})
    else:
        return render(request,'empreg.html')
#end employee

#admin
#employee reject
def reject(request):

    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['action']
        if b == 'reject':
            d = employee.objects.filter(name=a)
            d.delete()
            d1 = employee.objects.all()
            return render(request, 'admn.html',{'r':d1})
        elif b == 'rejectt':
            d = employee.objects.filter(name=a)
            d.delete()
            d1 = employee.objects.all()
            return render(request, 'emplist.html',{'r':d1})
        elif b == 'accept':
            d = employee.objects.filter(name=a)
            d.update(action='confirm',status=2)
            d1 = employee.objects.all()
            return render(request, 'admn.html', {'r': d1})
        elif b == 'pay':
            b1=employee.objects.filter(name=a)
            b1.update(deliver=0)
            d1 = employee.objects.all()
            return render(request, 'emplist.html', {'r':d1})
        elif b == 'cancel':
            f=request.session['id']
            c=request.POST['n3']
            e = request.POST['n2']
            d = price.objects.filter(name=f,total=c,action='pending',payment='complete')
            d.delete()
            d1 = detail.objects.filter(nme=f,amount=c,action='pending')
            d1.delete()
            d2 = orders.objects.filter(name=f,amount=c,action='pending')
            d2.update(action='canceled')
            d3 = cancel.objects.create(name=a,amount=c,action='pending',phone=e)
            d3.save()
            d1 = orders.objects.filter(name=a)
            return render(request, 'order2.html', {'r': d1})

        elif b== 'refund':
            c = request.POST['n2']
            d=cancel.objects.filter(name=a,amount=c,action='pending',phone=int(request.POST['n3']))
            d.update(action='confirm')
            d=cancel.objects.all()
            return render(request,'cancel.html',{'r':d})




    else:
        return HttpResponse("error")

#admin page
def list(request):
    d = d = employee.objects.all()
    return render(request,'emplist.html',{'r':d})

def adm(request):
    d = employee.objects.all()
    return render(request, 'admn.html', {'r': d})
def order(request):
    d = detail.objects.all()
    return render(request, 'order.html', {'r': d})
def delivr(request):
    d3 = detail.objects.all()
    return render(request,'delivr.html',{'r':d3})

def refund(request):
    d=cancel.objects.all()
    return render(request,'cancel.html',{'r':d})

#end admin


#payment
def payment(request):
    e = request.session['id']
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['adress']
        d = request.POST['phone']
        d2=price.objects.get(name=e,payment='pending')
        y=d2.total
        x=d2.total*100
        z=datetime.datetime.now().strftime("%Y-%m-%d")
        d1 = detail.objects.create(name=a, email=b, adres=c, phone=d, nme=e,action='pending',emp='',amount=y,q1=d2.q1,q2=d2.q2,q3=d2.q3,q4=d2.q4,datee=z)
        d1.save()
        return render(request, 'payment.html',{'r':x})
    else:
        return HttpResponse("error")

def payment1(request, id):
    e = request.session['id']
    d=price.objects.get(name=e,action='pending',payment='pending')
    amount = d.total
    order_currency = 'INR'
    client = razorpay.Client(
    auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    cursor = connection.cursor()
    cursor.execute(
    "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(
    id) + "' ")

    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, "payment.html")
def success(request):
    a= request.session['id']
    d = price.objects.filter(name=a, action='pending', payment='pending')
    d.update(payment='complete')
    d1 = price.objects.filter(name=a, payment='complete')
    b=0
    c=0
    b1=0
    b2=0
    amt=0
    ph=0
    for i in d1:
        b = i.q1
        c = i.q2
        b1 = i.q3
        b2 = i.q4
        amt=i.total
    d = detail.objects.filter(nme=a,amount=amt,action='pending')
    for i in d:
        print(i.phone)

        ph=i.phone
    z = datetime.datetime.now().strftime("%Y-%m-%d")
    d2 = orders.objects.create(name=a, q1=b, q2=c, q3=b1, q4=b2, action='pending',amount=amt,phone=ph,datee=z)
    d2.save()
    return render(request,'success.html')
#end payment

#delivery

def deliver(request):
    if request.method == 'POST':
        n=''
        a=request.POST['n1']
        b=request.session['id']
        amt=int(request.POST['n2'])
        b1=employee.objects.filter(name=b,status=2,action='confirm')
        c=0
        for i in b1:
            c=i.deliver
            c+=1
        b1.update(deliver=c)
        d=detail.objects.filter(name=a,action='pending',amount=amt)
        d.update(action='confirm',emp=b)
        d = detail.objects.filter(name=a, action='confirm', amount=amt)
        for i in d:
            n=i.nme
        d1=price.objects.filter(name=n,action='pending',total=amt)
        d1.update(action='confirm')
        d2=orders.objects.filter(name=n,amount=amt)
        d2.update(action='delivered')
        d3=detail.objects.all()
        return render(request,'order1.html',{'r':d3})
    else:
        return HttpResponse("error")


def order2(request):
    a = request.session['id']
    d1 = orders.objects.filter(name=a)
    return render(request, 'order2.html', {'r': d1})




#social media
def facebook(request):
    return redirect('https://www.facebook.com/YourFacebookPage')
def twitter(request):
    return redirect('https://www.twitter.com/YourTwitterPage')
def instagram(request):
    return redirect('https://www.instagram.com/YourIstagramPage')


#forgotpassword
def forgot(request):
    return render(request,'email.html')


def changepassword(request):
    return render(request,'chngpaswd.html')

def changepassword1(request):
    if request.method == 'POST':
        c=request.session['id']
        a= request.POST['n1']
        b = request.POST['n2']
        if a == b:
            d = logi.objects.filter(name=c)
            d.update(pswd=a)
            return render(request, 'chngpaswd.html')

        else:
            return render(request,'chngpaswd.html')

def mail(re):
    if re.method == 'POST':
        a=re.POST['name']
        b = re.POST['email']
        c=re.POST['phone']
        d=re.POST['message']
        z = datetime.datetime.now().strftime("%Y-%m-%d")
        d1=concent.objects.create(name=a,email=b,phone=c,message=d,date=z)
        d1.save()
    return render(re,'contact1.html')

def inbox(request):
    d = concent.objects.all()
    return render(request,'inbox.html',{'r':d})

# ------------------- PASSWORD FUNCTIONS STARTS ---------------------


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            userr = user.objects.get(emaill=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=userr, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'password_reset_sent.html')

# def resetpage(r,token):
#     return render(r, 'reset_password.html')

def reset_password(request, token):
    # Verify token and reset the password
    password_reset = PasswordReset.objects.get(token=token)
    usr = user.objects.get(id=password_reset.user_id)
    return render(request, 'reset_password.html',{'token':token})

def reset_password2(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    usr = user.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('repeatpassword')
        if repeat_password == new_password:
            password_reset.user.pswd = new_password
            password_reset.user.save()
            password_reset.delete()
            return redirect(login)
    return render(request, 'reset_password.html')

# ------------------- PASSWORD FUNCTIONS ENDS ---------------------





