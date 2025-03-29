# DtoCreatePaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**currency** | **str** |  | 
**destination_id** | **str** |  | 
**destination_type** | [**TypesPaymentDestinationType**](TypesPaymentDestinationType.md) |  | 
**idempotency_key** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**payment_method_type** | [**TypesPaymentMethodType**](TypesPaymentMethodType.md) |  | 
**process_payment** | **bool** |  | [optional] [default to True]

## Example

```python
from flexprice_client.models.dto_create_payment_request import DtoCreatePaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreatePaymentRequest from a JSON string
dto_create_payment_request_instance = DtoCreatePaymentRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreatePaymentRequest.to_json())

# convert the object into a dict
dto_create_payment_request_dict = dto_create_payment_request_instance.to_dict()
# create an instance of DtoCreatePaymentRequest from a dict
dto_create_payment_request_from_dict = DtoCreatePaymentRequest.from_dict(dto_create_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


