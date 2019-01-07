from flask import Flask
import json
import Query
from clientQuery import  ClientQuery

app = Flask(__name__)


@app.route('/')
def default():
    print("hello")
    #result = schema.execute('{ hello }')
    return "hello "

@app.route('/graphql/<query>/<arg>')
def graphql(query,arg):
    clientquery = ClientQuery('name')
    args={}
    args['name']='me'
    q = '{hello ('+ str(args)+')}'
    
    
    print('{ hello (argument: "graph") }')
    print(clientquery.getQuery())
    result = Query.schema.execute(clientquery.getQuery())
    print(result.data )
    return result.data['hello']

if __name__ == '__main__':
   print("running")
   app.run(debug=True)