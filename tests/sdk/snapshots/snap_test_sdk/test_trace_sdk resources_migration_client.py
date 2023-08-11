# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from .types.migration import Migration


class MigrationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_attempted_migrations(self, *, admin_key_header: str) -> typing.List[Migration]:
        """
        Parameters:
            - admin_key_header: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "migration-info/all"),
            headers=remove_none_from_dict({**self._client_wrapper.get_headers(), "admin-key-header": admin_key_header}),
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Migration], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMigrationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_attempted_migrations(self, *, admin_key_header: str) -> typing.List[Migration]:
        """
        Parameters:
            - admin_key_header: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "migration-info/all"),
            headers=remove_none_from_dict({**self._client_wrapper.get_headers(), "admin-key-header": admin_key_header}),
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Migration], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
