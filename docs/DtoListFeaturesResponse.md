# DtoListFeaturesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoFeatureResponse]**](DtoFeatureResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_list_features_response import DtoListFeaturesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListFeaturesResponse from a JSON string
dto_list_features_response_instance = DtoListFeaturesResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListFeaturesResponse.to_json())

# convert the object into a dict
dto_list_features_response_dict = dto_list_features_response_instance.to_dict()
# create an instance of DtoListFeaturesResponse from a dict
dto_list_features_response_from_dict = DtoListFeaturesResponse.from_dict(dto_list_features_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


