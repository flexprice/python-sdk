# DtoListSubscriptionPausesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoSubscriptionPauseResponse]**](DtoSubscriptionPauseResponse.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from flexprice.models.dto_list_subscription_pauses_response import DtoListSubscriptionPausesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListSubscriptionPausesResponse from a JSON string
dto_list_subscription_pauses_response_instance = DtoListSubscriptionPausesResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListSubscriptionPausesResponse.to_json())

# convert the object into a dict
dto_list_subscription_pauses_response_dict = dto_list_subscription_pauses_response_instance.to_dict()
# create an instance of DtoListSubscriptionPausesResponse from a dict
dto_list_subscription_pauses_response_from_dict = DtoListSubscriptionPausesResponse.from_dict(dto_list_subscription_pauses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


