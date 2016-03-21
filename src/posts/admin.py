from django.contrib import admin
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","updated","timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated","timestamp"]
	search_fields = ["title","updated","timestamp"]

	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)