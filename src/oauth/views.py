from django.contrib.auth import get_user_model
from rest_framework import status, views
from rest_framework.response import Response
from .services.base_auth import create_token
from drf_yasg.utils import swagger_auto_schema
from .serializers import TokenObtainSerializer


User = get_user_model()


class TokenObtainView(views.APIView):
    @swagger_auto_schema(request_body=TokenObtainSerializer, responses={200: 'Token'})
    def post(self, request):
        try:
            user = User.objects.get(username=request.data.get('username'))
        except User.DoesNotExist:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

        token = create_token(user_id=user.id)
        return Response(token, status=status.HTTP_200_OK)