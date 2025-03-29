# DtoCustomerMultiCurrencyInvoiceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**default_currency** | **str** |  | [optional] 
**summaries** | [**List[DtoCustomerInvoiceSummary]**](DtoCustomerInvoiceSummary.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_customer_multi_currency_invoice_summary import DtoCustomerMultiCurrencyInvoiceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCustomerMultiCurrencyInvoiceSummary from a JSON string
dto_customer_multi_currency_invoice_summary_instance = DtoCustomerMultiCurrencyInvoiceSummary.from_json(json)
# print the JSON string representation of the object
print(DtoCustomerMultiCurrencyInvoiceSummary.to_json())

# convert the object into a dict
dto_customer_multi_currency_invoice_summary_dict = dto_customer_multi_currency_invoice_summary_instance.to_dict()
# create an instance of DtoCustomerMultiCurrencyInvoiceSummary from a dict
dto_customer_multi_currency_invoice_summary_from_dict = DtoCustomerMultiCurrencyInvoiceSummary.from_dict(dto_customer_multi_currency_invoice_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


