from django.shortcuts import render
import facebook
import json
# Create your views here.


def sharing(request):
    access_token = 'EAAEEP5iPQosBAA0I1jJ7aSVY4OL7hZBM0kTugRJM4c428ZCUUkfLY3uhxSkRpNo2txzV6ZCXP0IqJK7OYAtf72W45tBmPdQBX07P5Hv3QbY5UQz1HoVoGtTC54MzBPIWKchnyd7TPqAIobTi782gs1VNBE5GtPdRBo37BITlxwymmCyIW57fIFVa4ggWGT6uxsjKDyKyZCYaz9FMWyt5'
    
    graph = facebook.GraphAPI(access_token)
    print(graph)
    graph.put_object(parent_object='me', connection_name='feed',
                  message='Hello, world')
    
    return render(request, 'sharing.html')