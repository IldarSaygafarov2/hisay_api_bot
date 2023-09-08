from django.contrib import admin

from .models import ServiceProfile, Service, ServiceHashtag, SimpleUserProfile, UserRequest


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(SimpleUserProfile)
class SimpleUserProfileAdmin(admin.ModelAdmin):
    pass


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
