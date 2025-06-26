from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
from rest_framework.exceptions import NotFound
from .serializers import FeedSerializer
# Create your views here.

class Feeds(APIView):
    #전체 게시글 데이터 조회
    def get(self, request):
        feeds = Feed.objects.all()

        # 객체 -> JSON(시리얼 라이즈)
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # 역직렬화 (클라이언트가 보내온 Json -> object)
        serializer = FeedSerializer(data=request.data)

        if serializer.is_valid():
            feed = serializer.save(user=request.user)

            serializer = FeedSerializer(feed)
            # print("post serializer", serializer)

            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound

    def get(self, request, feed_id):
        feed = self.get_object(feed_id)

        serializer = FeedSerializer(feed)

        return Response(serializer.data)