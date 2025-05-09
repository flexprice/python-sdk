# TypesCustomerFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ids** | **List[str]** |  | [optional] 
**email** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**expand** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**filters** | [**List[TypesFilterCondition]**](TypesFilterCondition.md) | filters allows complex filtering based on multiple fields | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**order** | **str** |  | [optional] 
**sort** | [**List[TypesSortCondition]**](TypesSortCondition.md) |  | [optional] 
**start_time** | **str** |  | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 

## Example

```python
from flexprice.models.types_customer_filter import TypesCustomerFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TypesCustomerFilter from a JSON string
types_customer_filter_instance = TypesCustomerFilter.from_json(json)
# print the JSON string representation of the object
print(TypesCustomerFilter.to_json())

# convert the object into a dict
types_customer_filter_dict = types_customer_filter_instance.to_dict()
# create an instance of TypesCustomerFilter from a dict
types_customer_filter_from_dict = TypesCustomerFilter.from_dict(types_customer_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


