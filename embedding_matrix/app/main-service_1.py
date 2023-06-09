import os
import sys
from minio import Minio
import urllib3
import io
import ast
import json

class format:
    def __init__(self, alpha, value,return_input_values):
        self.alpha = alpha
        self.values = value
        self.return_input_values= return_input_values


print("Running service ...")

client = Minio(
    #"localhost:30300",
    #"minio.minio:9000",
    #"minio.nervous-brahmagupta6.im.grycap.net",
    "minio.frosty-grothendieck5.im.grycap.net",
    access_key="minio",
    secret_key="minio123", #"MGE3YWI0",
    secure=True,
    region="us-east-1",
    
)
objCount=3

objects = client.list_objects("drs", recursive=True, prefix="output/",)
objList=0
for obj in objects:
    objList=objList+1
if objList>objCount+1:
    dataFiles = []
    objects = client.list_objects("drs", recursive=True, prefix="output/",)
    z=0
    for i in objects:
            z=z+1
            if z!=1:
                print(i)
                response = client.get_object(
                bucket_name = 'drs',
                object_name= i.object_name
                )
            #print(i.object_name)
            #print(response.read())
                x=str(response.read(),'utf-8')
                x1=x.strip('\n')
                b = ast.literal_eval(x1)
                dataFiles.append(b)
        
        
    #print(dataFiles)    
    values=format(float('0.05'),dataFiles,True)
    data = json.dumps(values.__dict__)
        
    
    #print(str(data))
    out=sys.argv[2]
    f = open(str(out)+".json", "w")
    f.write(str(data))
    f.close()      
        
    objects = client.list_objects("drs", recursive=True, prefix="output/",)
    for ii in objects:
          client.remove_object("drs", ii.object_name)
    
    
    #client.put_object( "dimensionality", "/output/", io.BytesIO(b""), 0, )
    
    print("Process completed ...")
    
    
    
else:
    print("Objects in the input bucket: "+str(objList))
    
