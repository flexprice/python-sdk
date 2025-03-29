# DtoCustomerInvoiceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**overdue_invoice_count** | **int** |  | [optional] 
**total_invoice_count** | **int** |  | [optional] 
**total_overdue_amount** | **float** |  | [optional] 
**total_revenue_amount** | **float** |  | [optional] 
**total_unpaid_amount** | **float** |  | [optional] 
**unpaid_fixed_charges** | **float** |  | [optional] 
**unpaid_invoice_count** | **int** |  | [optional] 
**unpaid_usage_charges** | **float** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_customer_invoice_summary import DtoCustomerInvoiceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCustomerInvoiceSummary from a JSON string
dto_customer_invoice_summary_instance = DtoCustomerInvoiceSummary.from_json(json)
# print the JSON string representation of the object
print(DtoCustomerInvoiceSummary.to_json())

# convert the object into a dict
dto_customer_invoice_summary_dict = dto_customer_invoice_summary_instance.to_dict()
# create an instance of DtoCustomerInvoiceSummary from a dict
dto_customer_invoice_summary_from_dict = DtoCustomerInvoiceSummary.from_dict(dto_customer_invoice_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


