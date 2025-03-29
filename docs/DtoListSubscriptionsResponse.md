# DtoListSubscriptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoSubscriptionResponse]**](DtoSubscriptionResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_list_subscriptions_response import DtoListSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListSubscriptionsResponse from a JSON string
dto_list_subscriptions_response_instance = DtoListSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListSubscriptionsResponse.to_json())

# convert the object into a dict
dto_list_subscriptions_response_dict = dto_list_subscriptions_response_instance.to_dict()
# create an instance of DtoListSubscriptionsResponse from a dict
dto_list_subscriptions_response_from_dict = DtoListSubscriptionsResponse.from_dict(dto_list_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


