# flexprice.EntitlementsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entitlements_get**](EntitlementsApi.md#entitlements_get) | **GET** /entitlements | Get entitlements
[**entitlements_id_delete**](EntitlementsApi.md#entitlements_id_delete) | **DELETE** /entitlements/{id} | Delete an entitlement
[**entitlements_id_get**](EntitlementsApi.md#entitlements_id_get) | **GET** /entitlements/{id} | Get an entitlement by ID
[**entitlements_id_put**](EntitlementsApi.md#entitlements_id_put) | **PUT** /entitlements/{id} | Update an entitlement
[**entitlements_post**](EntitlementsApi.md#entitlements_post) | **POST** /entitlements | Create a new entitlement
[**plans_id_entitlements_get**](EntitlementsApi.md#plans_id_entitlements_get) | **GET** /plans/{id}/entitlements | Get plan entitlements


# **entitlements_get**
> DtoListEntitlementsResponse entitlements_get(end_time=end_time, expand=expand, feature_ids=feature_ids, feature_type=feature_type, is_enabled=is_enabled, limit=limit, offset=offset, order=order, plan_ids=plan_ids, sort=sort, start_time=start_time, status=status)

Get entitlements

Get entitlements with the specified filter

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_list_entitlements_response import DtoListEntitlementsResponse
from flexprice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice.Configuration(
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
with flexprice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice.EntitlementsApi(api_client)
    end_time = 'end_time_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    feature_ids = ['feature_ids_example'] # List[str] |  (optional)
    feature_type = 'feature_type_example' # str |  (optional)
    is_enabled = True # bool |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    plan_ids = ['plan_ids_example'] # List[str] | Specific filters for entitlements (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Get entitlements
        api_response = api_instance.entitlements_get(end_time=end_time, expand=expand, feature_ids=feature_ids, feature_type=feature_type, is_enabled=is_enabled, limit=limit, offset=offset, order=order, plan_ids=plan_ids, sort=sort, start_time=start_time, status=status)
        print("The response of EntitlementsApi->entitlements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **feature_ids** | [**List[str]**](str.md)|  | [optional] 
 **feature_type** | **str**|  | [optional] 
 **is_enabled** | **bool**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **plan_ids** | [**List[str]**](str.md)| Specific filters for entitlements | [optional] 
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**DtoListEntitlementsResponse**](DtoListEntitlementsResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_id_delete**
> Dict[str, object] entitlements_id_delete(id)

Delete an entitlement

Delete an entitlement

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice.Configuration(
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
with flexprice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice.EntitlementsApi(api_client)
    id = 'id_example' # str | Entitlement ID

    try:
        # Delete an entitlement
        api_response = api_instance.entitlements_id_delete(id)
        print("The response of EntitlementsApi->entitlements_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entitlement ID | 

### Return type

**Dict[str, object]**

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_id_get**
> DtoEntitlementResponse entitlements_id_get(id)

Get an entitlement by ID

Get an entitlement by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_entitlement_response import DtoEntitlementResponse
from flexprice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice.Configuration(
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
with flexprice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice.EntitlementsApi(api_client)
    id = 'id_example' # str | Entitlement ID

    try:
        # Get an entitlement by ID
        api_response = api_instance.entitlements_id_get(id)
        print("The response of EntitlementsApi->entitlements_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entitlement ID | 

### Return type

[**DtoEntitlementResponse**](DtoEntitlementResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_id_put**
> DtoEntitlementResponse entitlements_id_put(id, entitlement)

Update an entitlement

Update an entitlement with the specified configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_entitlement_response import DtoEntitlementResponse
from flexprice.models.dto_update_entitlement_request import DtoUpdateEntitlementRequest
from flexprice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice.Configuration(
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
with flexprice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice.EntitlementsApi(api_client)
    id = 'id_example' # str | Entitlement ID
    entitlement = flexprice.DtoUpdateEntitlementRequest() # DtoUpdateEntitlementRequest | Entitlement configuration

    try:
        # Update an entitlement
        api_response = api_instance.entitlements_id_put(id, entitlement)
        print("The response of EntitlementsApi->entitlements_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entitlement ID | 
 **entitlement** | [**DtoUpdateEntitlementRequest**](DtoUpdateEntitlementRequest.md)| Entitlement configuration | 

### Return type

[**DtoEntitlementResponse**](DtoEntitlementResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_post**
> DtoEntitlementResponse entitlements_post(entitlement)

Create a new entitlement

Create a new entitlement with the specified configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_create_entitlement_request import DtoCreateEntitlementRequest
from flexprice.models.dto_entitlement_response import DtoEntitlementResponse
from flexprice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice.Configuration(
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
with flexprice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice.EntitlementsApi(api_client)
    entitlement = flexprice.DtoCreateEntitlementRequest() # DtoCreateEntitlementRequest | Entitlement configuration

    try:
        # Create a new entitlement
        api_response = api_instance.entitlements_post(entitlement)
        print("The response of EntitlementsApi->entitlements_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement** | [**DtoCreateEntitlementRequest**](DtoCreateEntitlementRequest.md)| Entitlement configuration | 

### Return type

[**DtoEntitlementResponse**](DtoEntitlementResponse.md)

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

# **plans_id_entitlements_get**
> DtoPlanResponse plans_id_entitlements_get(id)

Get plan entitlements

Get all entitlements for a plan

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_plan_response import DtoPlanResponse
from flexprice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flexprice.Configuration(
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
with flexprice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flexprice.EntitlementsApi(api_client)
    id = 'id_example' # str | Plan ID

    try:
        # Get plan entitlements
        api_response = api_instance.plans_id_entitlements_get(id)
        print("The response of EntitlementsApi->plans_id_entitlements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->plans_id_entitlements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plan ID | 

### Return type

[**DtoPlanResponse**](DtoPlanResponse.md)

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

