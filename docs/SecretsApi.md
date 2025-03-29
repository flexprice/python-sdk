# flexprice.SecretsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secrets_api_keys_get**](SecretsApi.md#secrets_api_keys_get) | **GET** /secrets/api/keys | List API keys
[**secrets_api_keys_id_delete**](SecretsApi.md#secrets_api_keys_id_delete) | **DELETE** /secrets/api/keys/{id} | Delete an API key
[**secrets_api_keys_post**](SecretsApi.md#secrets_api_keys_post) | **POST** /secrets/api/keys | Create a new API key


# **secrets_api_keys_get**
> DtoListSecretsResponse secrets_api_keys_get(limit=limit, offset=offset, status=status)

List API keys

Get a paginated list of API keys

### Example


```python
import flexprice
from flexprice.models.dto_list_secrets_response import DtoListSecretsResponse
from flexprice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with flexprice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice.SecretsApi(api_client)
    limit = 56 # int | Limit (optional)
    offset = 56 # int | Offset (optional)
    status = 'status_example' # str | Status (published/archived) (optional)

    try:
        # List API keys
        api_response = api_instance.secrets_api_keys_get(limit=limit, offset=offset, status=status)
        print("The response of SecretsApi->secrets_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->secrets_api_keys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit | [optional] 
 **offset** | **int**| Offset | [optional] 
 **status** | **str**| Status (published/archived) | [optional] 

### Return type

[**DtoListSecretsResponse**](DtoListSecretsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_api_keys_id_delete**
> secrets_api_keys_id_delete(id)

Delete an API key

Delete an API key by ID

### Example


```python
import flexprice
from flexprice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with flexprice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice.SecretsApi(api_client)
    id = 'id_example' # str | API key ID

    try:
        # Delete an API key
        api_instance.secrets_api_keys_id_delete(id)
    except Exception as e:
        print("Exception when calling SecretsApi->secrets_api_keys_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| API key ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_api_keys_post**
> DtoCreateAPIKeyResponse secrets_api_keys_post(request)

Create a new API key

Create a new API key with the specified type and permissions

### Example


```python
import flexprice
from flexprice.models.dto_create_api_key_request import DtoCreateAPIKeyRequest
from flexprice.models.dto_create_api_key_response import DtoCreateAPIKeyResponse
from flexprice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with flexprice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice.SecretsApi(api_client)
    request = flexprice.DtoCreateAPIKeyRequest() # DtoCreateAPIKeyRequest | API key creation request

    try:
        # Create a new API key
        api_response = api_instance.secrets_api_keys_post(request)
        print("The response of SecretsApi->secrets_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretsApi->secrets_api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoCreateAPIKeyRequest**](DtoCreateAPIKeyRequest.md)| API key creation request | 

### Return type

[**DtoCreateAPIKeyResponse**](DtoCreateAPIKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

