'''
Created on Feb 6, 2013

@author: mpetyx
'''

import facepy
import allauth

from facepy import GraphAPI

class PersonalProfile():
    
    def __init__(self, request):
        # Initialize the Graph API with a valid access token (optional,
        # but will allow you to do all sorts of fun stuff).
        
        from allauth.socialaccount import SocialToken
        oauth_access_token= SocialToken.objects.get(account = request.user.username).token
        
        self.graph = GraphAPI(oauth_access_token)
        
    def userProfile(self):
        
        from py2neo import neo4j
        graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
        
        self.user = graph_db.create_node({
                "name"          : "Bob Robertson",
                "date_of_birth" : "1981-07-01",
                "occupation"    : "Hacker"
            })
        
        people = graph_db.create_node()
        people.create_relationship_to(self.user, "PERSON")
    
    def myposts(self):
        
        # Get my latest posts
        posts = self.graph.get('me/posts')
        
    def friends(self):
        
        for friend in friends:
            myfriend = Thing(friend)
            friendship = self.user.create_relationship_to(myfriend, "KNOWS")