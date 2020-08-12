from django.urls import path, re_path
from django.conf.urls import include
from .views import AccountList, ExtractList, AccountExtractView
from .page import page_bank, page_account
# from .api_view import api_root


urlpatterns = [
    # path("", api_root, name="api-root"),
    path("", page_bank, name="page_bank"),
    re_path(r"^(?P<number>[0-9]+)/?$", page_account, name="page_account"),
    path("account/", AccountList.as_view(), name="account-list"),
    path("extract/", ExtractList.as_view(), name="extract-list"),
    re_path(
        r"^me/(?P<number>[0-9]+)/?$",
        AccountExtractView.as_view(),
        name="accountextract-detail",
    ),
]

urlpatterns += [path("api-auth/", include("rest_framework.urls"))]
