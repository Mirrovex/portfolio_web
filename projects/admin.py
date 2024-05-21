from django.contrib import admin

from .models import Tag, Project, ProjectImage


class ProjectImageInline(admin.TabularInline):

    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):

    list_display = ("title", "order", "show", "github", "website")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags", )
    list_editable = ('order',)


class TagAdmin(admin.ModelAdmin):

    list_display = ("name", "order", "show")
    search_fields = ("name", )
    list_editable = ('order',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
