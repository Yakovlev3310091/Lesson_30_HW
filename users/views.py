import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from Lesson_27 import settings
from users.models import User, Location
from users.serializers import LocationSerialiser, UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserDeleteSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerialiser


# class UserListView(ListView):
#     model = User
#     queryset = User.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         super().get(self, *args, **kwargs)
#         self.object_list = self.object_list.order_by('user_name')
#         paginator = Paginator(object_list=self.object_list, per_page=settings.TOTAL_ON_PAGE)
#         page = request.GET.get('page')
#         page_obj = paginator.get_page(page)
#         result = []
#         for user in page_obj:
#             result.append(
#                 {'id': user.id,
#                  'username': user.username,
#                  'first_name': user.first_name,
#                  'last_name': user.last_name,
#                  'role': user.role,
#                  'age': user.age,
#                  'ads_count': user.ads.filter(is_published=True).count(),
#                  })
#         return JsonResponse({'ads': result,
#                              'page': page_obj.number,
#                              'total': page_obj.paginator.count,
#                              }, safe=False, json_dumps_params={'ensure_ascii': False})

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @method_decorator(csrf_exempt, name='dispatch')
# class UserDetailView(DetailView):
#     model = User
#
#     def get(self, request, *args, **kwargs):
#         user = self.get_object()
#         return JsonResponse({
#             'id': user.id,
#             'username': user.username,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'role': user.role,
#             'age': user.age
#         }, safe=False, json_dumps_params={'ensure_ascii': False})

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @method_decorator(csrf_exempt, name='dispatch')
# class UserCreateView(CreateView):
#     model = User
#     fields = ['username', 'password', 'first_name', 'last_name', 'role', 'age', 'locations']
#
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#
#         user = User.objects.create(
#             username=data['username'],
#             first_name=data['first_name'],
#             last_name=data['last_name'],
#             role=data['role'],
#             password=data['password'],
#             age=data['age']
#         )
#         for loc in data['locations']:
#             location, _ = Location.objects.get_or_create(name=loc)
#             user.location.add(location)
#
#         return JsonResponse(
#             {'id': user.id,
#              'username': user.username,
#              'first_name': user.first_name,
#              'last_name': user.last_name,
#              'role': user.role,
#              'age': user.age,
#              'locations': [str(u) for u in user.location.all()]
#              })

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


# @method_decorator(csrf_exempt, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ['username', 'first_name', 'last_name', 'role', 'age']
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         data = json.loads(request.body)
#
#         self.object.username = data['username']
#         self.object.first_name = data['first_name']
#         self.object.last_name = data['last_name']
#         self.object.role = data['role']
#         self.object.age = data['age']
#         self.object.save()
#         return JsonResponse({'id': self.object.id,
#                              'username': self.object.username,
#                              'first_name': self.object.first_name,
#                              'last_name': self.object.last_name,
#                              'role': self.object.role,
#                              'age': self.object.age,
#                              }, safe=False,
#                             json_dumps_params={'ensure_ascii': False})


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


# @method_decorator(csrf_exempt, name='dispatch')
# class UserDeleteView(DeleteView):
#     model = User
#     success_url = '/'
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#
#         return JsonResponse({'status': 'ok'}, status=204)


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer








