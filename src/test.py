import graphene
import json
import Query

quser = """
 { user(id: $id) {
     firstName 
     lastName 
     age 
     }
  }'
 """
query = """
 query { user  }
 """ 
print(quser)
result = Query.schema.execute('{ user }',quser,variable_values={'id': 12},)


