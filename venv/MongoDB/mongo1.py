import pymongo

client = pymongo.MongoClient("mongodb://root:I8194Z19zVOUCQap@ac-rtnw0gy-shard-00-00.4jf4wg4.mongodb.net:27017,ac-rtnw0gy-shard-00-01.4jf4wg4.mongodb.net:27017,ac-rtnw0gy-shard-00-02.4jf4wg4.mongodb.net:27017/?ssl=true&replicaSet=atlas-l5eicf-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)
d={'name':'Prasanna',
   'email':'hpprasanna07@gmail.com',
   'phone':'343422344'
   }
d2={'name':"Guru",
    'email':'guru@gmail.com',
    'phone':'37782999'
    }
import collections  # From Python standard library.
import bson
from bson.codec_options import CodecOptions
data = bson.BSON.encode(d)
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
