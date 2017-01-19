import httplib
import urllib
a=httplib.HTTPSConnection('www.quora.com')

a.request("GET","/")
w=a.getresponse()
print(w.status,w.reason)
print w.read()

print "............................................................................"





s=urllib.urlretrieve('http://www.google.com')
print s.read()

