# flexprice.IntegrationsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secrets_integrations_id_delete**](IntegrationsApi.md#secrets_integrations_id_delete) | **DELETE** /secrets/integrations/{id} | Delete an integration
[**secrets_integrations_linked_get**](IntegrationsApi.md#secrets_integrations_linked_get) | **GET** /secrets/integrations/linked | List linked integrations
[**secrets_integrations_provider_get**](IntegrationsApi.md#secrets_integrations_provider_get) | **GET** /secrets/integrations/{provider} | Get integration details
[**secrets_integrations_provider_post**](IntegrationsApi.md#secrets_integrations_provider_post) | **POST** /secrets/integrations/{provider} | Create or update an integration


# **secrets_integrations_id_delete**
> secrets_integrations_id_delete(id)

Delete an integration

Delete integration credentials

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
    api_instance = flexprice.IntegrationsApi(api_client)
    id = 'id_example' # str | Integration ID

    try:
        # Delete an integration
        api_instance.secrets_integrations_id_delete(id)
    except Exception as e:
        print("Exception when calling IntegrationsApi->secrets_integrations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration ID | 

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

# **secrets_integrations_linked_get**
> DtoLinkedIntegrationsResponse secrets_integrations_linked_get()

List linked integrations

Get a list of unique providers which have a valid linked integration secret

### Example


```python
import flexprice
from flexprice.models.dto_linked_integrations_response import DtoLinkedIntegrationsResponse
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
    api_instance = flexprice.IntegrationsApi(api_client)

    try:
        # List linked integrations
        api_response = api_instance.secrets_integrations_linked_get()
        print("The response of IntegrationsApi->secrets_integrations_linked_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->secrets_integrations_linked_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DtoLinkedIntegrationsResponse**](DtoLinkedIntegrationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_integrations_provider_get**
> DtoSecretResponse secrets_integrations_provider_get(provider)

Get integration details

Get details of a specific integration

### Example


```python
import flexprice
from flexprice.models.dto_secret_response import DtoSecretResponse
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
    api_instance = flexprice.IntegrationsApi(api_client)
    provider = 'provider_example' # str | Integration provider

    try:
        # Get integration details
        api_response = api_instance.secrets_integrations_provider_get(provider)
        print("The response of IntegrationsApi->secrets_integrations_provider_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->secrets_integrations_provider_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Integration provider | 

### Return type

[**DtoSecretResponse**](DtoSecretResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_integrations_provider_post**
> DtoSecretResponse secrets_integrations_provider_post(provider, request)

Create or update an integration

Create or update integration credentials

### Example


```python
import flexprice
from flexprice.models.dto_create_integration_request import DtoCreateIntegrationRequest
from flexprice.models.dto_secret_response import DtoSecretResponse
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
    api_instance = flexprice.IntegrationsApi(api_client)
    provider = 'provider_example' # str | Integration provider
    request = flexprice.DtoCreateIntegrationRequest() # DtoCreateIntegrationRequest | Integration creation request

    try:
        # Create or update an integration
        api_response = api_instance.secrets_integrations_provider_post(provider, request)
        print("The response of IntegrationsApi->secrets_integrations_provider_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->secrets_integrations_provider_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Integration provider | 
 **request** | [**DtoCreateIntegrationRequest**](DtoCreateIntegrationRequest.md)| Integration creation request | 

### Return type

[**DtoSecretResponse**](DtoSecretResponse.md)

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

