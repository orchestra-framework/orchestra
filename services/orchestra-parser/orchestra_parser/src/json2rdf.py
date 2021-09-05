import sys
from rdflib import Graph, Literal, URIRef, Namespace
from rdflib.namespace import RDFS, RDF, FOAF, OWL, XSD, DC, DCTERMS

import urllib.parse

def urify(ns, txt):
    txt=txt.replace(" ","_").replace(".","")
    return ns+urllib.parse.quote(txt)

ORCHESTRA_DOMAIN = "http://orchestra.software"
ORCHESTRA_URI = ORCHESTRA_DOMAIN + "/linked-data/"

## Defining needed namespaces 
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
schema = Namespace("http://schema.org/")

## Defining Orchestra Ontology
orc_ontology = Namespace(ORCHESTRA_URI + "ontology/")
orc_ontology_class_orchestra = Namespace(ORCHESTRA_URI + "ontology/classes/orchestra/")
orc_ontology_class_requirement = Namespace(ORCHESTRA_URI + "ontology/classes/requirement/")
orc_ontology_class_release = Namespace(ORCHESTRA_URI + "ontology/classes/release/")
#### --->
#### --->
#### --->
g = Graph ()

### # Class Entity 
gs = g.resource(oo.Entity)
gs.set(RDF.type, RDFS.Class) 

### # # Property: name
gs = g.resource(oo.name)
gs.set(RDF.type, RDF.Property)
gs.set(RDFS.domain, oo.Entity)
gs.set(RDFS.range, RDFS.Literal)

### # # Property: hasDescription
gs = g.resource(oo.has_description)
gs.set(RDF.type, RDF.Property)
gs.set(RDFS.domain, oo.Entity)
gs.set(RDFS.range, RDFS.Literal)

### # # Property: has_tags
gs = g.resource(oo.has_tags)

### # # Property: as
gs = g.resource(oo.as)
#### --->
#### --->
#### --->
### # Class Orchestra
gs = g.resource(oo.Orchestra)
gs.set(RDF.type, RDFS.Class)
gs.set(RDFS.subClassOf, oo.Entity)
### # # Property: extends
gs = g.resource(oreq.extends)
gs.set(RDF.type, RDF.Property)
gs.set(RDFS.domain, oreq.Requirement)
gs.set(RDFS.range, RDFS.Literal)

### # # Property: has_orchestras
gs = g.resource(oo.has_orchestras)

### # # Property: has_projects
gs = g.resource(oo.has_projects)

### # # Property: has_roles
gs = g.resource(oo.has_roles)

### # # Property: has_roles
gs = g.resource(oo.has_roles)
#### ---> 
#### ---> 
#### ---> 
### # Class Project
gs = g.resource(oo.Project)
gs.set(RDF.type, RDFS.Class) 
gs.set(RDFS.subClassOf, oo.Entity)
#### ---> 
#### ---> 
#### ---> 
### # Class Requirement
gs = g.resource(oreq.Requirement)
gs.set(RDF.type, RDFS.Class)
gs.set(RDFS.subClassOf, oo.Entity)

### # # Property: extends
gs = g.resource(oreq.extends)
gs.set(RDF.type, RDF.Property)
gs.set(RDFS.domain, oreq.Requirement)
gs.set(RDFS.range, RDFS.Literal)





### # Class Feature
gs = g.resource(oo.Feature)
gs.set(RDF.type, RDFS.Class) 
gs.set(RDFS.subClassOf, oo.Entity)

### # # Property: satisfies
gs = g.resource(oo.satisfies)
gs.set(RDF.type, RDF.Property)
gs.set(RDFS.domain, oo.Requirement)
gs.set(RDFS.range, RDFS.Literal)




### # Class Release
gs = g.resource(orel.Release)
gs.set(RDF.type, RDFS.Class) 
gs.set(RDFS.subClassOf, oo.Entity)

### # # Property: of
gs = g.resource(orel.of)
gs.set(RDF.type, RDF.Property)
gs.add(schema.domainIncludes, oo.Project)
gs.add(schema.domainIncludes, oo.Release)
gs.set(RDFS.range, RDFS.Literal)

### # # Property: requires
gs = g.resource(orel.requires)
gs.set(RDF.type, RDF.Property)
gs.set(schema.domainIncludes, oo.Requirement)
gs.set(schema.domainIncludes, oo.Feature)
gs.set(schema.domainIncludes, oo.Release)
gs.set(RDFS.range, RDFS.Literal)



# namespace bindings
g.bind("oo", oo)
g.bind("rdfs", rdfs)


import json


def start(): 
    with open(sys.argv[1]) as f:
        entities = json.load(f)
        for entity in entities:
            print(entity)
            if entity['entity_class_name'] == "project":
                projectURI = urify(ORCHESTRA_URI + "workspace_hash_prefix" + "/project/", entity['entity_prop_name'])
                print(projectURI)
                gs = g.resource(projectURI)
                gs.set(RDF.type, oo.Project)
                gs.set(oo.name, Literal(entity['entity_prop_name'], lang='it'))

        OUTPUT_PATH = 'out_graph.ttl'
        g.serialize(destination=OUTPUT_PATH, format='turtle')
    

