# DtoFeatureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**lookup_key** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**meter** | [**DtoMeterResponse**](DtoMeterResponse.md) |  | [optional] 
**meter_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**type** | [**TypesFeatureType**](TypesFeatureType.md) |  | [optional] 
**unit_plural** | **str** |  | [optional] 
**unit_singular** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_feature_response import DtoFeatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoFeatureResponse from a JSON string
dto_feature_response_instance = DtoFeatureResponse.from_json(json)
# print the JSON string representation of the object
print(DtoFeatureResponse.to_json())

# convert the object into a dict
dto_feature_response_dict = dto_feature_response_instance.to_dict()
# create an instance of DtoFeatureResponse from a dict
dto_feature_response_from_dict = DtoFeatureResponse.from_dict(dto_feature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


