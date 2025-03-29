# flexprice_client.TenantsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenant_billing_get**](TenantsApi.md#tenant_billing_get) | **GET** /tenant/billing | Get billing usage for the current tenant
[**tenants_id_get**](TenantsApi.md#tenants_id_get) | **GET** /tenants/{id} | Get tenant by ID
[**tenants_post**](TenantsApi.md#tenants_post) | **POST** /tenants | Create a new tenant
[**tenants_update_put**](TenantsApi.md#tenants_update_put) | **PUT** /tenants/update | Update a tenant


# **tenant_billing_get**
> DtoTenantBillingUsage tenant_billing_get()

Get billing usage for the current tenant

Get the subscription and usage details for the current tenant

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice_client
from flexprice_client.models.dto_tenant_billing_usage import DtoTenantBillingUsage
from flexprice_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with flexprice_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice_client.TenantsApi(api_client)

    try:
        # Get billing usage for the current tenant
        api_response = api_instance.tenant_billing_get()
        print("The response of TenantsApi->tenant_billing_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenant_billing_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DtoTenantBillingUsage**](DtoTenantBillingUsage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_id_get**
> DtoTenantResponse tenants_id_get(id)

Get tenant by ID

Get tenant by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice_client
from flexprice_client.models.dto_tenant_response import DtoTenantResponse
from flexprice_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with flexprice_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice_client.TenantsApi(api_client)
    id = 'id_example' # str | Tenant ID

    try:
        # Get tenant by ID
        api_response = api_instance.tenants_id_get(id)
        print("The response of TenantsApi->tenants_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tenant ID | 

### Return type

[**DtoTenantResponse**](DtoTenantResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **tenants_post**
> DtoTenantResponse tenants_post(request)

Create a new tenant

Create a new tenant

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice_client
from flexprice_client.models.dto_create_tenant_request import DtoCreateTenantRequest
from flexprice_client.models.dto_tenant_response import DtoTenantResponse
from flexprice_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with flexprice_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice_client.TenantsApi(api_client)
    request = flexprice_client.DtoCreateTenantRequest() # DtoCreateTenantRequest | Create tenant request

    try:
        # Create a new tenant
        api_response = api_instance.tenants_post(request)
        print("The response of TenantsApi->tenants_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoCreateTenantRequest**](DtoCreateTenantRequest.md)| Create tenant request | 

### Return type

[**DtoTenantResponse**](DtoTenantResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **tenants_update_put**
> DtoTenantResponse tenants_update_put(request)

Update a tenant

Update a tenant's details including name and billing information

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice_client
from flexprice_client.models.dto_tenant_response import DtoTenantResponse
from flexprice_client.models.dto_update_tenant_request import DtoUpdateTenantRequest
from flexprice_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with flexprice_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice_client.TenantsApi(api_client)
    request = flexprice_client.DtoUpdateTenantRequest() # DtoUpdateTenantRequest | Update tenant request

    try:
        # Update a tenant
        api_response = api_instance.tenants_update_put(request)
        print("The response of TenantsApi->tenants_update_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->tenants_update_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoUpdateTenantRequest**](DtoUpdateTenantRequest.md)| Update tenant request | 

### Return type

[**DtoTenantResponse**](DtoTenantResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

