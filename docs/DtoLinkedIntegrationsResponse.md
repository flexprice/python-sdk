# DtoLinkedIntegrationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | **List[str]** |  | [optional] 

## Example

```python
from flexprice.models.dto_linked_integrations_response import DtoLinkedIntegrationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoLinkedIntegrationsResponse from a JSON string
dto_linked_integrations_response_instance = DtoLinkedIntegrationsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoLinkedIntegrationsResponse.to_json())

# convert the object into a dict
dto_linked_integrations_response_dict = dto_linked_integrations_response_instance.to_dict()
# create an instance of DtoLinkedIntegrationsResponse from a dict
dto_linked_integrations_response_from_dict = DtoLinkedIntegrationsResponse.from_dict(dto_linked_integrations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


