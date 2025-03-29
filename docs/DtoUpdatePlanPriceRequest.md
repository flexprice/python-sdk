# DtoUpdatePlanPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**billing_cadence** | [**TypesBillingCadence**](TypesBillingCadence.md) |  | 
**billing_model** | [**TypesBillingModel**](TypesBillingModel.md) |  | 
**billing_period** | [**TypesBillingPeriod**](TypesBillingPeriod.md) |  | 
**billing_period_count** | **int** |  | 
**currency** | **str** |  | 
**description** | **str** |  | [optional] 
**filter_values** | **Dict[str, List[str]]** |  | [optional] 
**id** | **str** | The ID of the price to update (present if the price is being updated) | [optional] 
**invoice_cadence** | [**TypesInvoiceCadence**](TypesInvoiceCadence.md) |  | 
**lookup_key** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**meter_id** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**tier_mode** | [**TypesBillingTier**](TypesBillingTier.md) |  | [optional] 
**tiers** | [**List[DtoCreatePriceTier]**](DtoCreatePriceTier.md) |  | [optional] 
**transform_quantity** | [**PriceTransformQuantity**](PriceTransformQuantity.md) |  | [optional] 
**trial_period** | **int** |  | [optional] 
**type** | [**TypesPriceType**](TypesPriceType.md) |  | 

## Example

```python
from flexprice_client.models.dto_update_plan_price_request import DtoUpdatePlanPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdatePlanPriceRequest from a JSON string
dto_update_plan_price_request_instance = DtoUpdatePlanPriceRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdatePlanPriceRequest.to_json())

# convert the object into a dict
dto_update_plan_price_request_dict = dto_update_plan_price_request_instance.to_dict()
# create an instance of DtoUpdatePlanPriceRequest from a dict
dto_update_plan_price_request_from_dict = DtoUpdatePlanPriceRequest.from_dict(dto_update_plan_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


