from orchestra_parser import lang_value_types, lang_keywords_en
import sys
import types


entityTypes = ['orchestra', 'project', 'requirement', 'feature', 'release', 'eventhandler', 'event', 'repository', 'member', 'definition', 'issue', 'usecase', 'task', 'deployment', 'role']
orchestra_properties = ['extends', 'hasOrchestras', 'hasProjects', 'hasRoles', 'hasMembers']
project_properties = ['extends', 'hasReleases', 'hasRoles', 'hasMembers', 'hasRepositories']
requirement_properties = ['extends', 'expands', 'of', 'excludes', 'hasRequirements', 'hasSources']
feature_properties = ['extends', 'expands', 'from', 'hasRequirements', 'implemented', 'hasUrls']

release_properties = ['extends', 'of', 'hasRequirements', 'supports', 'excludes', 'hasStartDate', 'hasEndDate', 'hasReleaseDate', 'hasVersion', 'hasNotes']

values = lang_value_types.v
keywords = lang_keywords_en.kw


moduleObj = {
    'values': values,
    'keywords': keywords,
    'entityTypes': entityTypes,
    'orchestra_properties': orchestra_properties,
    'project_properties': project_properties,    
    'release_properties': release_properties,
}

class Lang(types.ModuleType):
    values = values
    keywords = keywords

    entityTypes = entityTypes
    orchestra_properties = orchestra_properties

    release_properties

    def __getitem__(self, key):
        if key in moduleObj:
            return moduleObj[key]
        return None

sys.modules[__name__] = Lang("orchestra_parser.lang")


