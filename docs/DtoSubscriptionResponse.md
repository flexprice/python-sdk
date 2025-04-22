# DtoSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_pause_id** | **str** | ActivePauseID references the current active pause configuration This will be null if no pause is active or scheduled | [optional] 
**billing_anchor** | **str** | BillingAnchor is the reference point that aligns future billing cycle dates. It sets the day of week for week intervals, the day of month for month and year intervals, and the month of year for year intervals. The timestamp is in UTC format. | [optional] 
**billing_cadence** | [**TypesBillingCadence**](TypesBillingCadence.md) |  | [optional] 
**billing_cycle** | [**TypesBillingCycle**](TypesBillingCycle.md) |  | [optional] 
**billing_period** | [**TypesBillingPeriod**](TypesBillingPeriod.md) |  | [optional] 
**billing_period_count** | **int** | BillingPeriodCount is the total number units of the billing period. | [optional] 
**cancel_at** | **str** | CancelAt is the date the subscription will be canceled | [optional] 
**cancel_at_period_end** | **bool** | CancelAtPeriodEnd is whether the subscription was canceled at the end of the current period | [optional] 
**cancelled_at** | **str** | CanceledAt is the date the subscription was canceled | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**currency** | **str** | Currency is the currency of the subscription in lowercase 3 digit ISO codes | [optional] 
**current_period_end** | **str** | CurrentPeriodEnd is the end of the current period that the subscription has been invoiced for. At the end of this period, a new invoice will be created. | [optional] 
**current_period_start** | **str** | CurrentPeriodStart is the end of the current period that the subscription has been invoiced for. At the end of this period, a new invoice will be created. | [optional] 
**customer** | [**DtoCustomerResponse**](DtoCustomerResponse.md) |  | [optional] 
**customer_id** | **str** | CustomerID is the identifier for the customer in our system | [optional] 
**end_date** | **str** | EndDate is the end date of the subscription | [optional] 
**environment_id** | **str** | EnvironmentID is the environment identifier for the subscription | [optional] 
**id** | **str** | ID is the unique identifier for the subscription | [optional] 
**line_items** | [**List[SubscriptionSubscriptionLineItem]**](SubscriptionSubscriptionLineItem.md) |  | [optional] 
**lookup_key** | **str** | LookupKey is the key used to lookup the subscription in our system | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**pause_status** | [**TypesPauseStatus**](TypesPauseStatus.md) |  | [optional] 
**pauses** | [**List[SubscriptionSubscriptionPause]**](SubscriptionSubscriptionPause.md) |  | [optional] 
**plan** | [**DtoPlanResponse**](DtoPlanResponse.md) |  | [optional] 
**plan_id** | **str** | PlanID is the identifier for the plan in our system | [optional] 
**start_date** | **str** | StartDate is the start date of the subscription | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**subscription_status** | [**TypesSubscriptionStatus**](TypesSubscriptionStatus.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**trial_end** | **str** | TrialEnd is the end date of the trial period | [optional] 
**trial_start** | **str** | TrialStart is the start date of the trial period | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**version** | **int** | Version is used for optimistic locking | [optional] 

## Example

```python
from flexprice.models.dto_subscription_response import DtoSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSubscriptionResponse from a JSON string
dto_subscription_response_instance = DtoSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(DtoSubscriptionResponse.to_json())

# convert the object into a dict
dto_subscription_response_dict = dto_subscription_response_instance.to_dict()
# create an instance of DtoSubscriptionResponse from a dict
dto_subscription_response_from_dict = DtoSubscriptionResponse.from_dict(dto_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


