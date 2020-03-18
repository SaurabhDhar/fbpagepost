from django.shortcuts import render
import facebook
import json
# Create your views here.


def sharing(request):
   access_token = 'EAAEEP5iPQosBAPDsctIxab9wZApXEt6PLkKMlpvDULMZAYdN4sSgwBgwrJDelaZCDnYUO2FFSZCbXpZCmNDm1wfV5veqPfhRzxZAt4kjn0nHgUgGDrBT9GKTKcy6KcyhUKwj1yFXszqqFJmRnLG1i5RNOpfXJJv9g1ELnPZBeqrI9NFAX0HWCtvEmYQb7idXBZADJqPSj5LAQcTY3ESZB9k0s'
    
   graph = facebook.GraphAPI(access_token)
   
   if request.method == 'POST':

      content = request.POST.get('content')

      graph.put_object(parent_object='me', 
                           connection_name='feed',
                              message=content) # data yazmaq ucun

   return render(request, 'sharing.html')