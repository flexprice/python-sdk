# DtoUpdatePaymentStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**payment_status** | [**TypesPaymentStatus**](TypesPaymentStatus.md) |  | 

## Example

```python
from flexprice.models.dto_update_payment_status_request import DtoUpdatePaymentStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdatePaymentStatusRequest from a JSON string
dto_update_payment_status_request_instance = DtoUpdatePaymentStatusRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdatePaymentStatusRequest.to_json())

# convert the object into a dict
dto_update_payment_status_request_dict = dto_update_payment_status_request_instance.to_dict()
# create an instance of DtoUpdatePaymentStatusRequest from a dict
dto_update_payment_status_request_from_dict = DtoUpdatePaymentStatusRequest.from_dict(dto_update_payment_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


