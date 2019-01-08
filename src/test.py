import graphene
import json
import Query

quser = '''query getUser(){ user(_id:12) {
          _id
         firstName 
         lastname 
         age 
     }
  } '''

print(quser)

result =  Query.myschema.execute(quser)#,variable_values={'_id': 12},)


