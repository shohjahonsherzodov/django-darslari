from django.views import View
from django.shortcuts import render

class LandingPageView(View):
    def get(self, request):
        return render(request, 'landing_page.html')