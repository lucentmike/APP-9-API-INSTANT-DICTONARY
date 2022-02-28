import justpy as jp
import definition
import json
import requests

class API:
    """Handles reqeuests at /api?w=moon"""

    @classmethod 
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        defined = definition.Definition(word).get()
        payload =  { 
            
            "word":word,
            "defined":defined
            
        }    

        wp.html = json.dumps(payload)
        return wp 


jp.Route("/api", API.serve)
jp.justpy()