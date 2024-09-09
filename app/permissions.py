from rest_framework import permissions


class IsStaffPermission(permissions.DjangoModelPermissions):
    #ADDING PERMISSION TO THE REQUEST METHODS 
    perms_map = {

        'GET' : ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS' : [],
        'HEAD' : [],
        'POST' : ['%(app_label)s.add_%(model_name)s'],
        'PUT' : ['%(app_label)s.change_%(model_name)s'],
        'PATCH' : ['%(app_label)s.change_%(model_name)s'],
        'DELETE' : ['%(app_label)s.delete_%(model_name)s'],
    }
     

         



class IsUserPermission(permissions.DjangoModelPermissions):
    #ADDING PERMISSION TO THE REQUEST METHODS 
    perms_map = {
        
        'GET' : ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS' : [],
        'HEAD' : [],
        'POST' : ['%(app_label)s.add_%(model_name)s'],
        'PUT' : ['%(app_label)s.change_%(model_name)s'],
        'PATCH' : ['%(app_label)s.change_%(model_name)s'],
        'DELETE' : ['%(app_label)s.delete_%(model_name)s'],
    }
    
    #checking if user is permitted
    def has_permission (self, request ,views):
        return super().has_permission(request, views)
