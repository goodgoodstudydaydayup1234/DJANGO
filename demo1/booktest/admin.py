from django.contrib import admin
from .models import BookInfo,HeroInfo

# Register your models here.


class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    # 关联个数
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline]


admin.site.register(BookInfo, BookInfoAdmin)


class HeroInfoAdmin(admin.ModelAdmin):
    # 显示字段，点击列头可以排序
    list_display = ['name', 'sex', 'skill']
    # 过滤字段，过滤框出现在右侧
    list_filter = ['hgender']
    # 分页，分页框出现在下侧
    list_per_page = 2
    # 搜索字段，搜索框出现在上侧
    search_fields = ['hname']


admin.site.register(HeroInfo, HeroInfoAdmin)

