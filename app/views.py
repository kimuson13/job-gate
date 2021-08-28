from django.shortcuts import render, redirect
from django.views.generic import View
from .models import User
from .forms import PostUserInfoForm, PostElementary
from django.contrib.auth.mixins import LoginRequiredMixin


class homeView(View):
    def get(self, request, *args, **kwargs):
        # post_data = Post.objects.order_by('-id')
        # return render(request, 'app/home.html', {
        #     # 'post_data': post_data
        # })
        return render(request, 'app/home.html')

    def post(self, request, *args, **kwargs):
        form = PostUserInfoForm(request.POST or None)
        if form.is_valid():
            post_user_data = User()
            post_user_data.name = request.POST['name']
            post_user_data.email = request.POST['email']
            post_user_data.save()
            return redirect('question_description')

        return render(request, 'app/home.html')


class QuestionDescriptionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/questionDescription.html')

class ElementarySchoolView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/elementarySchool.html')

    def post(self, request, *args, **kwargs):
        form = PostElementary(request.POST or None)
        if form.is_valid():
            return redirect('junior-high-school')

        return render(request, 'app/elementarySchool')

class JuniorHighSchoolView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/juniorHighSchool.html')

class HighSchoolView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/highSchool.html')

class UniversityView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/university.html')

# class PostDetailView(View):
#     def get(self, request, *args, **kwargs):
#         post_data = Post.objects.get(id=self.kwargs['pk'])
#         return render(request, 'app/post_detail.html', {
#             'post_data': post_data
#         })


# class CreatePostView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         form = PostForm(request.POST or None)
#         return render(request, 'app/post_form.html', {
#             'form': form
#         })

#     def post(self, request, *args, **kwargs):
#         form = PostForm(request.POST or None)

#         if form.is_valid():
#             post_data = Post()
#             post_data.author = request.user
#             post_data.title = form.cleaned_data['title']
#             post_data.content = form.cleaned_data['content']
#             post_data.save()
#             return redirect('post_detail', post_data.id)

#         return render(request, 'app/post_form.html', {
#             'form': form
#         })


# class PostEditView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         post_data = Post.objects.get(id=self.kwargs['pk'])
#         form = PostForm(
#             request.POST or None,
#             initial={
#                 'title': post_data.title,
#                 'content': post_data.content
#             }
#         )
#         return render(request, 'app/post_form.html', {
#             'form': form
#         })

#     def post(self, request, *args, **kwargs):
#         form = PostForm(request.POST or None)

#         if form.is_valid():
#             post_data = Post.objects.get(id=self.kwargs['pk'])
#             post_data.title = form.cleaned_data['title']
#             post_data.content = form.cleaned_data['content']
#             post_data.save()
#             return redirect('post_detail', self.kwargs['pk'])

#         return render(request, 'app/post_form.html', {
#             'form': form
#         })


# class PostDeleteView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         post_data = Post.objects.get(id=self.kwargs['pk'])
#         return render(request, 'app/post_delete.html', {
#             'post_data': post_data
#         })

#     def post(self, request, *args, **kwargs):
#         post_data = Post.objects.get(id=self.kwargs['pk'])
#         post_data.delete()
#         return redirect('index')
