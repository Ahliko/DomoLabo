from Application import Application
from Objects import Object

from uuid import getnode as get_mac
import json

def getIdentity():
    return {
    "name":"Hub",
    "mac": str(get_mac())
}

def getRequest_HubOK():
        return json.dumps({
            "identity":getIdentity(),
            "content":{
                "type":"response",
                "what":"connection",
                "response":"ok",
                "data":json.dumps(Object.OBJECTS)
            }
        })

def getRequest_HubDisponible():
        return json.dumps({
            "identity":getIdentity(),
            "content":{
                "type":"response",
                "what":"connection",
                "response":"disponible",
            }
        })

def processRequest(rqt:str,author:str)->tuple[bool,str,list[str]]:
    try:
        re = json.loads(rqt)
        if re["identity"] != getIdentity():
            match re['content']['type']:
                case "connection":
                    return (True, getRequest_HubDisponible(), [author])
                case "add":
                    return (True, "hola", [re['content']['topic']])
                case "data":
                     return (True, json.dumps({
            "identity":getIdentity(),
            "content":{
                "type":"hola",
                "response":"girl",
            }
        }), [author]) 
                case _:
                    return (False,"", [])
    except Exception as e:
        print(e)
        return (False,"", [])
    return (False,"", [])