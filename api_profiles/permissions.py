from rest_framework import permissions


class UpdateOnlyOwnProfile(permissions.BasePermission):
	#Allow the user to edint only their onw profile

	def has_object_permission(self,request,view,obj):
		#Check user is trying to edit their own profile
		if request.method in permissions.SAFE_METHODS: #Safe methods are HTTP methods that dont change the object as GET request
			return True

		return obj.id == request.user.id #This will return a boolean TRUE|FALSE