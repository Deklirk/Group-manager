from django.shortcuts import render
from django.utils import timezone
from .models import Member_share

#@login_required

def dashboard(request):	
	members = Member_share.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
	return render(request, 'memberaccount/member_dashboard.html', {'members':members})