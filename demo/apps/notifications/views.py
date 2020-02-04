from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Notifications
from .serializers import NotificationSerializer
from .renderers import NoticeJSONRenderer

# Create your views here.


class NotificationsAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (NoticeJSONRenderer,)
    serializer_class = NotificationSerializer

    """
    POST action handler
        create new object if success then return 201 status code with serializer.data
    """
    def post(self, request):
        notice = request.data.get("notice", {})
        serializer = self.serializer_class(data=notice)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    """
    PUT action handler
        find object by id
        if object is not found then return not found
        if object existing then update object, if success then return 200 status code with serializer.data
    """
    def put(self, request, id):
        try:
            old_notice = Notifications.objects.get(id=id)
            new_notice = request.data.get("notice", {})
            serializer = self.serializer_class(old_notice, data=new_notice)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Notifications.DoesNotExist:
            raise NotFound("This notice does not exist")

        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    GET action handler
        find object by id or get all objects
        if object is not found then return not found
        if object existing then return 200 status code with serializer.data
    """
    def get(self, request, id=None):
        if id:
            return self.get_by_id(request, id)
        else:
            return self.get_list(request)

    """
    DELETE action handler
        find object by id
        if object is not found then return not found
        if object existing then delete this object and return 204 status code with message = {"detail": "This object has been deleted"}
    """
    def delete(self, request, id):
        try:
            notice = Notifications.objects.get(id=id)
            notice.delete()
            message = {"detail": "This notice has been deleted"}
        except Notifications.DoesNotExist:
            raise NotFound("This notice does not exist")

        return Response(message, status=status.HTTP_204_NO_CONTENT)

    def get_by_id(self, request, id):
        try:
            notice = Notifications.objects.get(id=id)
        except Notifications.DoesNotExist:
            raise NotFound("This notice does not exist")

        serializer = NotificationSerializer(notice)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def get_list(self, request):
        try:
            notices = Notifications.objects.all()
        except Notifications.DoesNotExist:
            raise NotFound("Notices is empty")

        serializer = NotificationSerializer(notices, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
