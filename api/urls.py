from django.urls import path, re_path
from django.conf.urls import include
from .views import (
    AccountList,
    ExtractList,
    CreditList,
    AccountExtractView,
    AccountCreditView,
)
from .page import page_bank, page_account, page_credit

# from .api_view import api_root


urlpatterns = [
    # path("", api_root, name="api-root"),
    path("", page_bank, name="page_bank"),
    re_path(r"^(?P<number>[0-9]+)/?$", page_account, name="page_account"),
    re_path(r"^(?P<number>[0-9]+)/c/?$", page_credit, name="page_credit"),
    path("account/", AccountList.as_view(), name="account-list"),
    path("extract/", ExtractList.as_view(), name="extract-list"),
    path("credit/", CreditList.as_view(), name="credit-list"),
    re_path(
        r"^me/(?P<number>[0-9]+)/?$",
        AccountExtractView.as_view(),
        name="accountextract-detail",
    ),
    re_path(
        r"^mc/(?P<number>[0-9]+)/?$",
        AccountCreditView.as_view(),
        name="accountcredit-detail",
    ),
]

urlpatterns += [path("api-auth/", include("rest_framework.urls"))]
