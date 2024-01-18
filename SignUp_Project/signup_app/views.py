from signup_app.models import User
from signup_app.serialization import UserSerializer
from django.http import Http404
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.
class UserViews(generics.CreateAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    def get(self, request, format=None):
        Users = User.objects.all()
        serializer = UserSerializer(Users, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        # breakpoint()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class UsergetUpdateDelete(generics.RetrieveUpdateDestroyAPIView,generics.GenericAPIView):
    # breakpoint()
    serializer_class=UserSerializer
    queryset=User.objects.all()
    def get_object(self):
        
        try:
            lookup_url_kwarg =self.lookup_field
            # breakpoint()
            assert lookup_url_kwarg in self.kwargs, ((self.__class__.__name__, lookup_url_kwarg))
            filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
            obj = User.objects.get(**filter_kwargs)
            return obj
        except User.DoesNotExist:
            raise Http404
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK,data={'data':'deleted successfully'})