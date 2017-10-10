from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


# 새로운 post 생성
def write(request):
    # 저장 또는 발행하기 버튼을 누른 경우 (POST)
    if request.method == "POST":
        # 두 경우 모두, 일단 DB에 새로 생성된 Post를 저장한다
        post = Post.objects.create(
            author=User.objects.get(username='markkim'),
            title=request.POST.get('title'),
            delta_content=request.POST.get('answer_delta'),
        )

        # post를 save한 경우 (save - default published=False)
        if request.POST.get('action') == "save":
            return redirect('quill:post_edit', username=post.author.username, pk=post.pk)
        # post를 publish한 경우 (published=True)
        elif request.POST.get('action') == 'publish':
            post.publish()
            return redirect('quill:published_list')

    # 처음 글쓰기 페이지로 온 경우 (GET)
        return render(request, 'quill/post_form.html')
        # return HttpResponse('opens a text editor to publish/save posts')


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
    # 저장 또는 발행하기 버튼을 누른 경우 (POST)
    if request.method == "POST":
        # 두 경우 모두, 일단 DB에 수정된 Post를 저장한다
        post = Post.objects.get(
            author=User.objects.get(username='markkim'),
            pk=pk
        )
        post.title = request.POST.get('title')
        post.delta_content = request.POST.get('answer_delta')

        post.save()

        # post를 save한 경우 (save - default published=False)
        if request.POST.get('action') == "save":
            # 빈 response를 보내준다
            return HttpResponse(status=204)
        # post를 publish한 경우 (published=True)
        elif request.POST.get('action') == 'publish':
            post.publish()
            return redirect('quill:published_list')

    # 처음 수정 페이지로 온 경우 (GET)
    else:
        post = Post.objects.get(author=User.objects.get(username=username), pk=pk)
        context = {
            'post': post
        }
        return render(request, 'quill/post_edit_form.html', context)
