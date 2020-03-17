from django.shortcuts import render
import facebook
import json
# Create your views here.


def sharing(request):
    access_token = 'EAAXtqYRjczYBAImuXn1uvj3UhZB4wl1GQRKZAZBDLl5E1ExCSvcii473vsyuH1A4iI8GRdcjEWbCceZC0uYQmfrcCffZCPzfEZApVnpZAios6xhwS4P0ELc3qpQKcSAWNtiDCGbcAJuqwfaqdwvEElS8CgESPoqRb8lSstHYTHQUSJy3UZBjDf93rxSSvaJHYowZD'
    
    graph = facebook.GraphAPI(access_token)
    print(graph)
    graph.put_object(parent_object='me', connection_name='feed',
                  message='Hello, world')
    
    return render(request, 'sharing.html')