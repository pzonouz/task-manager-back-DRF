from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework import status


class JwtObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        response.set_cookie(
            "access",
            response.data["access"],
            httponly=True,
            secure=False,
            samesite="Lax",
            path="/",
            # FIXME: Make Max age parametric
            # max_age=int(os.getenv("SIMPLE_JWT_ACCESS_TOKEN_LIFETIME_HOURS")),
            max_age=3600 * 24 * 365,
        )
        return response
