# DtoCreateSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_cadence** | [**TypesBillingCadence**](TypesBillingCadence.md) |  | 
**billing_period** | [**TypesBillingPeriod**](TypesBillingPeriod.md) |  | 
**billing_period_count** | **int** |  | 
**currency** | **str** |  | 
**customer_id** | **str** |  | 
**end_date** | **str** |  | [optional] 
**lookup_key** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**plan_id** | **str** |  | 
**start_date** | **str** |  | 
**trial_end** | **str** |  | [optional] 
**trial_start** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_create_subscription_request import DtoCreateSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateSubscriptionRequest from a JSON string
dto_create_subscription_request_instance = DtoCreateSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateSubscriptionRequest.to_json())

# convert the object into a dict
dto_create_subscription_request_dict = dto_create_subscription_request_instance.to_dict()
# create an instance of DtoCreateSubscriptionRequest from a dict
dto_create_subscription_request_from_dict = DtoCreateSubscriptionRequest.from_dict(dto_create_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


