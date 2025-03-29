# DtoResumeSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**resume_mode** | [**TypesResumeMode**](TypesResumeMode.md) |  | 

## Example

```python
from flexprice_client.models.dto_resume_subscription_request import DtoResumeSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoResumeSubscriptionRequest from a JSON string
dto_resume_subscription_request_instance = DtoResumeSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(DtoResumeSubscriptionRequest.to_json())

# convert the object into a dict
dto_resume_subscription_request_dict = dto_resume_subscription_request_instance.to_dict()
# create an instance of DtoResumeSubscriptionRequest from a dict
dto_resume_subscription_request_from_dict = DtoResumeSubscriptionRequest.from_dict(dto_resume_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


