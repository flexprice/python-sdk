# DtoGetUsageBySubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **str** |  | [optional] 
**lifetime_usage** | **bool** |  | [optional] 
**start_time** | **str** |  | [optional] 
**subscription_id** | **str** |  | 

## Example

```python
from flexprice_client.models.dto_get_usage_by_subscription_request import DtoGetUsageBySubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetUsageBySubscriptionRequest from a JSON string
dto_get_usage_by_subscription_request_instance = DtoGetUsageBySubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(DtoGetUsageBySubscriptionRequest.to_json())

# convert the object into a dict
dto_get_usage_by_subscription_request_dict = dto_get_usage_by_subscription_request_instance.to_dict()
# create an instance of DtoGetUsageBySubscriptionRequest from a dict
dto_get_usage_by_subscription_request_from_dict = DtoGetUsageBySubscriptionRequest.from_dict(dto_get_usage_by_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


