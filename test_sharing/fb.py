import facebook
access_token = "EAANLZCsMhezQBACKy1QMotIEUcN0EixXoju3iXp08xp2ZBLtyX6g6NJeZAw0O5MVWfAIphPYJQnwcZBqGNJVCpSZCQ50lBEXLo4OAG1wmChloWqjCNtr31J4yiqrc3kHuTaOMejEIrmXJukZC5BFXVL9AxHvKZAvT2vkgrqPZB4BHIffYuwyfNTjoiDSwxXvEy4RWuYjnADfaBr0luAoTHlbQca3bR77g9XEVZCJxNfCn0gZDZD"
graph = facebook.GraphAPI(access_token)

graph.put_object(parent_object='me',
                 connection_name='feed',
                 message='Hello Guys')
