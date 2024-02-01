from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile,Role
from .serializers import UserSerializer

# @receiver(post_save, sender=User)
# def user_saved(sender, instance, created, **kwargs):
#     if created:

#         if role'
#         role_id = data.pop("role")
        
#         role_inst = Role.objects.get(id=role_id)
#         UserProfile.objects.create(user=instance, role=role_inst)
#         print("A new user has been created:", instance.username)
#     else:
#         print("An existing user has been updated:", instance.username)



# @receiver(post_save, sender=User)
# def user_saved(sender, instance, created, **kwargs):
#     print(kwargs)
#     # import pdb;pdb.set_trace()
#     if created:
#         if hasattr(instance,'role'):
#             role_id = instance['role']
#             role_inst = Role.objects.get(id=role_id)
#             UserProfile.objects.create(user=instance, role=role_inst)
#         else:
#             role_id = 1
#             role_inst = Role.objects.get(id=role_id)
#             UserProfile.objects.create(user=instance, role=role_inst)


@receiver(pre_save, sender=User)
def user_pre_save(sender, instance,**kwargs):
    data = instance
    # print(data,"\n")
    print(kwargs)

    import pdb;pdb.set_trace()
    if hasattr(data,'role'):
        role_id = data['role']
        role_inst = Role.objects.get(id=role_id)
        UserProfile.objects.create(user=data, role=role_inst)
    else:
        role_id = 1
        role_inst = Role.objects.get(id=role_id)
        UserProfile.objects.create(user=data, role=role_inst)
