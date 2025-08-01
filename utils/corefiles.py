import json
import os
from typing import Dict, List, Optional
from config import AGREGAR

def readJson()->Dict:
    try:
        with open(AGREGAR, "r", encoding="utf-8") as cf:
            return json.load(cf)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def writeJson(data : Dict)->Dict:
    with open(AGREGAR, "w", encoding="utf-8") as cf:
        json.dump(data, cf, indent=4)

def updateJson(data : Dict, path: Optional[List[str]] = None, name: str = None) -> None:
    currentData = readJson()
    if not path:
        currentData.update(data)
    else:
        current = currentData
        for key in path[:-1]:
            if key not in current:
                return False
            current = current[key]

        if path and path[-1] in current:
            current[path[-1]].update(data)
        else:
            current[path[-1]] = data

    
    writeJson(currentData)

def deleteJson(path: List[str])->bool:
    data = readJson()
    if not data:
        return False
    
    current = data
    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]
    
    if path and path[-1] in current:
        del current[path[-1]]
        writeJson(data)
        return True
    return False

def initializeJson(initialStructure:Dict)->None:
    if not os.path.isfile(AGREGAR):
        writeJson(initialStructure)
    else:
        currentData = readJson()
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        writeJson(currentData)
        return True
    return False