# DtoUpdateCustomerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_city** | **str** |  | [optional] 
**address_country** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_postal_code** | **str** |  | [optional] 
**address_state** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_update_customer_request import DtoUpdateCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateCustomerRequest from a JSON string
dto_update_customer_request_instance = DtoUpdateCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateCustomerRequest.to_json())

# convert the object into a dict
dto_update_customer_request_dict = dto_update_customer_request_instance.to_dict()
# create an instance of DtoUpdateCustomerRequest from a dict
dto_update_customer_request_from_dict = DtoUpdateCustomerRequest.from_dict(dto_update_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


