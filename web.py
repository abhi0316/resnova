import httplib
a=httplib.HTTPConnection("www.google.com")
q=a.getresponse()
print q.status()
print q.reason()

