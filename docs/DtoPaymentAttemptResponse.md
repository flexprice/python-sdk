# DtoPaymentAttemptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_number** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_payment_attempt_response import DtoPaymentAttemptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoPaymentAttemptResponse from a JSON string
dto_payment_attempt_response_instance = DtoPaymentAttemptResponse.from_json(json)
# print the JSON string representation of the object
print(DtoPaymentAttemptResponse.to_json())

# convert the object into a dict
dto_payment_attempt_response_dict = dto_payment_attempt_response_instance.to_dict()
# create an instance of DtoPaymentAttemptResponse from a dict
dto_payment_attempt_response_from_dict = DtoPaymentAttemptResponse.from_dict(dto_payment_attempt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


