# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class ListType(pydantic.BaseModel):
    value_type: VariableType = pydantic.Field(alias="valueType")
    is_fixed_length: typing.Optional[bool] = pydantic.Field(
        alias="isFixedLength",
        description="Whether this list is fixed-size (for languages that supports fixed-size lists). Defaults to false.",
    )

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


from .variable_type import VariableType  # noqa: E402

ListType.update_forward_refs()
