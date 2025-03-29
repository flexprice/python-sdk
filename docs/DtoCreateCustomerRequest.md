# DtoCreateCustomerRequest


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
**external_id** | **str** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_create_customer_request import DtoCreateCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateCustomerRequest from a JSON string
dto_create_customer_request_instance = DtoCreateCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateCustomerRequest.to_json())

# convert the object into a dict
dto_create_customer_request_dict = dto_create_customer_request_instance.to_dict()
# create an instance of DtoCreateCustomerRequest from a dict
dto_create_customer_request_from_dict = DtoCreateCustomerRequest.from_dict(dto_create_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


