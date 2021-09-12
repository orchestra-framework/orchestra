import datetime
class Entity():
    pass

class Orchestra(Entity):
    pass
class Project(Entity):
    pass
class Requirement(Entity):
    pass
class Feature(Entity):
    pass
class Release(Entity):
    pass
class EventHandler(Entity):
    pass
class Event(Entity):
    pass
class Test(Entity):
    pass
class Repository(Entity):
    pass
class Member(Entity):
    pass
class Definition(Entity):
    pass
class Issue(Entity):
    pass
class UseCase(Entity):
    pass
class Task(Entity):
    pass
class DataStruct(Entity):
    pass
class Deployment(Entity):
    pass
class Role(Entity):
    pass

v = {
    "orchestra_prop___extends": Orchestra,
    "orchestra_prop___hasOrchestras": [Orchestra],
    "orchestra_prop___hasProjects": [Project],
    "orchestra_prop___hasRoles": [Role],
    "orchestra_prop___hasMembers": [Member],

    "project_prop___extends": Project,
    "project_prop___of": Orchestra,
    "project_prop___hasReleases": [Release],
    "project_prop___hasRoles": [Role],
    "project_prop___hasMembers": [Member],
    "project_prop___hasRepositories": [Repository],

    "requirement_prop___extends": Requirement,
    "requirement_prop___expands": [Requirement],
    "requirement_prop___of": Project,
    "requirement_prop___excludes": [Requirement],
    "requirement_prop___hasRequirements": [Requirement],
    "requirement_prop___hasSources": [Member, str],

    "feature_prop___extends": Feature,
    "feature_prop___expands": Feature,
    "feature_prop___from": [Member, str],
    "feature_prop___hasRequirements": [Requirement],
    "feature_prop___implemented": "bool",
    "feature_prop___hasUrls": [str],

    "release_prop___extends": [Release],
    "release_prop___of": [Orchestra, Project, Release],
    "release_prop___hasRequirements": [Requirement],
    "release_prop___supports": [Requirement, Feature],
    "release_prop___excludes": [Requirement, Feature],
    "release_prop___hasStartDate": datetime.date,
    "release_prop___hasEndDate": datetime.date,
    "release_prop___hasReleaseDate": datetime.date,
    "release_prop___hasVersion": str,
    "release_prop___hasNotes": str,

    "eventHandler_prop___extends": EventHandler,
    "eventHandler_prop___on": Event,
    "eventHandler_prop___triggers": Task,

    "event_prop___extends": Event,
    "event_prop___hasType": {datetime.date, "merge_request", "commit"},
    "event_prop___hasRepositories": [Repository],
    "event_prop___hasSources": [Repository, Role, Member],

    "repository_prop___extends": [Repository],
    "repository_prop___hasUrl": str,
    "repository_prop___hasGuests": [Member],
    "repository_prop___hasDevelopers": [Member],
    "repository_prop___hasMaintainers": [Member],

    "member_prop___extends": [Member],
    "member_prop___hasHandles": str,
    "member_prop___hasRoles": [Role, str],

    "definition_prop___extends": Definition,
    "definition_prop___expands": [Entity],
    "definition_prop___hasSources": [Member, str],
    "definition_prop___from": {Member, str},
    "definition_prop___solves": [Issue],

    "issue_prop___extends": Issue,
    "issue_prop___solvedby": [Entity],
    "issue_prop___relatedto": [Entity],
    "issue_prop___from": {Member, str},

    "usecase_prop___extends": UseCase,
    "usecase_prop___hasPrimaryactor": {Member, str},
    "usecase_prop___hasActors": [Member, str],
    "usecase_prop___triggers": [Feature],

    "task_prop___extends": Task,
    "task_prop___hasCommand": str,
    "task_prop___hasUrls": [str],

    "deployment_prop___extends": Deployment,
    "deployment_prop___hasType": {"Production", "Test"},
    "deployment_prop___of": {Release, Deployment},
    "deployment_prop___hasIp": str,
    "deployment_prop___hasDomain": str,
    "deployment_prop___hasPorts": [str],
    "deployment_prop___islive": bool,

    "role_prop___extends": Role,
    "role_prop___hasStartDate": datetime.date,
    "role_prop___hasEndDate": datetime.date,
    "role_prop___hasReponsabilities": [str],
    "role_prop___of": [Orchestra, Project],
}
