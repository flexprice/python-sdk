# DtoPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**attempts** | [**List[DtoPaymentAttemptResponse]**](DtoPaymentAttemptResponse.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**destination_id** | **str** |  | [optional] 
**destination_type** | [**TypesPaymentDestinationType**](TypesPaymentDestinationType.md) |  | [optional] 
**error_message** | **str** |  | [optional] 
**failed_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**payment_method_type** | [**TypesPaymentMethodType**](TypesPaymentMethodType.md) |  | [optional] 
**payment_status** | [**TypesPaymentStatus**](TypesPaymentStatus.md) |  | [optional] 
**refunded_at** | **str** |  | [optional] 
**succeeded_at** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**track_attempts** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_payment_response import DtoPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoPaymentResponse from a JSON string
dto_payment_response_instance = DtoPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(DtoPaymentResponse.to_json())

# convert the object into a dict
dto_payment_response_dict = dto_payment_response_instance.to_dict()
# create an instance of DtoPaymentResponse from a dict
dto_payment_response_from_dict = DtoPaymentResponse.from_dict(dto_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


