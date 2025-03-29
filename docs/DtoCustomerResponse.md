# DtoCustomerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_city** | **str** | AddressCity is the city of the customer&#39;s address | [optional] 
**address_country** | **str** | AddressCountry is the country of the customer&#39;s address (ISO 3166-1 alpha-2) | [optional] 
**address_line1** | **str** | AddressLine1 is the first line of the customer&#39;s address | [optional] 
**address_line2** | **str** | AddressLine2 is the second line of the customer&#39;s address | [optional] 
**address_postal_code** | **str** | AddressPostalCode is the postal code of the customer&#39;s address | [optional] 
**address_state** | **str** | AddressState is the state of the customer&#39;s address | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**email** | **str** | Email is the email of the customer | [optional] 
**environment_id** | **str** | EnvironmentID is the environment identifier for the customer | [optional] 
**external_id** | **str** | ExternalID is the external identifier for the customer | [optional] 
**id** | **str** | ID is the unique identifier for the customer | [optional] 
**metadata** | **Dict[str, str]** | Metadata | [optional] 
**name** | **str** | Name is the name of the customer | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_customer_response import DtoCustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCustomerResponse from a JSON string
dto_customer_response_instance = DtoCustomerResponse.from_json(json)
# print the JSON string representation of the object
print(DtoCustomerResponse.to_json())

# convert the object into a dict
dto_customer_response_dict = dto_customer_response_instance.to_dict()
# create an instance of DtoCustomerResponse from a dict
dto_customer_response_from_dict = DtoCustomerResponse.from_dict(dto_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


