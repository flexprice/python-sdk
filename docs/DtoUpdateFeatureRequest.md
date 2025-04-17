# DtoUpdateFeatureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**filters** | [**List[MeterFilter]**](MeterFilter.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**unit_plural** | **str** |  | [optional] 
**unit_singular** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_update_feature_request import DtoUpdateFeatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateFeatureRequest from a JSON string
dto_update_feature_request_instance = DtoUpdateFeatureRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateFeatureRequest.to_json())

# convert the object into a dict
dto_update_feature_request_dict = dto_update_feature_request_instance.to_dict()
# create an instance of DtoUpdateFeatureRequest from a dict
dto_update_feature_request_from_dict = DtoUpdateFeatureRequest.from_dict(dto_update_feature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


