from django.shortcuts import render

def articleAccueil(request):
    return render(request,"article/accueil.html")

def desc(request):
    return render(request,"article/pk.html")

def qui(request):
    return render(request,"article/qui.html")

def oudonner(request):
    return render(request,'article/oudonner.html')

def prendrerdv(request):
    return render(request,'article/prendrerdv.html')

def contact(request):
    return render(request,'article/contact.html')
