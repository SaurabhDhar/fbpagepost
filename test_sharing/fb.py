import facebook
access_token = "EAANLZCsMhezQBAOpQMRBqeReyqF9bo3cg767iRd4jRYTlwSXWh8N1iahmNMGGOEZAKgQCtQYbZBKsd9Rp0dH12M9i7hSMj3DUZBPwYYDGuisv6lEfzyVzBHCeMl8NBDod0mBZBqsfQw18052RAY1VzeI6ZACAfkdXytHNPwQ18At9QDF9x10aZBvLFyHEHrxOZCticSBuEHZAtwZDZD"
graph = facebook.GraphAPI(access_token)

graph.put_object(parent_object='me',
                 connection_name='feed',
                 message='necesen')
