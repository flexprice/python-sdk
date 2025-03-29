# SubscriptionSubscriptionPause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**environment_id** | **str** | EnvironmentID is the environment identifier for the pause | [optional] 
**id** | **str** | ID is the unique identifier for the subscription pause | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**original_period_end** | **str** | OriginalPeriodEnd is the end of the billing period when the pause was created | [optional] 
**original_period_start** | **str** | OriginalPeriodStart is the start of the billing period when the pause was created | [optional] 
**pause_end** | **str** | PauseEnd is when the pause will end (null for indefinite) | [optional] 
**pause_mode** | [**TypesPauseMode**](TypesPauseMode.md) |  | [optional] 
**pause_start** | **str** | PauseStart is when the pause actually started | [optional] 
**pause_status** | [**TypesPauseStatus**](TypesPauseStatus.md) |  | [optional] 
**reason** | **str** | Reason is the reason for pausing | [optional] 
**resume_mode** | [**TypesResumeMode**](TypesResumeMode.md) |  | [optional] 
**resumed_at** | **str** | ResumedAt is when the pause was actually ended (if manually resumed) | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**subscription_id** | **str** | SubscriptionID is the identifier for the subscription | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice.models.subscription_subscription_pause import SubscriptionSubscriptionPause

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionSubscriptionPause from a JSON string
subscription_subscription_pause_instance = SubscriptionSubscriptionPause.from_json(json)
# print the JSON string representation of the object
print(SubscriptionSubscriptionPause.to_json())

# convert the object into a dict
subscription_subscription_pause_dict = subscription_subscription_pause_instance.to_dict()
# create an instance of SubscriptionSubscriptionPause from a dict
subscription_subscription_pause_from_dict = SubscriptionSubscriptionPause.from_dict(subscription_subscription_pause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


