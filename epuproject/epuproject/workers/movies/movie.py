'''
Created on Feb 6, 2013

@author: mpetyx
'''

from epuproject.workers.thing import Thing

class Movie(Thing):
    
    def __init__(self):
        
        if not self.Movie.exists():
            self.add()
            
    
    def add(self):
        """
            add new movie
        """