import facebook
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



# Create your views here.

User = get_user_model()

def sharing(request):
   social = request.user.social_auth.get(provider='facebook')
   

   access_token = social.extra_data['access_token']
   # access_token = 'EAADNuxn7q1wBANUNbvXf8Lm0nTJvnamD2tfGpkR35CKQk8XpiFLjF8ZBW8qtwhJOE9g3AePqQ1H6xZCZBtAhUEdVNHD9Kw69l6Nb9gmqs9sZCX0QQKgnZBNmzh63D7zjg9f5HQEctbJjrnykbKkWqefs8ipWT5MA9IYlC13NWtgcPd5oresf2PXQZBX3E6rFjNl5NaC5QnZATKcXFqXCatg'
   graph = facebook.GraphAPI(access_token)
   # page_id = social.extra_data['id']
   
   if request.method == 'POST':

      content = request.POST.get('content')

      graph.put_object(parent_object='me', 
                           connection_name='feed',
                           message=content) # data yazmaq ucun

   return render(request, 'sharing.html')



def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  
   return render(request, 'home.html')


          