from django.contrib import admin

from models import *

from django.forms import ModelForm
from suit.widgets import AutosizedTextarea

class IdeaForm(ModelForm):
    class Meta:
        widgets = {
            'content': AutosizedTextarea(attrs={'rows': 4, 'class': 'input-xlarge'}),

            # You can also specify html attributes
            #'': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
        }

class IdeaAdmin(admin.ModelAdmin):
	form = IdeaForm
	search_fields = ['title', 'content']
	list_display = ['title', 'content', 'source', 'datetime', 'archived']
	list_filter = ['archived']
	date_hierarchy = "datetime"
	exclude=("datetime",)
	readonly_fields=('datetime', )


admin.site.register(Idea, IdeaAdmin)