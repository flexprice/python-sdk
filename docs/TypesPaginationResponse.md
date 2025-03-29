# TypesPaginationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from flexprice.models.types_pagination_response import TypesPaginationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TypesPaginationResponse from a JSON string
types_pagination_response_instance = TypesPaginationResponse.from_json(json)
# print the JSON string representation of the object
print(TypesPaginationResponse.to_json())

# convert the object into a dict
types_pagination_response_dict = types_pagination_response_instance.to_dict()
# create an instance of TypesPaginationResponse from a dict
types_pagination_response_from_dict = TypesPaginationResponse.from_dict(types_pagination_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


