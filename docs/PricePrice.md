# PricePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount stored in main currency units (e.g., dollars, not cents) For USD: 12.50 means $12.50 | [optional] 
**billing_cadence** | [**TypesBillingCadence**](TypesBillingCadence.md) |  | [optional] 
**billing_model** | [**TypesBillingModel**](TypesBillingModel.md) |  | [optional] 
**billing_period** | [**TypesBillingPeriod**](TypesBillingPeriod.md) |  | [optional] 
**billing_period_count** | **int** | BillingPeriodCount is the count of the billing period ex 1, 3, 6, 12 | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**currency** | **str** | Currency 3 digit ISO currency code in lowercase ex usd, eur, gbp | [optional] 
**description** | **str** | Description of the price | [optional] 
**display_amount** | **str** | DisplayAmount is the formatted amount with currency symbol For USD: $12.50 | [optional] 
**environment_id** | **str** | EnvironmentID is the environment identifier for the price | [optional] 
**filter_values** | **Dict[str, List[str]]** |  | [optional] 
**id** | **str** | ID uuid identifier for the price | [optional] 
**invoice_cadence** | [**TypesInvoiceCadence**](TypesInvoiceCadence.md) |  | [optional] 
**lookup_key** | **str** | LookupKey used for looking up the price in the database | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**meter_id** | **str** | MeterID is the id of the meter for usage based pricing | [optional] 
**plan_id** | **str** | PlanID is the id of the plan for plan based pricing | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**tier_mode** | [**TypesBillingTier**](TypesBillingTier.md) |  | [optional] 
**tiers** | [**List[PricePriceTier]**](PricePriceTier.md) |  | [optional] 
**transform_quantity** | [**PriceJSONBTransformQuantity**](PriceJSONBTransformQuantity.md) |  | [optional] 
**trial_period** | **int** | TrialPeriod is the number of days for the trial period Note: This is only applicable for recurring prices (BILLING_CADENCE_RECURRING) | [optional] 
**type** | [**TypesPriceType**](TypesPriceType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.price_price import PricePrice

# TODO update the JSON string below
json = "{}"
# create an instance of PricePrice from a JSON string
price_price_instance = PricePrice.from_json(json)
# print the JSON string representation of the object
print(PricePrice.to_json())

# convert the object into a dict
price_price_dict = price_price_instance.to_dict()
# create an instance of PricePrice from a dict
price_price_from_dict = PricePrice.from_dict(price_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


