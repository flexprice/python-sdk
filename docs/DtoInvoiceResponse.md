# DtoInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_due** | **float** |  | [optional] 
**amount_paid** | **float** |  | [optional] 
**amount_remaining** | **float** |  | [optional] 
**billing_period** | **str** |  | [optional] 
**billing_reason** | **str** |  | [optional] 
**billing_sequence** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**customer** | [**DtoCustomerResponse**](DtoCustomerResponse.md) |  | [optional] 
**customer_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**finalized_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**invoice_pdf_url** | **str** |  | [optional] 
**invoice_status** | [**TypesInvoiceStatus**](TypesInvoiceStatus.md) |  | [optional] 
**invoice_type** | [**TypesInvoiceType**](TypesInvoiceType.md) |  | [optional] 
**line_items** | [**List[DtoInvoiceLineItemResponse]**](DtoInvoiceLineItemResponse.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**paid_at** | **str** |  | [optional] 
**payment_status** | [**TypesPaymentStatus**](TypesPaymentStatus.md) |  | [optional] 
**period_end** | **str** |  | [optional] 
**period_start** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**subscription** | [**DtoSubscriptionResponse**](DtoSubscriptionResponse.md) |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**voided_at** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_invoice_response import DtoInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoInvoiceResponse from a JSON string
dto_invoice_response_instance = DtoInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(DtoInvoiceResponse.to_json())

# convert the object into a dict
dto_invoice_response_dict = dto_invoice_response_instance.to_dict()
# create an instance of DtoInvoiceResponse from a dict
dto_invoice_response_from_dict = DtoInvoiceResponse.from_dict(dto_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


