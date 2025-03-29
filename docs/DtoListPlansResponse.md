# DtoListPlansResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoPlanResponse]**](DtoPlanResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_list_plans_response import DtoListPlansResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListPlansResponse from a JSON string
dto_list_plans_response_instance = DtoListPlansResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListPlansResponse.to_json())

# convert the object into a dict
dto_list_plans_response_dict = dto_list_plans_response_instance.to_dict()
# create an instance of DtoListPlansResponse from a dict
dto_list_plans_response_from_dict = DtoListPlansResponse.from_dict(dto_list_plans_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


