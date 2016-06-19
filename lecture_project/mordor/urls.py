from django.conf.urls import url
# , include
from mordor import views
from mordor.views import UserViewSet, SnippetViewSet, PersonViewSet
from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'snippets', SnippetViewSet)
router.register(r'persons', PersonViewSet)

person_list = PersonViewSet.as_view({
    'get': 'list',
    'delete': 'destroy'
})

person_detail = PersonViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    url(r'^$',
        views.api_root,
        name='home'),

    url(r'^persons/$',
        person_list,
        name='person_list'),

    url(r'^persons/(?P<pk>[0-9]+)$',
        person_detail,
        name='person_detail'),

    url(r'^snippets/$',
        snippet_list,
        name='snippet_list'),

    url(r'^snippets/(?P<pk>[0-9]+)/$',
        snippet_detail,
        name='snippet_detail'),

    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        snippet_highlight,
        name='snippet_highlight'),

    url(r'^users/$',
        user_list,
        name='user_list'),

    url(r'^users/(?P<pk>[0-9]+)/$',
        user_detail,
        name='user_detail'),

    # url(r'^api/hello', views.ApiEndpoint.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
