import urllib2, URLLister,pymongo,urllib
from pymongo import Connection
#from linkcheck import LinkChecker
from pymongo.errors import ConnectionFailure

def extractURL(DBName,collection,urlstr):
	#urlstr=raw_input()
	c=Connection('localhost',27017)
	dbh=c[DBName]

	urllist=[]
	cursor=dbh[collection].find()
	count=cursor.count()+1

	
	
	dbh[collection].save({"id":count,"parent-URL":urlstr,"child-URL":urlstr })
	pid=count
	#cursor=dbh[collection].find({"parent-URL":urlstr,"child-URL":urlstr})	
	#Code to read from Database list of URLS in the form of loop
	#cursor=dbh[collection].find()
	while True:
		#urlstr= doc["child-URL"]
		
		
		usock = urllib.urlopen(urlstr)
		parser = URLLister.URLLister()
		parser.feed(usock.read())         	
		usock.close()                     
		parser.close()	
		countchild =8

		for url in parser.urls: 
			countchild=countchild-1
 			if countchild<0:
				break			

			chkpresent=dbh[collection].find({'child-URL':url})			
			if chkpresent.count()== 0:
				count=count+1			
				dbh[collection].save({"id":count,"parent-URL":urlstr,"child-URL":url })
				print "{Parent-URL:"+urlstr+"     Child-URL:"+url+" }"

		cursor=dbh[collection].find({'id':{"$gt":pid}})
			
		if cursor.count()>0:
			
			for url1 in cursor:
				print "\n"
				print "the URL being scrapped: "+url1["child-URL"]
				urlstr=url1["child-URL"]
				pid=url1["id"]
				if urlstr[0]!='/':
	
				        break
		else:
			break
        c.disconnect()
	


