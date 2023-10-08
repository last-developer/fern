# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .movie_id import MovieId


class Movie(pydantic.BaseModel):
    """
    from seed.examples import Movie

    Movie(id="movie-c06a4ad7", title="The Boy and the Heron", from_="Hayao Miyazaki", rating=8.0)
    """

    id: MovieId
    title: str
    from_: str = pydantic.Field(alias="from")
    rating: float = pydantic.Field(description="The rating scale is one to five stars")
    type: typing_extensions.Literal["movie"]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
