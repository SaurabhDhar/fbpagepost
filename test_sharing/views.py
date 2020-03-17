from django.shortcuts import render
import facebook
import json
# Create your views here.


def sharing(request):
    access_token = 'EAAEEP5iPQosBAPfGiq7KkHDchEjBwv3zbGlO9wFtQonvT0ccYDHPn0O6qX2XwIDhwczYhAQCmjzmsNEZAzxzVyi0K7UVZBe4yIk1lLGpMR2DbuVjvB0z0wMp27lwgzVTqDcow5lYCWyQRwiUZCbEPQZBlKAdjbgS0UrsuZBWp9i2rjEcnTtJiO3nFcKVp6OUrLuvzVMR0LHPZCt7pRTF70'
    
    graph = facebook.GraphAPI(access_token)
    print(graph)
    graph.put_object(parent_object='me', connection_name='feed',
                  message='Hello, world')
    
    return render(request, 'sharing.html')