import json
import xml.etree.ElementTree as ET
import time
import sys
#import stomp
import boto3
import ssl
from stomp import *

def lambda_handler(event, context):
    # TODO implement
    tree=ET.parse("samplexml.xml")
    root=tree.getroot()
    tag=root.tag
    #print(tag)

    attr=root.attrib
    #print(attr)

    for c in root.findall('services'):
        #print(c)
        srv=c.find('serviceversion').text
        #print(srv)
        rank=c.find('servicename').text
        #clprint(rank)
        if rank == "app02" and srv == "v4":
            print("available")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
