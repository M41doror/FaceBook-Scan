import urllib2
import re

class FacebookIdHandler(object):
    """Class to use facebook id's to retreive other useful pieces of information"""
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)
    
    def retreive_email(id):
        url = "http://facebook.com/profile.php?id="+str(id)
        try:
            u = urllib2.urlopen(url)
            e = re.compile('<title*[^>]*>.*</title*>')
            data = u.read()
            
            current =  e.findall(data)

            if "Unavailable" in current[0] or "Not Found" in current[0]:
                return "Profile url not found"
            else:
                match = re.search(r'URL=/?([^?>]+)',data)
                return newemail
        except:
                return "Profile url couldn't be retreived due to an exception"
        return null

