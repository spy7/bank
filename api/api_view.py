from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request, format=None):
    links = {
        "account": reverse("account-list", request=request, format=format),
        "extract": reverse("extract-list", request=request, format=format),
        "credit": reverse("credit-list", request=request, format=format),
        "me/<number>": reverse(
            "accountextract-detail",
            request=request,
            format=format,
            kwargs={"number": 0},
        ),
        "mc/<number>": reverse(
            "accountcredit-detail",
            request=request,
            format=format,
            kwargs={"number": 0},
        ),
    }
    return Response(links)
