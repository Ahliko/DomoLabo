from Application import Application
from Objects import Object

from uuid import getnode as get_mac
import json

haveResponse = False


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
    global haveResponse
    try:
        re = json.loads(rqt)
        if re["identity"] != getIdentity():
            match re['content']['type']:
                case "connection":
                    app = Application(identity=re['identity'], topic=author)
                    Application.APPLICATIONS.append(app)
                    crud.insert_db("app", "topic", author)
                    return (True, getRequest_HubDisponible(), [author], False)
                case "add":
                    return (True, getRequest_ObjData(), [re['content']['topic']], True)  # Dire que l'on veut attendre une reponse
                case "data":
                     return (True, json.dumps({
                        "identity":getIdentity(),
                        "content":{
                            "type":"data",
                            "data":re['content']['data'],
                        }
                    }), [re['content']['topic']], False) 
                case "response":
                    haveResponse = True
                    match re['content']['what']:
                        case "add":
                            Object.OBJECTS[author]= json.dumps(re['content']['data'])
                            crud.insert_db("object", "topic", author)
                            re["content"]["data"]["topic"] = author
                            return (True, json.dumps({
                                 "identity":getIdentity(),
                                 "content":{
                                    "type":"response",
                                    "what":"add",
                                    "response":"ok",
                                    "identity":json.dumps(re['identity']),
                                    "data": json.dumps(re["content"]["data"]),
                                 }
                            }), [x.topic if type(x) == Application else str(x[0]) for x in Application.APPLICATIONS], False)
                        case "data":
                            return (True, json.dumps({
                                "identity":getIdentity(),
                                "content":{
                                    "type":"data",
                                    "data":json.dumps(re['content']['data']),
                                }
                            }), [x.topic if type(x) == Application else str(x[0]) for x in Application.APPLICATIONS], False)
                case _:
                    return (False,"", [], False)
    except Exception as e:
        print(e)
        return (False,"", [],False)
    return (False,"", [],False)