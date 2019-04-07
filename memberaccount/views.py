from django.shortcuts import render
from django.utils import timezone
from .models import Member_share
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):	
	members_shares = Member_share.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
	group_members = User.objects.all().count()

	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	context = {
		'members_shares':members_shares, 
        'group_members': group_members,
        'num_visits': num_visits,
    }

	return render(request, 'memberaccount/member_dashboard.html', context = context)

@login_required
def members_list(request):	
	group_members = User.objects.filter(date_joined__lte=timezone.now()).order_by('date_joined')
	
	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	context = {
        'group_members': group_members,
        'num_visits': num_visits,
    }

	return render(request, 'memberaccount/members_list.html', context = context)

@login_required
def accounts_balances(request):	
	members_shares = Member_share.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
	
	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	context = {
        'group_members': group_members,
        'num_visits': num_visits,
    }

	return render(request, 'memberaccount/accounts_balances.html', context = context)