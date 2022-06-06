import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['email', 'contents']


def index(request):
    return render(request, 'index/index.html', context={
        'comment': CommentForm()
    })


def first(request):
    return render(request, 'index/first.html')


def second(request):
    return render(request, 'index/second.html')


def third(request):
    return render(request, 'index/third.html')


def reg(request):
    return render(request, 'index/reg.html')


def auto(request):
    return render(request, 'index/reg.html')


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(json.loads(request.body))
        if form.is_valid():
            Comment.objects.create(**form.cleaned_data)
            return HttpResponse("Created")
        else:
            return HttpResponse("Bad request", status=400)
    else:
        return HttpResponse("Bad method", status=400)


def get_comments(request):
    comments = Comment.objects.all()
    result = []
    for comment in comments:
        result.append({
            "email": comment.email,
            "contents": comment.contents,
        })
    return HttpResponse(json.dumps(result))
