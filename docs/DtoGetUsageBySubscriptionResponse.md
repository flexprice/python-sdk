# DtoGetUsageBySubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**charges** | [**List[DtoSubscriptionUsageByMetersResponse]**](DtoSubscriptionUsageByMetersResponse.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**display_amount** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_get_usage_by_subscription_response import DtoGetUsageBySubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetUsageBySubscriptionResponse from a JSON string
dto_get_usage_by_subscription_response_instance = DtoGetUsageBySubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(DtoGetUsageBySubscriptionResponse.to_json())

# convert the object into a dict
dto_get_usage_by_subscription_response_dict = dto_get_usage_by_subscription_response_instance.to_dict()
# create an instance of DtoGetUsageBySubscriptionResponse from a dict
dto_get_usage_by_subscription_response_from_dict = DtoGetUsageBySubscriptionResponse.from_dict(dto_get_usage_by_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


