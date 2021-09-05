import lorem, random, json, datetime, time
from datetime import date

from string import Template
from lorem.text import TextLorem
from typing import List, Type

from orchestra_parser import lang
idLorem = TextLorem(wsep='_', srange=(6,6), words="ab cd ef gh il mn op".split())


def gen___v_id():
    id = idLorem.sentence().rstrip(".").lower()
    return id

def gen___v_string():
    return random.choice(lorem.sentence().split(' ')).rstrip(".")

def gen___v_list(valueTypes, length):
    print("valueTypes: " )
    print(valueTypes)
    values = []
    for _ in range (0, length):
        valueType = random.choice(valueTypes)
        values.append(getValue(valueType))
    return values

def gen___v_bool():
    return random.choice((True, False))

idStore = {}
for entityType in lang['entityTypes']:
    idStore[entityType] = []
    for _ in range(1, 5):
        idStore[entityType].append(gen___v_id())

def random_date():
    return "1/1/2021"

def isAnId(typeName):
    return hasattr(typeName, '__name__') and typeName.__name__.lower() in lang['entityTypes']

def getValue(valueType, length = 1):
    #print(type(valueType))
    # print("valueType: " + str(valueType))
    # if type(entityTypes) != List:        
    #     print("if 1")
    #     entityTypes = (entityTypes)

        
            
    if hasattr(valueType, '__name__'):
        if valueType.__name__ == 'date':
            return random_date()

        if valueType.__name__ == 'str':
            return "AAAAAA"
    
    if isAnId(valueType):
        return random.choice(idStore[valueType.__name__.lower()])
        
    if type(valueType) == list:
        value = ''        
        for subValueType in valueType:
            value = value + ' ' + getValue(subValueType)
        
        value = value.strip()
        return value

    raise Exception('type ' + str(valueType) +' not implemented')

    
def gen___properties(entityType):
    properties = ''
    if lang[entityType + '_properties']:
        for propertyKey in lang[entityType + '_properties']:
            propKwVarName = entityType + '_prop___' + propertyKey
            propKw = lang.keywords[propKwVarName]
            if type(propKw) == list:
                propKw = random.choice(propKw)
            
            propValueVarName = entityType + '_prop___' + propertyKey
            properties = properties + '\n\t' + propKw + ' ' + getValue(lang.values[propValueVarName])
    return properties
    
    

def gen___entity(entityType):    
    return (Template("""$prefix $name $properties_prefix
\t$description
\t$tags $properties""").substitute({
        'prefix': random.choice(lang.keywords['entity__declaration_prefix']) + ' ' + lang.keywords[entityType],        
        'name': gen___v_string(),
        'properties_prefix': lang.keywords['entity__properties_prefix'],        
        'description': lang.keywords['entity__prop__hasDescription'] + ' ' + idLorem.sentence(),        
        'tags': lang.keywords['entity__prop__hasTags'] + ' ' + gen___v_string().lower(),
        'properties': gen___properties(entityType)
    }))


def start():
    WRITE_TO_FILE = True
    sample = []
    for entityType in lang['entityTypes']:
        for _ in range(0, random.randint(2, 10)):
            sample.append(gen___entity(entityType))        
    
    random.shuffle(sample)
    sample = '\n\n'.join(sample)

    if WRITE_TO_FILE:
        f = open("orchestra_parser/tests/samples/sample.orchx", "w")
        f.write(sample)
        f.close()
    else:
        print(sample)        