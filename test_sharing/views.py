import facebook
import json
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialToken,SocialAccount
import requests


# Create your views here.

@login_required
def sharing(request):
   sosial = SocialToken.objects.filter(account = 1).last()
   social_user = SocialAccount.objects.filter(user=request.user.id).last()
   user_id = social_user.uid
   user_token = sosial.token
   response = requests.get(f"https://graph.facebook.com/{user_id}/accounts?fields=name,access_token&access_token={user_token}").json()
   context = {
      'data':response['data']
   }
   
   
      
   if request.method == 'POST':
      content = request.POST.get('content')
      if content == "":
         redirect('home')
      
      else:
         access_token = request.POST.get('pages')
         graph = facebook.GraphAPI(access_token)
            
      

         graph.put_object(parent_object='me', 
                        connection_name='feed',
                        message=content) # data yazmaq ucun
   return render(request, 'sharing.html',context)



def login(request):

   return render(request, 'login.html')


def home(request):
  
   return render(request, 'home.html')


          


