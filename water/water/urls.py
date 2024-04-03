"""
URL configuration for water project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.profile),
    path('about.html', views.about),
    path('index.html', views.display),
    path('contact.html', views.contact),
    path('shop.html', views.shopp),
    # path('checkout.html', views.checkout),
    path('login.html', views.login),
    path('reg.html', views.register),
    path('cancel1', views.cancel1),
    path('cancel2', views.cancel2),
    path('cancel3', views.cancel3),
    path('cancel4', views.cancel4),
    path('reg', views.reg),
    path('log', views.login1),
    path('logout', views.logout),
    path('about1.html', views.about1),
    path('index1.html', views.display1),
    path('contact1.html', views.contact1),
    path('shop1.html', views.shop1),
    path('checkout1.html', views.checkout1),
    path('cart1.html', views.cart1),
    path('crt1.html', views.crt1),
    path('crt2.html', views.crt2),
    path('crt3.html', views.crt3),
    path('crt4.html', views.crt4),
path('crt11.html', views.crt11),
    path('crt21.html', views.crt21),
    path('crt31.html', views.crt31),
    path('crt41.html', views.crt41),
    path('cart', views.cart2),
    path('empreg.html', views.empreg),
    path('empreg', views.empreg1),
    path('reject', views.reject),
    path('emplist.html', views.list),
    path('order.html', views.order),
    path('order1.html', views.order2),
    path('admn.html', views.adm),
    path('ordr', views.payment),
    path('dlvr', views.deliver),
    path('success', views.success),
    path('cancel.html', views.refund),
    path('forgot.html', views.forgot),
path('mail.php', views.mail),
path('inbox.html', views.inbox),

    path('deliver.html', views.delivr),
    path('facebook', views.facebook),
    path('twitter', views.twitter),
    path('instagram', views.instagram),

   # forgot password
    path("forgot",views.forgot_password,name="forgot"),
    path("reset/<token>",views.reset_password,name="reset"),
    path("reset/reset2/<token>",views.reset_password2,name="reset2"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)