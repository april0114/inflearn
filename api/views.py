from typing import Any
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.views import View
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import BaseCreateView
from django.views.generic.list import BaseListView

from api.utils import obj_to_post , prev_next_post, obj_to_comment
from blog.models import Post, Category, Tag, Comment
# Create your views here.

class ApiPostLV(BaseListView):
    paginate_by = 3 

    def get_queryset(self):
        paramCate = self.request.GET.get('category')
        paramTag = self.request.GET.get('tag')
        if paramCate:
            qs = Post.objects.filter(category__name__iexact=paramCate)
        elif paramTag:
            qs = Post.objects.filter(tags__name__iexact = paramTag)
        else :
            qs = Post.objects.all()
        return qs.select_related('category').prefetch_related('tags')
    
    def render_to_response(self, context, **response_kwargs):
        qs =context['object_list']
        postList = [obj_to_post(obj, False) for obj in qs]

        pageCnt = context['paginator'].num_pages
        curPage =context['page_obj'].number

        jsonData ={
            'postList':postList,
            'pageCnt': pageCnt,
            'curPage':curPage,
        }
        return JsonResponse(data = jsonData, safe=True, status =200)
    

class ApiPostDV(BaseDetailView):
    pass

class ApiCateTagView(View):
    def get(self,request, *args, **kwargs):
        qs1 = Category.obejcts.all()
        qs2 = Tag.objects.all()
        cateList = [cate.name for cate in qs1]
        taglist = [tag.name for tag in qs2]

        jsonData ={
            'postList':postList,
            'pageCnt': pageCnt,
            'curPage':curPage,
        }
        return JsonResponse(data = jsonData, safe=True, status =200)

class ApiPostLikeDV(BaseDetailView):
    pass

class CommentCV(BaseCreateView):
    pass