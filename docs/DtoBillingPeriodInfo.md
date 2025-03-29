# DtoBillingPeriodInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **str** |  | [optional] 
**period** | **str** | e.g., \&quot;monthly\&quot;, \&quot;yearly\&quot; | [optional] 
**start_time** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_billing_period_info import DtoBillingPeriodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DtoBillingPeriodInfo from a JSON string
dto_billing_period_info_instance = DtoBillingPeriodInfo.from_json(json)
# print the JSON string representation of the object
print(DtoBillingPeriodInfo.to_json())

# convert the object into a dict
dto_billing_period_info_dict = dto_billing_period_info_instance.to_dict()
# create an instance of DtoBillingPeriodInfo from a dict
dto_billing_period_info_from_dict = DtoBillingPeriodInfo.from_dict(dto_billing_period_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


