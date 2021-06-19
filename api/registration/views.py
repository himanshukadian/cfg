from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_auth.registration.views import RegisterView

from cfg.permissions import IsTeam, IsTeamMember, Ismentor



class TeamMemberRegisterView(RegisterView):
    permission_classes = (IsAuthenticated, IsTeam)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        print(self.request.user)
        print(request.data)
        # mutable = request.data._mutable
        # request.data._mutable = True
        d = {'userType': '1'}
        request.data.update(d)
        # request.data._mutable = mutable
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "some message", "status": "ok"}
        response.data.update(custom_data)
        return response

class TeamRegisterView(RegisterView):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        print(self.request.user)
        mutable = request.data._mutable
        request.data._mutable = True
        d = {'userType': '0'}
        request.data.update(d)
        request.data._mutable = mutable
        response = super().create(request, *args, **kwargs)
        custom_data = {"message": "some message", "status": "ok"}
        response.data.update(custom_data)
        return response

#
#
# class MentorRegisterView(RegisterView):
#
#     def create(self, request, *args, **kwargs):
#         print(self.request.user)
#         mutable = request.data._mutable
#         request.data._mutable = True
#         d = {'userType': '2'}
#         request.data.update(d)
#         request.data._mutable = mutable
#         response = super().create(request, *args, **kwargs)
#         custom_data = {"message": "some message", "status": "ok"}
#         response.data.update(custom_data)
#         return response
