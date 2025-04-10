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


class TypesPauseMode(str, Enum):
    """
    TypesPauseMode
    """

    """
    allowed enum values
    """
    IMMEDIATE = 'immediate'
    SCHEDULED = 'scheduled'
    PERIOD_END = 'period_end'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TypesPauseMode from a JSON string"""
        return cls(json.loads(json_str))


