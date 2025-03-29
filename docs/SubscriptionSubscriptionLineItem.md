# SubscriptionSubscriptionLineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_period** | [**TypesBillingPeriod**](TypesBillingPeriod.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**invoice_cadence** | [**TypesInvoiceCadence**](TypesInvoiceCadence.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**meter_display_name** | **str** |  | [optional] 
**meter_id** | **str** |  | [optional] 
**plan_display_name** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**price_id** | **str** |  | [optional] 
**price_type** | [**TypesPriceType**](TypesPriceType.md) |  | [optional] 
**quantity** | **float** |  | [optional] 
**start_date** | **str** |  | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**trial_period** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.subscription_subscription_line_item import SubscriptionSubscriptionLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionSubscriptionLineItem from a JSON string
subscription_subscription_line_item_instance = SubscriptionSubscriptionLineItem.from_json(json)
# print the JSON string representation of the object
print(SubscriptionSubscriptionLineItem.to_json())

# convert the object into a dict
subscription_subscription_line_item_dict = subscription_subscription_line_item_instance.to_dict()
# create an instance of SubscriptionSubscriptionLineItem from a dict
subscription_subscription_line_item_from_dict = SubscriptionSubscriptionLineItem.from_dict(subscription_subscription_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


