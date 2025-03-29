# ErrorsErrorDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **Dict[str, object]** |  | [optional] 
**internal_error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.errors_error_detail import ErrorsErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsErrorDetail from a JSON string
errors_error_detail_instance = ErrorsErrorDetail.from_json(json)
# print the JSON string representation of the object
print(ErrorsErrorDetail.to_json())

# convert the object into a dict
errors_error_detail_dict = errors_error_detail_instance.to_dict()
# create an instance of ErrorsErrorDetail from a dict
errors_error_detail_from_dict = ErrorsErrorDetail.from_dict(errors_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


