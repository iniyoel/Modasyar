from django.shortcuts import render

def home(request): 
    return render(request, "myApp/Dashboard.html")

def homelogged(request):
    return render(request, "myApp/Dashboard-logged.html")

def login(request):
    return render(request, "myApp/Login.html")

def explore(request):
    return render(request, "myApp/exploreUMKM.html")

def explorelogged(request):
    return render(request, "myApp/exploreUMKM-logged.html")

def tingkatkanmodal(request):
    return render(request, "myApp/tingkatkan-modal.html")

def umkmprofile(request):
    return render(request, "myApp/profilUMKM.html")

def transaction(request):
    return render(request, "myApp/transaksi.html")

def userdetail(request):
    return render(request, "myApp/user-profile-detail.html")

def userdashboard(request):
    return render(request, "myApp/user-dashboard.html")

def aboutus(request):
    return render(request, "myApp/aboutUs.html")

def aboutUslogged(request):
    return render(request, "myApp/aboutUs-logged.html")

def investporto(request):
    return render(request, "myApp/invest-portofolio.html")

def detailPorto(request):
    return render(request, "myApp/detail-porto.html")

def growth(request):
    return render(request, "myApp/bisnis-growth.html")