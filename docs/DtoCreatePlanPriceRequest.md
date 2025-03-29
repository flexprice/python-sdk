# DtoCreatePlanPriceRequest


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
from flexprice_client.models.dto_create_plan_price_request import DtoCreatePlanPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreatePlanPriceRequest from a JSON string
dto_create_plan_price_request_instance = DtoCreatePlanPriceRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreatePlanPriceRequest.to_json())

# convert the object into a dict
dto_create_plan_price_request_dict = dto_create_plan_price_request_instance.to_dict()
# create an instance of DtoCreatePlanPriceRequest from a dict
dto_create_plan_price_request_from_dict = DtoCreatePlanPriceRequest.from_dict(dto_create_plan_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


