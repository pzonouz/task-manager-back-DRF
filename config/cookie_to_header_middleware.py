from rest_framework.request import Request
from rest_framework.response import Response


def cookie_to_header_middleware(get_response):
    def middleware(request: Request):
        access = request.COOKIES.get("access")
        if access is not None:
            request.META["HTTP_AUTHORIZATION"] = f"JWT {access}"
        response: Response = get_response(request)
        return response

    return middleware
