from datetime import datetime

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Base
from .serializer import BaseSerializer, JobSerializer, StorySerializer, CommentSerializer, PollSerializer, PollOptionSerializer


class BaseViewSet(viewsets.ModelViewSet):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @api_view(['GET'])
    def latest_news(self):
        try:
            type = self.GET.get('type')
            query = self.GET.get('search')

            page_query_param = 'page'
            paginator = PageNumberPagination()
            paginator.page_size = 15
            paginator.page_query_param = page_query_param
            if type and query:
                filtered_news = Base.objects.filter(
                    deleted=False, dead=False, type=type, text__icontains=query, is_latest=True)
            elif type:
                filtered_news = Base.objects.filter(
                    deleted=False, dead=False, type=type, is_latest=True)
            elif query:
                filtered_news = Base.objects.filter(
                    deleted=False, dead=False, text__icontains=query, is_latest=True)
                print(filtered_news)
            else:
                filtered_news = Base.objects.filter(
                    deleted=False, dead=False, is_latest=True)
            context = paginator.paginate_queryset(filtered_news, self)
            job_data = []
            story_data = []
            comment_data = []
            poll_data = []
            pollopt_data = []
            for i in range(len(context)):
                if context[i].type == 'job':
                    job_data.append(context[i])
                elif context[i].type == 'story':
                    story_data.append(context[i])
                elif context[i].type == 'comment':
                    comment_data.append(context[i])
                elif context[i].type == 'poll':
                    poll_data.append(context[i])
                elif context[i].type == 'pollopt':
                    pollopt_data.append(context[i])
            serialized_data = []
            if len(job_data) > 0:
                job_serialized_data = JobSerializer(job_data, many=True).data
                serialized_data.extend(job_serialized_data)
            if len(story_data) > 0:
                story_serialized_data = StorySerializer(
                    story_data, many=True).data
                serialized_data.extend(story_serialized_data)
            if len(comment_data) > 0:
                comment_serialized_data = CommentSerializer(
                    comment_data, many=True).data
                serialized_data.extend(comment_serialized_data)
            if len(poll_data) > 0:
                poll_serialized_data = PollSerializer(
                    poll_data, many=True).data
                serialized_data.extend(poll_serialized_data)
            if len(pollopt_data) > 0:
                pollopt_serialized_data = PollOptionSerializer(
                    pollopt_data, many=True).data
                serialized_data.extend(pollopt_serialized_data)
            return paginator.get_paginated_response(serialized_data)
        except:
            response = {
                "status": "error",
                "message": "No News Found!"
            }
            return Response(data=response, status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create_news(self):
        if 'type' in self.data:
            type = self.data['type']
        else:
            response = {
                "status": "error",
                "message": "Type is required!"
            }
            return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)
        if 'by' in self.data:
            by = self.data['by']
        else:
            response = {
                "status": "error",
                "message": "By is required!"
            }
            return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)
        time = datetime.now()
        if 'kids' in self.data:
            kids = self.data['kids']
        else:
            kids = None
        if 'parts' in self.data:
            parts = self.data['parts']
        else:
            parts = None
        if 'parent' in self.data:
            parent = self.data['parent']
        else:
            parent = None
        if 'text' in self.data:
            text = self.data['text']
        else:
            text = None
        if 'descendants' in self.data:
            descendants = self.data['descendants']
        else:
            descendants = None
        if 'score' in self.data:
            score = self.data['score']
        else:
            score = None
        if 'url' in self.data:
            url = self.data['url']
        else:
            url = None
        if 'title' in self.data:
            title = self.data['title']
        else:
            title = None
        if type == 'job':
            Base.objects.create(type=type, by=by, time=time,
                                kids=kids, text=text, url=url, title=title, is_from_hacker_news=False)
        elif type == 'story':
            Base.objects.create(type=type, by=by, time=time,
                                descendants=descendants, score=score, title=title, url=url, is_from_hacker_news=False)
        elif type == 'comment':
            Base.objects.create(type=type, by=by, time=time,
                                kids=kids, parent=parent, text=text, is_from_hacker_news=False)
        elif type == 'poll':
            Base.objects.create(type=type, by=by, time=time, kids=kids, parts=parts,
                                descendants=descendants, score=score, title=title, text=text, is_from_hacker_news=False)
        elif type == 'pollopt':
            Base.objects.create(type=type, by=by, time=time,
                                kids=kids, parent=parent, score=score, is_from_hacker_news=False)
        else:
            response = {
                "status": "error",
                "message": "Type is incorrect! (use either job, story, comment, poll or pollopt)!"
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        response = {
            "status": "success",
            "message": f"{type.capitalize()} by {by} created successfully!"
        }
        return Response(data=response, status=status.HTTP_200_OK)

    @api_view(['PATCH'])
    def update_news_by_id(self, id):
        try:
            news = Base.objects.get(pk=id)
            if news.is_from_hacker_news:
                response = {
                    "status": "error",
                    "message": "You cannot update a news from Hacker News!"
                }
                return Response(data=response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            if 'type' in self.data:
                type = self.data['type']
            else:
                type = news.type
            if 'by' in self.data:
                by = self.data['by']
            else:
                by = news.by
            time = datetime.now()
            if 'kids' in self.data:
                kids = self.data['kids']
            elif news.kids is not None:
                kids = news.kids
            else:
                kids = None
            if 'parts' in self.data:
                parts = self.data['parts']
            elif news.parts is not None:
                parts = news.parts
            else:
                parts = None
            if 'parent' in self.data:
                parent = self.data['parent']
            elif news.parent is not None:
                parent = news.parent
            else:
                parent = None
            if 'text' in self.data:
                text = self.data['text']
            elif news.text is not None:
                text = news.text
            else:
                text = None
            if 'descendants' in self.data:
                descendants = self.data['descendants']
            elif news.descendants is not None:
                descendants = news.descendant
            else:
                descendants = None
            if 'score' in self.data:
                score = self.data['score']
            elif news.score is not None:
                score = news.score
            else:
                score = None
            if 'url' in self.data:
                url = self.data['url']
            elif news.url is not None:
                url = news.url
            else:
                url = None
            if 'title' in self.data:
                title = self.data['title']
            elif news.title is not None:
                title = news.title
            else:
                title = None
            news.type = type
            news.by = by
            news.time = time
            news.kids = kids
            news.parts = parts
            news.parent = parent
            news.text = text
            news.descendants = descendants
            news.score = score
            news.url = url
            news.title = title
            news.save()
            response = {
                "status": "success",
                "message": f"{(news.type).capitalize()} by {news.by} updated successfully!"
            }
            return Response(data=response, status=status.HTTP_200_OK)
        except:
            response = {
                "status": "error",
                "message": "No News Found!"
            }
            return Response(data=response, status=status.HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    def delete_news_by_id(self, id):
        try:
            news = Base.objects.get(pk=id)
            if news.is_from_hacker_news:
                response = {
                    "status": "error",
                    "message": "You cannot update a news from Hacker News!"
                }
                return Response(data=response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            news.delete()
            response = {
                "status": "success",
                "message": f"{news.type.capitalize()} by {news.by} deleted successfully!"
            }
            return Response(data=response, status=status.HTTP_200_OK)
        except:
            response = {
                "status": "error",
                "message": "No News Found!"
            }
            return Response(data=response, status=status.HTTP_404_NOT_FOUND)
