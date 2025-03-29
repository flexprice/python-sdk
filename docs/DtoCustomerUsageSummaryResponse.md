# DtoCustomerUsageSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**features** | [**List[DtoFeatureUsageSummary]**](DtoFeatureUsageSummary.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 
**period** | [**DtoBillingPeriodInfo**](DtoBillingPeriodInfo.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_customer_usage_summary_response import DtoCustomerUsageSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCustomerUsageSummaryResponse from a JSON string
dto_customer_usage_summary_response_instance = DtoCustomerUsageSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(DtoCustomerUsageSummaryResponse.to_json())

# convert the object into a dict
dto_customer_usage_summary_response_dict = dto_customer_usage_summary_response_instance.to_dict()
# create an instance of DtoCustomerUsageSummaryResponse from a dict
dto_customer_usage_summary_response_from_dict = DtoCustomerUsageSummaryResponse.from_dict(dto_customer_usage_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


