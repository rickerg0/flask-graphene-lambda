

class ClientQuery(object):
    
        def __init__(self,name,arg={}):
            self.name = name
            self.arg = arg 

  		  
        def getQuery(self,key, value):
                temp=''
                query = '{' + self.name +' ( '+key +':'+value +') {'
               
                for key in self.arg:
                   temp += key+': "' +self.arg[key]+'"'
                   
                query += temp +' ) }'
               
                return query

	  
        def addQueryParams(self,name,value ):
	           self.arg[name] = value
               
        def addSearchParams(self,name,value, id):
               self.arg[name] = value+'('+id+ ')'
               
     
 

   