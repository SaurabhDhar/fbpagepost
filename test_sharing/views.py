from django.shortcuts import render
import facebook
import json
# Create your views here.


def sharing(request):
   access_token = 'EAAEEP5iPQosBAOiKZCfA5wK0KTUIg9E2DZAKXCGKbfi8Lpd4q3fZCOrfJmsCLaasQkQTMZAlYlxNfyWNoA3u4iYEzJbSsSHNAUhYhTiXezrbdjsBk0VQOdT3Vi6ZCU5VMCN1jjEbwGpxXGbczJgQrBjLZBeLEicuAyT7mkXGhBXSZBAIUCSZAGdrfe4ZCe5TZChYhNCxgE8m6fuAGdlopp3Uue'
    
   graph = facebook.GraphAPI(access_token)
   
   if request.method == 'POST':
      content = request.POST.get('post')
      graph.put_object(parent_object='me', 
                           connection_name='feed',
                              message=content) # data yazmaq ucun

   return render(request, 'sharing.html')