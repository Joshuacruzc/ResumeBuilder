from django.contrib import admin

from experience.models import Experience, ExperienceStatement, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ExperienceStatementsInline(admin.TabularInline):
    model = ExperienceStatement


class TagInline(admin.TabularInline):
    model = Tag.experiences.through


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'host']
    inlines = [ExperienceStatementsInline, TagInline]

