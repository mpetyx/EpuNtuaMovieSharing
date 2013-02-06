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
    
    def myposts(self):
        
        # Get my latest posts
        posts = self.graph.get('me/posts')