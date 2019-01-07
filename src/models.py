import graphene

class User(graphene.ObjectType):
    id = graphene.ID()
    firstname = graphene.String()
    lastname = graphene.String()
    age = graphene.Int()
    
    
if __name__ == '__main__':
    pass
