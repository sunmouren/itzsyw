from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View

from .models import Course, Video
from .forms import SearchForm


class CourseList(ListView):
    """
    课程列表
    """
    model = Course
    template_name = 'course-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'courses'
        return context


class CourseDetail(View):
    """
    课程详情
    """
    def get(self, request, cid):
        course = get_object_or_404(Course, id=int(cid))
        course.view_count += 1
        course.save()
        videos = course.video_set.all()
        return render(request, 'course-detail.html', {
            'course': course,
            'videos': videos
        })


class VideoDetail(View):
    """
    视频详情
    """

    def get(self, request, vid):
        video = get_object_or_404(Video, id=int(vid))
        video.view_count += 1
        video.save()
        return render(request, 'video-detail.html', {'video': video})


def course_search(request):
    """
    搜索课程
    :param request:
    :return:
    """
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Course.objects.annotate(
                search=SearchVector('title', 'overview'),
            ).filter(search=query)
    return render(request, 'search.html', {
        'query': query,
        'results': results,
    })


class UploadCourse(LoginRequiredMixin, View):
    def post(self, request):
        if request.is_ajax():
            title = request.POST.get('title', None)
            overview = request.POST.get('overview', None)
            img_url = request.POST.get('srcUrl', None)
            if title and overview and img_url:
                try:
                    new_service = Course(title=title, overview=overview)
                    new_service.img_url = settings.DOMAIN + img_url
                    new_service.save()
                    return JsonResponse({'msg': 'ok'})
                except BaseException:
                    return JsonResponse({'msg': 'ko'})
        return JsonResponse({'msg': 'ko'})


class UploadVideo(LoginRequiredMixin, View):
    def post(self, request):
        if request.is_ajax():
            title = request.POST.get('title', None)
            overview = request.POST.get('overview', None)
            cid = request.POST.get('cid', None)
            url = request.POST.get('srcUrl', None)
            print(title, cid, overview, url)
            if title and overview and cid and url:
                try:
                    course = Course.objects.get(id=int(cid))
                    new_video = Video(title=title, overview=overview, course=course)
                    new_video.url = settings.DOMAIN + url
                    new_video.save()
                    return JsonResponse({'msg': 'ok'})
                except (Course.DoesNotExist, BaseException) as e:
                    print(e)
                    return JsonResponse({'msg': 'ko'})
        return JsonResponse({'msg': 'ko'})

