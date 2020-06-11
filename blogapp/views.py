from .models import ArticleList
from .serializers import ArticleSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
 
 
 
#ViewSet
# a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create(). the method handlers for a ViewSet are only bound to the corresponding actions at the point of finalizing the view, using the .as_view() method.

class ArticleViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        articles = ArticleList.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
 
 
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
    def retrieve(self, request, pk=None):
        queryset = ArticleList.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

#....................................................................................................
#from django.shortcuts import render
#from django.http import HttpResponse
#from rest_framework.response import Response
# from .models import ArticleList
# from .serializers import ArticleSerializer
#from rest_framework.views import APIView
# from rest_framework import generics, mixins
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# Create your views here.
#Genric View for less code
# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = ArticleList.objects.all()
#     lookup_field = 'id'

#     authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    
    # def get(self, request, id = None):

    #     if id:
    #         return self.retrieve(request)
    #     else:
    #         return self.list(request)
    # def post(self, request, id=None):
    #     return self.create(request)
 
    # def put(self, request, id=None):
    #     return self.update(request, id)
 
    # def delete(self, request, id):
    #     return self.destroy(request, id)

# ClassBased APIView
# class ArticleAPIView(APIView):
 
#     def get(self, request):
#         articles = ArticleList.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
 
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
 
# class ArticleDetails(APIView):
 
#     def get_object(self, id):
#         try:
#             return ArticleList.objects.get(id=id)
#         except ArticleList.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
 
 
#     def get(self, request, id):
#         articles = self.get_object(id)
#         serializer = ArticleSerializer(articles)
#         return Response(serializer.data)
 
 
 
#     def put(self, request,id):
#         articles = self.get_object(id)
#         serializer = ArticleSerializer(articles, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#     def delete(self, request, id):
#         articles = self.get_object(id)
#         articles.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#....................................................................................
#function based
# @csrf_exempt
# def article_list(request):
    
#     if request.method == 'GET':
#         articles = ArticleList.objects.all()
#         serializer = ArticleSerializer(articles, many = True)
#         return JsonResponse(serializer.data, safe = False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, pk):
#     try:
#         articles = ArticleList.objects.get(pk=pk)
#     except ArticleList.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method =='GET':
#         serializer = ArticleSerializer(articles)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(articles, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         articles.delete()
#         return HttpResponse(status=204)
