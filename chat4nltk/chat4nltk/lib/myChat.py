from nltk.chat.util import Chat

import random
import re

class myChat(Chat):
 
    def respond(self, str):
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            if match is not None:
                if type(response) is list or tuple:
                    resp = random.choice(response)
                else:
                    resp = response
                    
                # process wildcards and fix munged punctuation at the end                
                resp = self._wildcards(resp, match) 
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                
                return resp
