# DtoSubscriptionUsageByMetersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**display_amount** | **str** |  | [optional] 
**filter_values** | **Dict[str, List[str]]** |  | [optional] 
**meter_display_name** | **str** |  | [optional] 
**meter_id** | **str** |  | [optional] 
**price** | [**PricePrice**](PricePrice.md) |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_subscription_usage_by_meters_response import DtoSubscriptionUsageByMetersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSubscriptionUsageByMetersResponse from a JSON string
dto_subscription_usage_by_meters_response_instance = DtoSubscriptionUsageByMetersResponse.from_json(json)
# print the JSON string representation of the object
print(DtoSubscriptionUsageByMetersResponse.to_json())

# convert the object into a dict
dto_subscription_usage_by_meters_response_dict = dto_subscription_usage_by_meters_response_instance.to_dict()
# create an instance of DtoSubscriptionUsageByMetersResponse from a dict
dto_subscription_usage_by_meters_response_from_dict = DtoSubscriptionUsageByMetersResponse.from_dict(dto_subscription_usage_by_meters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


