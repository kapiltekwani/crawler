import urllib2,URLLister,pymongo,urllib
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from crawler import extractURL
DBName="param3"
collection="links"
urlstr=raw_input()
extractURL(DBName,collection,urlstr)

print urlstr
