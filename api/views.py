from rest_framework import generics
from .models import Account, Extract
from .serializers import (
    AccountSerializer,
    ExtractSerializer,
    AccountExtractSerializer,
)


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ExtractList(generics.ListCreateAPIView):
    queryset = Extract.objects.all()
    serializer_class = ExtractSerializer


class AccountExtractView(generics.RetrieveAPIView):
    lookup_field = "number"
    lookup_url_kwarg = "number"
    queryset = Account.objects.all()
    serializer_class = AccountExtractSerializer
