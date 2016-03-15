from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Post
from .forms import PostForm



# <createpage>
def posts_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Successfully Created!")
		return HttpResponseRedirect(instance.get_absolute_url())

	else:
		messages.error(request, "Failed to create!")

	context_data = {
		"form":form,
	}
	return render(request, "post_form.html", context_data)

# </createpage>


# <detailpage>
def posts_detail(request, id=None): # Retrieve
	#instance = Post.objects.get(id=100)

	instance = get_object_or_404(Post,id=id)

	context_data = {
		"title":instance.title,
		"instance":instance,
	}
	return render(request, "post_detail.html", context_data)

# </detailpage>


# <listpage>
def posts_list(request): # List items
	queryset = Post.objects.all()

	context_data = {
		"object_list" : queryset,
		"title" : "List",
	}
		
	return render(request, "base.html", context_data)

# </listpage>



# <updatepage>
def posts_update(request, id=None):
	instance = get_object_or_404(Post,id=id)

	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Item saved!", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context_data = {
		"title":instance.title,
		"instance":instance,
		"form":form,
	}

	return render(request, "post_form.html", context_data)
# </updatepage>
 


# <deletepage>
def posts_delete(request, id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request, "Successfully deleted!")
	return redirect("posts_lists.html")

# </deletepage>	
