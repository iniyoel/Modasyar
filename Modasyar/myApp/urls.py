from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="Dashboard"),
    path("logged", views.homelogged, name="dashboardlogged"),
    path("aboutUs/", views.aboutus, name="aboutus"),
    path("aboutUslogged", views.aboutUslogged, name="aboutUslogged"),
    path("login/", views.login, name="login"),
    path("explore/", views.explore, name="explore"),
    path("explorelogged", views.explorelogged, name="explorelogged"),
    path("transaction", views.transaction, name="transaction"),
    path("tingkatkanmodal/", views.tingkatkanmodal, name="tingkatkanmodal"),
    path("umkmprofile/", views.umkmprofile, name="umkmprofile"),
    path("userdetail/", views.userdetail, name="userdetail"),
    path("userdashboard/", views.userdashboard, name="userdashboard"),
    path("investporto/", views.investporto, name="investporto"),
    path("detailporto/", views.detailPorto, name="detailporto"),
    path("growth/", views.growth, name="growth"),
]