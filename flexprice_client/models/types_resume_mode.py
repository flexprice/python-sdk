# coding: utf-8

"""
    FlexPrice API

    FlexPrice API Service

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TypesResumeMode(str, Enum):
    """
    TypesResumeMode
    """

    """
    allowed enum values
    """
    IMMEDIATE = 'immediate'
    SCHEDULED = 'scheduled'
    AUTO = 'auto'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TypesResumeMode from a JSON string"""
        return cls(json.loads(json_str))


