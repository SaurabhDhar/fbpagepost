from django.shortcuts import render
import facebook
# Create your views here.


def sharing(request):
    
    access_token = 'EAAcGqZCEr6pgBAPZBpL0tNICvrjeCyHZBgwTHMZA4ZAItMrQ9VjMgZAR24m5EDEH32bMpPJba1ZA9dqTnzaZBSPSL5c5VG7VFJtlZAoENYhiFtN8XzqyOMOoJgriCWqPm55JtIwZBJ6xDn8RV8GpNe1sMSNYu513TrU0oAq1IVvmu2sO3NecQ37OWZAjJZBo13eZAt0glQDZCthW1KUBahtFGzyZCRnhpmQbGZB8zH3yY6tpEp4QUvyhe99ZAHOnz'

    if request.method == 'POST':
        fb = facebook.GraphAPI(access_token)
        fb.push_wall_post("This is test post by python...")
    
    return render(request, 'sharing.html')