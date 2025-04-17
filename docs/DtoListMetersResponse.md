# DtoListMetersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoMeterResponse]**](DtoMeterResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_list_meters_response import DtoListMetersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListMetersResponse from a JSON string
dto_list_meters_response_instance = DtoListMetersResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListMetersResponse.to_json())

# convert the object into a dict
dto_list_meters_response_dict = dto_list_meters_response_instance.to_dict()
# create an instance of DtoListMetersResponse from a dict
dto_list_meters_response_from_dict = DtoListMetersResponse.from_dict(dto_list_meters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


