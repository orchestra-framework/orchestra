import sys
from lark import Lark, Transformer, v_args
from lark.indenter import Indenter
import json
from string import Template

from orchestra_parser import  lang

        
class TreeToList(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\\"', '"')
    def string_ml(self, s):
        return (
            s[0][1:-1]
            .replace('""', '')
        )
        
    def entity_name(self, s):
        self.prop_name = s[0]
        return s[0]

    def keyword_class_entity_has_description(self, s):
        return s

    def entity_has_description(self, s):
        self.prop_has_description = s[1].strip()
        return self.prop_has_description


    def keyword_class_entity_has_alias(self, s):
        return s

    def entity_has_alias(self, s):
        self.prop_has_alias = s[1].strip()
        return self.prop_has_alias


    def keyword_class_project(self, subtree):
        return subtree    

    def entity_class_project(self, subtree):
        self.entity_type = "project"
        return subtree
    
        

    def keyword_class_requirement(self, subtree):
        return subtree

    def entity_class_requirement(self, subtree):
        self.entity_type = "requirement"
        return subtree    
    


    def keyword_class_release(self, subtree):
        return subtree

    def entity_class_release_property_of(self, subtree):
        return subtree

    def entity_class_release_property_of(self, subtree):
        return subtree

    

    start = list
    entity = lambda self, _: dict({    
        'entity_prop_has_description': getattr(self, 'prop_has_description', ""),
        'entity_prop_name': getattr(self, 'prop_name', ""),
        'entity_class_name': getattr(self, 'entity_type', ""),
    })

    




def start():
    grammar_template_file_path = "orchestra-lang-grammar.v1.5.lark.template"
    with open(grammar_template_file_path) as grammar_template_file:
        orchestra_parser = Lark(Template(grammar_template_file.read()).substitute(lang.keywords))

        Lark.open(, parser='lalr', lexer='standard', transformer=TreeToList())
        #print(orchestra_parser.parse(orchestra_test_string1).pretty())
        with open(sys.argv[1]) as f:
            #tree = json_parser.parse(f.read())
            #tree = TreeToJson().transform(tree)        
            #print(tree['a'])
            entities = orchestra_parser.parse(f.read())
            print(json.dumps(entities))
