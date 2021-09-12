import sys
import json, os
from string import Template
import sys
from lark import Lark, Transformer, v_args
from lark.indenter import Indenter
import json
from string import Template

from orchestra_parser import  lang

from orchestra_parser import lang


orchestra_lark = None

def define_transformer_class(): 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("dir_path:" + dir_path)
    grammar_template_file_path = os.path.join(dir_path, "grammar.v1.5.lark.template")
    with open(grammar_template_file_path) as grammar_template_file:
        #print(lang.keywords['orchestra_prop___extends'])
        grammar = Template(grammar_template_file.read()).substitute(lang.keywords)
        #print(grammar)
        
        class_declarations = ''
        for entityType in lang.entityTypes:
            class_declarations = class_declarations + Template("""
    def declaration_class_$entityType(self, subtree):
        self.entity_type = "$entityType"            
        return subtree
            """).substitute({
                'entityType': entityType
            })

        
        parser_script = """
class OrchestraTransformer(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\\"', '"')
    def string_ml(self, s):
        return (
            s[0][1:-1]
            .replace('""', '')
        )
    
    def Entity_prop___name(self, s):
        print(s)
        self.prop_name = s[0]
        return s[0]

        """ + class_declarations + """
orchestra_lark = Lark(grammar, parser='lalr', lexer='standard', transformer=OrchestraTransformer())
        """
    exec(parser_script)


def main():     
    define_transformer_class()
    with open(sys.argv[1]) as f:
        pass
            #tree = json_parser.parse(f.read())
            #tree = TreeToJson().transform(tree)        
            #print(tree['a'])
            #print(f.read())
            
            #entities = orchestra_lark.parse(f.read())
            #print(json.dumps(entities))
    



        #print(file_body)
        # orchestra_parser = Template(parser_template_file.read()).substitute({
        #     class_declarations: 
        # })

if __name__ == "__main__":    
    main()
    