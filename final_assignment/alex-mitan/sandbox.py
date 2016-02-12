import urllib2
response = urllib2.urlopen('https://www.example.com/')
file_content = response.read()

print file_content