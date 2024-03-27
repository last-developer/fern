# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def and_(self, value: bool) -> Test:
        return Test(__root__=_Test.And(type="and", value=value))

    def or_(self, value: bool) -> Test:
        return Test(__root__=_Test.Or(type="or", value=value))


class Test(pydantic.BaseModel):
    """
    from seed.examples import Test_And

    Test_And(value=True)
    """

    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_Test.And, _Test.Or]:
        return self.__root__

    def visit(self, and_: typing.Callable[[bool], T_Result], or_: typing.Callable[[bool], T_Result]) -> T_Result:
        if self.__root__.type == "and":
            return and_(self.__root__.value)
        if self.__root__.type == "or":
            return or_(self.__root__.value)

    __root__: typing.Annotated[typing.Union[_Test.And, _Test.Or], pydantic.Field(discriminator="type")]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _Test:
    class And(pydantic.BaseModel):
        type: typing.Literal["and"] = "and"
        value: bool

    class Or(pydantic.BaseModel):
        type: typing.Literal["or"] = "or"
        value: bool


Test.update_forward_refs()
