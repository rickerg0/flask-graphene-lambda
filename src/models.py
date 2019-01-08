import graphene

class User(graphene.ObjectType):
    _id = graphene.ID()
    firstname = graphene.String()
    lastname = graphene.String()
    age = graphene.Int()
    
    def __init__(self,id,fname,lname,age): 
        self._id = id
        self.firstname = fname
        self.lastname = lname
        self.age = age
      
 
 
class DB(graphene.ObjectType):
      
    def find_user_by_id(self,id):
        user = User(id,'bob','smith',23)
        
        return user
        
              
if __name__ == '__main__':
    pass
