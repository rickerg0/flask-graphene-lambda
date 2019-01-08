import graphene
from  models import User

class Query(graphene.ObjectType):
    


    user =  graphene.Field(User,_id =graphene.ID()) #, dict(_id=graphene.String(required=True)))
    
    def resolve_user(self, info,_id):
        print('resolve_user')
       # user = info.context.get('user')
        #temp = find_user_by_id(dict(_id=id))
          # do the simple filted
       #resolved_fileds = {f: user[f]
        #                   for f in User._meta.fields}
        #user = User(**resolved_fileds) if user else None
        return hero

myschema = graphene.Schema(query=Query)

if __name__ == '__main__':
    pass
