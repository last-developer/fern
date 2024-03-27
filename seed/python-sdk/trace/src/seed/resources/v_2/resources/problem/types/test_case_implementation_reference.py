# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .test_case_implementation import TestCaseImplementation
from .test_case_template_id import TestCaseTemplateId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TestCaseImplementationReference_TemplateId(pydantic.BaseModel):
    type: typing.Literal["templateId"] = "templateId"
    value: TestCaseTemplateId

    class Config:
        frozen = True
        smart_union = True


class TestCaseImplementationReference_Implementation(TestCaseImplementation):
    type: typing.Literal["implementation"] = "implementation"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


TestCaseImplementationReference = typing.Union[
    TestCaseImplementationReference_TemplateId, TestCaseImplementationReference_Implementation
]
