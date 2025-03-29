# DtoListPricesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoPriceResponse]**](DtoPriceResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_list_prices_response import DtoListPricesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListPricesResponse from a JSON string
dto_list_prices_response_instance = DtoListPricesResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListPricesResponse.to_json())

# convert the object into a dict
dto_list_prices_response_dict = dto_list_prices_response_instance.to_dict()
# create an instance of DtoListPricesResponse from a dict
dto_list_prices_response_from_dict = DtoListPricesResponse.from_dict(dto_list_prices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


