# DtoUpdatePriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**lookup_key** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from flexprice.models.dto_update_price_request import DtoUpdatePriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdatePriceRequest from a JSON string
dto_update_price_request_instance = DtoUpdatePriceRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdatePriceRequest.to_json())

# convert the object into a dict
dto_update_price_request_dict = dto_update_price_request_instance.to_dict()
# create an instance of DtoUpdatePriceRequest from a dict
dto_update_price_request_from_dict = DtoUpdatePriceRequest.from_dict(dto_update_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


