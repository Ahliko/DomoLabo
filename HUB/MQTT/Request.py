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

def getRequest_ObjData():
    return json.dumps({
        "identity":getIdentity(),
            "content":{
                "type":"add",
            }
    })

def processRequest(rqt:str,author:str, crud)->tuple[bool,str,list[str]]:
    try:
        re = json.loads(rqt)
        if re["identity"] != getIdentity():
            match re['content']['type']:
                case "connection":
                    app = Application(identity=re['identity'], topic=author)
                    Application.APPLICATIONS.append(app)
                    crud.insert_db("app", "topic", author)
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
                case "response":
                    match re['content']['what']:
                        case "add":
                            Object.OBJECTS[re['content']['topic']]= json.dump(re['content']['data'])
                            crud.insert_db("object", "topic", re['content']['topic'])
                case _:
                    return (False,"", [])
    except Exception as e:
        print(e)
        return (False,"", [])
    return (False,"", [])