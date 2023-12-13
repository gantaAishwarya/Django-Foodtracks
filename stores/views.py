from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Store, StoreHours
from .serializers import StoreSerializer, StoreHoursSerializer
from django.http import JsonResponse
from .models import Store
from .filters import StoreHoursFilter
from .serializers import StoreSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class CustomAuthTokenLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            #'user_id': user.pk,
            'email': user.username
        })

# class StoreViewSet(ModelViewSet):
#     model = Store
#     serializer_class = StoreSerializer
#     permission_classes = [AllowAny]
#     queryset = Store.objects.all()
#     filterset_fields = ["name",]

#@authentication_classes(TokenAuthentication)
#@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def store_list(request, format=None):
    if request.method == 'GET':
        queryset = Store.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = StoreSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@authentication_classes(TokenAuthentication)
#@permission_classes([IsAuthenticated])
@api_view(['GET','PUT','DELETE'])
def store_detail(request, id, format=None):

    try:
        store = Store.objects.get(pk=id)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StoreSerializer(store)
        return Response(serializer.data,status=status.HTTP_200_OK)
 
    elif request.method == 'PUT':
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
         

class StoreHoursViewSet(ModelViewSet):
    model = StoreHours
    serializer_class = StoreHoursSerializer
    #permission_classes = [AllowAny]
    queryset = StoreHours.objects.all().order_by('day_of_week')
    filter_backends = [DjangoFilterBackend]
    filterset_class = StoreHoursFilter  