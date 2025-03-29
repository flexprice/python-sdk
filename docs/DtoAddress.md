# DtoAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_city** | **str** |  | [optional] 
**address_country** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_postal_code** | **str** |  | [optional] 
**address_state** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_address import DtoAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAddress from a JSON string
dto_address_instance = DtoAddress.from_json(json)
# print the JSON string representation of the object
print(DtoAddress.to_json())

# convert the object into a dict
dto_address_dict = dto_address_instance.to_dict()
# create an instance of DtoAddress from a dict
dto_address_from_dict = DtoAddress.from_dict(dto_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


