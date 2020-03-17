from django.shortcuts import render
import facebook
import json
# Create your views here.


def sharing(request):
    access_token = 'EAAEEP5iPQosBANYZC885XTn1vXkmWS21WRycE5wmewZANT1m68MIf39GtDrH3FXJVaTvRt6R0S09M5m8eKv7wQkyxl6IaEdCmHwuv5mZCC3nflcCoUr4wJqVJHFZBj7lD8HFpCcut595srbUiPn7eFVSwcBPjM77SIGrRj0SCcoscAgN2OvnVMbq65P3KSyr1IEZClUaOKyxxu5FHgyOx'
    
    if request.method == 'POST':
        graph = facebook.GraphAPI(access_token)
        print(graph)
        # profile = graph.put_object(parent_object="me", connection_name="feed", message = "Hello World")
        # print(profile)
    
    return render(request, 'sharing.html')