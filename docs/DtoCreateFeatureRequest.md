# DtoCreateFeatureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**lookup_key** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**meter** | [**DtoCreateMeterRequest**](DtoCreateMeterRequest.md) |  | [optional] 
**meter_id** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | [**TypesFeatureType**](TypesFeatureType.md) |  | 
**unit_plural** | **str** |  | [optional] 
**unit_singular** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_create_feature_request import DtoCreateFeatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateFeatureRequest from a JSON string
dto_create_feature_request_instance = DtoCreateFeatureRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateFeatureRequest.to_json())

# convert the object into a dict
dto_create_feature_request_dict = dto_create_feature_request_instance.to_dict()
# create an instance of DtoCreateFeatureRequest from a dict
dto_create_feature_request_from_dict = DtoCreateFeatureRequest.from_dict(dto_create_feature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


