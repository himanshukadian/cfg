from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Team(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='rootadmin')
    contact_no = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return f'{self.user.username}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'team'


class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team_member')
    team = models.ForeignKey(Team, related_name="team", on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20, blank=True, default="")
    school = models.CharField(max_length=20, blank=True, default="")
    city = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return f'{self.user.username}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'teammember'


