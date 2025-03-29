# DtoPauseSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**pause_days** | **int** |  | [optional] 
**pause_end** | **str** |  | [optional] 
**pause_mode** | [**TypesPauseMode**](TypesPauseMode.md) |  | 
**pause_start** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_pause_subscription_request import DtoPauseSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoPauseSubscriptionRequest from a JSON string
dto_pause_subscription_request_instance = DtoPauseSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(DtoPauseSubscriptionRequest.to_json())

# convert the object into a dict
dto_pause_subscription_request_dict = dto_pause_subscription_request_instance.to_dict()
# create an instance of DtoPauseSubscriptionRequest from a dict
dto_pause_subscription_request_from_dict = DtoPauseSubscriptionRequest.from_dict(dto_pause_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


