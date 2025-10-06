from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')
def succes_login(request):
    return render(request, 'succes_login.html')