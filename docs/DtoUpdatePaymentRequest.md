# DtoUpdatePaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, str]** |  | [optional] 
**payment_status** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_update_payment_request import DtoUpdatePaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdatePaymentRequest from a JSON string
dto_update_payment_request_instance = DtoUpdatePaymentRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdatePaymentRequest.to_json())

# convert the object into a dict
dto_update_payment_request_dict = dto_update_payment_request_instance.to_dict()
# create an instance of DtoUpdatePaymentRequest from a dict
dto_update_payment_request_from_dict = DtoUpdatePaymentRequest.from_dict(dto_update_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


