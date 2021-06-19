from django.contrib.auth import user_logged_in
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request

from cfg import settings

from team.models import *


class User(AbstractUser):
    TEAM = '0'
    TEAMMEMBER = '1'
    MENTOR = '2'
    USER_TYPE_CHOICES = (
        (TEAM, "Team"),
        (TEAMMEMBER, "Team Member"),
        (MENTOR, "Mentor"),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)

    class Meta:
        db_table = 'auth_user'


current_user = None


@receiver(user_logged_in, sender=User)
def user_logged_in(sender, request, user, **kwargs):
    print("hello")
    global current_user
    current_user = user




@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    """Automatically Create A User Profile When A New User IS Registered"""
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    if created:
        if instance.user_type == '0':
            team = Team(user=instance)
            team.save()
        elif instance.user_type == '1':
            team_member = TeamMember(user=instance)
            print("njh",request.user.id)
            team = Team.objects.filter(user=request.user.id)[0]
            team_member.team = team
            team_member.save()
        # elif instance.user_type == '2':
        #     mentor = Mentor(user=instance)
        #     researcher.save()


def add_user_to_group(sender, instance: User, created: bool, **kwargs):
    try:
        if created:
            group, _ = Group.objects.get_or_create(name=instance.user_type)
            instance.groups.add(group)
            instance.save()
    except Group.DoesNotExist:
        pass


models.signals.post_save.connect(add_user_to_group, sender=User)
