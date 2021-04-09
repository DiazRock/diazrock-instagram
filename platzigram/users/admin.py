from django.contrib import admin


from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile Admin """
    list_display = ('pk', 
                    'user__username', 
                    'phone_number', 
                    'website', 
                    'picture')
    list_display_links = ('pk', 'user__username')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = ('user__email',
                     'user__username', 
                     'user__first_name', 
                     'user__last_name', 
                     'phone_number')
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )
    fieldsets = (
        ('Profile', {
            'fields': ('user', 'profile')
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        })
    )
    
    