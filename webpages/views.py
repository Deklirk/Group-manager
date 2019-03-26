from django.shortcuts import render
from django.utils import timezone
from .models import Home_page, Messages

def index(request):
	home_data = Home_page.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
	message = Messages.objects.all()
	
	return render(request, 'index.html', {'home_data': home_data, 'messages':message})