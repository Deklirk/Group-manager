from django.shortcuts import render

def member_list(request):
    return render(request, 'memberaccount/member_list.html', {})