from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile, ServiceProfile, Service, ServiceHashtag, SimpleUserProfile


@admin.register(SimpleUserProfile)
class SimpleUserProfileAdmin(admin.ModelAdmin):
    pass


# class UserProfileAdmin(UserAdmin):
#     pass


class ServiceProfileAdmin(admin.ModelAdmin):
    pass


class ServiceHashtagInline(admin.TabularInline):
    model = ServiceHashtag
    extra = 1


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceHashtagInline, ]


# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ServiceProfile, ServiceProfileAdmin)
admin.site.register(Service, ServiceAdmin)
