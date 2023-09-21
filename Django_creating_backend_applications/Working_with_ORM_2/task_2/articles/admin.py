from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            cleaned_data = form.cleaned_data
            if cleaned_data.get('is_main') == True:
                count += 1
                if count > 1:
                    raise ValidationError('Нужно указать только один основной раздел')
        if count == 0:
            raise ValidationError('Требуется указать основной раздел')
        return super().clean()

class TagsInLine(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsInLine,]