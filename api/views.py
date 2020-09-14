from rest_framework import generics
from .models import Account, Extract, Credit
from .serializers import (
    AccountSerializer,
    ExtractSerializer,
    CreditSerializer,
    AccountExtractSerializer,
    AccountCreditSerializer,
)


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ExtractList(generics.ListCreateAPIView):
    queryset = Extract.objects.all()
    serializer_class = ExtractSerializer


class CreditList(generics.ListCreateAPIView):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer


class AccountExtractView(generics.RetrieveAPIView):
    lookup_field = "number"
    lookup_url_kwarg = "number"
    queryset = Account.objects.all()
    serializer_class = AccountExtractSerializer


class AccountCreditView(generics.RetrieveAPIView):
    lookup_field = "number"
    lookup_url_kwarg = "number"
    queryset = Account.objects.all()
    serializer_class = AccountCreditSerializer
