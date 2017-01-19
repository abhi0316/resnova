import sys
print "helloworld"
print "sys argument",sys.argv[1]

if len(sys.argv)>1:
	print "argv greater than one"
else:
	print "argv lesser than one"

