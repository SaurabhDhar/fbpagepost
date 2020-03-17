from django.shortcuts import render
import facebook
import json
# Create your views here.


def sharing(request):
    access_token = 'EAAEEP5iPQosBAKonh85B4kB1nokkM9ZA4wtJq3VfEzrbEdShlcQyWsK2AAMylRRZCqClgz3Fr5I93YyJt3dyvES9ZBWDh9kISpjoe24Ul06PXPzGezhdvBfsaUTQVNxK4D7yZAKPqY8uIPd8SKo26jUOnkWjtOqmufZBKfDQRfk157t6I8cZCTPABmUFaoJroawdpD0T5H12oZC0MBZC3LObZA9hcAX3RMLr33adj5k7OE9SnZCkibsUMi'
    
    graph = facebook.GraphAPI(access_token)
    print(graph)
    content = graph.get_object('me', fields='name')
    context = {
       'content':content
    }
    
    return render(request, 'sharing.html',context)