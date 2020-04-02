import facebook
import json
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialToken,SocialAccount
import requests
from django.utils.html import strip_tags

def login(request):
   return render(request, 'login.html')


@login_required
def add_post(request):
    form = PostForm
    context = {
        'form' : form
    }

    if request.method == 'POST':
        if request.is_ajax():

            content = request.POST.get("content")
            postid = request.POST.get("postid")
            if postid == 'none':

                if content != '':
                    test = Post.objects.create(description=content)
                    id = test.id
                    return JsonResponse({
                        'id': id
                    })
            else:

                test = Post.objects.filter(id=int(postid)).last()
                test.description = content
                test.save()
                return JsonResponse({
                    'status':'oke'
                })
        redirect('home')

    return render(request, 'post_form.html', context)

@login_required
def sharing(request):

   sosial = SocialToken.objects.filter(account = 3).last()
   social_user = SocialAccount.objects.filter(user=4).last()
   print(social_user)
   user_id = social_user.uid
   user_token = sosial.token
   response = requests.get(f"https://graph.facebook.com/{user_id}/accounts?fields=name,access_token&access_token={user_token}").json()
   print(response)
   context = {
      'data':response['data']
   }

   if request.method == 'POST':
      content = Post.objects.all()
      print(strip_tags(content))
      if content == "":
         redirect('home')

      else:
         access_token = request.POST.get('pages')
         graph = facebook.GraphAPI(access_token)

         graph.put_object(parent_object='203694849725749',
                        connection_name='feed',
                        message=strip_tags(content)) # data yazmaq ucun

   return render(request, 'sharing.html',context)
