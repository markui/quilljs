from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# 새로운 post 생성
def write(request):
    return HttpResponse('opens a text editor to publish/save posts')

# 저장된 post_list page
def ready_list(request):
    return HttpResponse('shows a list of saved posts')

# 발행된 post_list page
def published_list(request):
    return HttpResponse('shows a list of published posts')

# post_detail page
def post_detail(request, username, pk):
    return HttpResponse(f'show the detail of a saved or published post {pk} by {username}')

# post_edit page - 기존의 post 수정
def post_edit(request, username, pk):
    return HttpResponse(f'open a text editor to previous published/saved post {pk} by {username} with previous data inside')


