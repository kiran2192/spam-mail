"""spammail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from siteadmin import views as adminview
from user import views as userview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"),
    path('login/',adminview.login,name="login"),
    path('loginaction/',adminview.loginaction,name="loginaction"),
    path('hobby/',adminview.hobby,name="hobby"),
    path('hobbyaction/',adminview.hobbyaction,name="hobbyaction"),
    path('hobbyfactor/',adminview.hobbyfactor,name="hobbyfactor"),
    path('hobbyfactoraction/',adminview.hobbyfactoraction,name="hobbyfactoraction"),
    path('register/',userview.register,name="register"),
    path('getstate/',userview.getstate,name="getstate"),
    path('registeraction/',userview.registeraction,name="registeraction"),
    path('season/',adminview.season,name="season"),
    path('seasonaction/',adminview.seasonaction,name="seasonaction"),
    path('seasonfactor/',adminview.seasonfactor,name="seasonfactor"),
    path('sfactoraction/',adminview.sfactoraction,name="sfactoraction"),
    path('scountry/',adminview.scountry,name="scountry"),
    path('getstates/',adminview.getstates,name="getstates"),
    path('getfactor/',adminview.getfactor,name="getfactor"),
    path('scountryaction/',adminview.scountryaction,name="scountryaction"),
    path('agefactor/',adminview.agefactor,name="agefactor"),
    path('agefactoraction/',adminview.agefactoraction,name="agefactoraction"),
    path('sendmessage/',userview.sendmessage,name="sendmessage"),
    path('checkreceivername/',userview.checkreceivername,name="checkreceivername"),
    path('sendmessageaction/',userview.sendmessageaction,name="sendmessageaction"),
    path('viewsendmessage/',userview.viewsendmessage,name="viewsendmessage"),
    path('deletemsg<int:id>/',userview.deletemsg,name="deletemsg"),
    path('inbox/',userview.inbox,name="inbox"),
    path('movetotrash/',userview.movetotrash,name="movetotrash"),
    path('viewtrash/',userview.viewtrash,name="viewtrash"),
    path('delmsg<int:id>/',userview.delmsg,name="delmsg"),
    path('forwardmsg<int:id>/',userview.forwardmsg,name="forwardmsg"),
    path('forwardmsgaction/',userview.forwardmsgaction,name="forwardmsgaction"),
    path('replymsg<int:id>/',userview.replymsg,name="replymsg"),
    path('replymsg/',userview.replymsgaction,name="replymsgaction"),
    path('contact/',userview.contact,name="contact"),
    path('contactaction/',userview.contactaction,name="contactaction"),
    path('checkcntct/',userview.checkcntct,name="checkcntct"),
    path('viewcontact/',userview.viewcontact,name="viewcontact"),
    path('delcontact<int:id>/',userview.delcontact,name="delcontact"),
    path('blacklist/',userview.blacklist,name="blacklist"),
    path('blacklistaction/',userview.blacklistaction,name="blacklistaction"),
    path('viewblacklist/',userview.viewblacklist,name="viewblacklist"),
    path('delblcklist<int:id>/',userview.delblcklist,name="delblcklist"),
    path('movetoblacklist<int:id>/',userview.movetoblacklist,name="movetoblacklist"),
    path('customerhobby/',userview.customerhobby,name="customerhobby"),
    path('getfctr/',userview.getfctr,name="getfctr"),
    path('customerhobbyaction/',userview.customerhobbyaction,name="customerhobbyaction"),
    path('customeragefactor/',userview.customeragefactor,name="customeragefactor"),
    path('customeragefactoraction/',userview.customeragefactoraction,name="customeragefactoraction"),
    path('cseasoncountry/',userview.cseasoncountry,name="cseasoncountry"),
    path('cscountryaction/',userview.cscountryaction,name="cscountryaction"),
    path('viewspam/',userview.viewspam,name="viewspam"),
    path('delspam<int:id>/',userview.delspam,name="delspam"),
    path('updateprofile/',userview.updateprofile,name="updateprofile"),
    path('updateprofileaction/',userview.updateprofileaction,name="updateprofileaction"),
    path('logout/',userview.logout,name="logout"),
    path('forgotpassword/',adminview.forgotpassword,name="forgotpassword"),
    path('forgotpasswordaction/',adminview.forgotpasswordaction,name="forgotpasswordaction"),
    path('newpasswordaction/',adminview.newpasswordaction,name="newpasswordaction"),
    path('resetpasswordaction/',adminview.resetpasswordaction,name="resetpasswordaction")

]
