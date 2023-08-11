# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from .errors.invalid_movie_error import InvalidMovieError
from .errors.movie_already_exists_error import MovieAlreadyExistsError
from .errors.movie_not_found_error import MovieNotFoundError
from .types.movie import Movie
from .types.movie_id import MovieId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MovieClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_movie(self, movie_id: MovieId) -> Movie:
        """
        Parameters:
            - movie_id: MovieId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"movie/movie/{movie_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Movie, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all_movies(self, *, string_header: str) -> typing.List[Movie]:
        """
        Parameters:
            - string_header: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "movie/all-movies"),
            headers=remove_none_from_dict(
                {**self._client_wrapper.get_headers(), "literal_header": "hello world", "string_header": string_header}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Movie], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_movie(
        self,
        *,
        date: dt.date,
        datetime: dt.datetime,
        optional_date: typing.Optional[dt.date] = None,
        optional_datetime: typing.Optional[dt.datetime] = None,
        boolean: bool,
        optional_boolean: typing.Optional[bool] = None,
        request: Movie,
    ) -> None:
        """
        Parameters:
            - date: dt.date.

            - datetime: dt.datetime.

            - optional_date: typing.Optional[dt.date].

            - optional_datetime: typing.Optional[dt.datetime].

            - boolean: bool.

            - optional_boolean: typing.Optional[bool].

            - request: Movie.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "movie/movie"),
            params=remove_none_from_dict(
                {
                    "date": str(date),
                    "datetime": serialize_datetime(datetime),
                    "optional_date": str(optional_date) if optional_date is not None else None,
                    "optional_datetime": serialize_datetime(optional_datetime)
                    if optional_datetime is not None
                    else None,
                    "boolean": boolean,
                    "optional_boolean": optional_boolean,
                }
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 429:
            raise MovieAlreadyExistsError()
        if _response.status_code == 400:
            raise InvalidMovieError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_movie(
        self, movie_id: MovieId, *, required_property: str, optional_property: typing.Optional[str] = OMIT
    ) -> None:
        """
        Parameters:
            - movie_id: MovieId.

            - required_property: str.

            - optional_property: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {"required_property": required_property}
        if optional_property is not OMIT:
            _request["optional_property"] = optional_property
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"movie/{movie_id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMovieClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_movie(self, movie_id: MovieId) -> Movie:
        """
        Parameters:
            - movie_id: MovieId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"movie/movie/{movie_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Movie, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all_movies(self, *, string_header: str) -> typing.List[Movie]:
        """
        Parameters:
            - string_header: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "movie/all-movies"),
            headers=remove_none_from_dict(
                {**self._client_wrapper.get_headers(), "literal_header": "hello world", "string_header": string_header}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Movie], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_movie(
        self,
        *,
        date: dt.date,
        datetime: dt.datetime,
        optional_date: typing.Optional[dt.date] = None,
        optional_datetime: typing.Optional[dt.datetime] = None,
        boolean: bool,
        optional_boolean: typing.Optional[bool] = None,
        request: Movie,
    ) -> None:
        """
        Parameters:
            - date: dt.date.

            - datetime: dt.datetime.

            - optional_date: typing.Optional[dt.date].

            - optional_datetime: typing.Optional[dt.datetime].

            - boolean: bool.

            - optional_boolean: typing.Optional[bool].

            - request: Movie.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "movie/movie"),
            params=remove_none_from_dict(
                {
                    "date": str(date),
                    "datetime": serialize_datetime(datetime),
                    "optional_date": str(optional_date) if optional_date is not None else None,
                    "optional_datetime": serialize_datetime(optional_datetime)
                    if optional_datetime is not None
                    else None,
                    "boolean": boolean,
                    "optional_boolean": optional_boolean,
                }
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 429:
            raise MovieAlreadyExistsError()
        if _response.status_code == 400:
            raise InvalidMovieError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_movie(
        self, movie_id: MovieId, *, required_property: str, optional_property: typing.Optional[str] = OMIT
    ) -> None:
        """
        Parameters:
            - movie_id: MovieId.

            - required_property: str.

            - optional_property: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {"required_property": required_property}
        if optional_property is not OMIT:
            _request["optional_property"] = optional_property
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"movie/{movie_id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
