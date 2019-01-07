import graphene
from  models import User

class Query(graphene.ObjectType):
    user = graphene.Field(User)
    
    def resolve_user(self, info):
    
        print(info)
        
        return user

    
schema = graphene.Schema(query=Query)


if __name__ == '__main__':
    pass
