# This file was auto-generated by Fern from our API Definition.

import typing

import httpx
import typing_extensions

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.no_headers.client import AsyncNoHeadersClient, NoHeadersClient
from .resources.only_literal_headers.client import AsyncOnlyLiteralHeadersClient, OnlyLiteralHeadersClient
from .resources.with_non_literal_headers.client import AsyncWithNonLiteralHeadersClient, WithNonLiteralHeadersClient


class SeedNurseryApi:
    def __init__(
        self,
        *,
        base_url: str,
        api_header: typing_extensions.Literal["api header value"],
        api_test: bool,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url, api_header=api_header, api_test=api_test, httpx_client=httpx.Client(timeout=timeout)
        )
        self.no_headers = NoHeadersClient(client_wrapper=self._client_wrapper)
        self.only_literal_headers = OnlyLiteralHeadersClient(client_wrapper=self._client_wrapper)
        self.with_non_literal_headers = WithNonLiteralHeadersClient(client_wrapper=self._client_wrapper)


class AsyncSeedNurseryApi:
    def __init__(
        self,
        *,
        base_url: str,
        api_header: typing_extensions.Literal["api header value"],
        api_test: bool,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url, api_header=api_header, api_test=api_test, httpx_client=httpx.AsyncClient(timeout=timeout)
        )
        self.no_headers = AsyncNoHeadersClient(client_wrapper=self._client_wrapper)
        self.only_literal_headers = AsyncOnlyLiteralHeadersClient(client_wrapper=self._client_wrapper)
        self.with_non_literal_headers = AsyncWithNonLiteralHeadersClient(client_wrapper=self._client_wrapper)
