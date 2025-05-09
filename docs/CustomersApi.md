# flexprice.CustomersApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_get**](CustomersApi.md#customers_get) | **GET** /customers | Get customers
[**customers_id_delete**](CustomersApi.md#customers_id_delete) | **DELETE** /customers/{id} | Delete a customer
[**customers_id_entitlements_get**](CustomersApi.md#customers_id_entitlements_get) | **GET** /customers/{id}/entitlements | Get customer entitlements
[**customers_id_get**](CustomersApi.md#customers_id_get) | **GET** /customers/{id} | Get a customer
[**customers_id_put**](CustomersApi.md#customers_id_put) | **PUT** /customers/{id} | Update a customer
[**customers_id_usage_get**](CustomersApi.md#customers_id_usage_get) | **GET** /customers/{id}/usage | Get customer usage summary
[**customers_lookup_lookup_key_get**](CustomersApi.md#customers_lookup_lookup_key_get) | **GET** /customers/lookup/{lookup_key} | Get a customer by lookup key
[**customers_post**](CustomersApi.md#customers_post) | **POST** /customers | Create a customer
[**customers_search_post**](CustomersApi.md#customers_search_post) | **POST** /customers/search | List customers by filter


# **customers_get**
> DtoListCustomersResponse customers_get(customer_ids=customer_ids, email=email, end_time=end_time, expand=expand, external_id=external_id, limit=limit, offset=offset, order=order, start_time=start_time, status=status)

Get customers

Get customers

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_list_customers_response import DtoListCustomersResponse
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
    api_instance = flexprice.CustomersApi(api_client)
    customer_ids = ['customer_ids_example'] # List[str] |  (optional)
    email = 'email_example' # str |  (optional)
    end_time = 'end_time_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    external_id = 'external_id_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Get customers
        api_response = api_instance.customers_get(customer_ids=customer_ids, email=email, end_time=end_time, expand=expand, external_id=external_id, limit=limit, offset=offset, order=order, start_time=start_time, status=status)
        print("The response of CustomersApi->customers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_ids** | [**List[str]**](str.md)|  | [optional] 
 **email** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **external_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**DtoListCustomersResponse**](DtoListCustomersResponse.md)

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

# **customers_id_delete**
> customers_id_delete(id)

Delete a customer

Delete a customer

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
    api_instance = flexprice.CustomersApi(api_client)
    id = 'id_example' # str | Customer ID

    try:
        # Delete a customer
        api_instance.customers_id_delete(id)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_id_entitlements_get**
> DtoCustomerEntitlementsResponse customers_id_entitlements_get(id, feature_ids=feature_ids, subscription_ids=subscription_ids)

Get customer entitlements

Get customer entitlements

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_customer_entitlements_response import DtoCustomerEntitlementsResponse
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
    api_instance = flexprice.CustomersApi(api_client)
    id = 'id_example' # str | Customer ID
    feature_ids = ['feature_ids_example'] # List[str] |  (optional)
    subscription_ids = ['subscription_ids_example'] # List[str] |  (optional)

    try:
        # Get customer entitlements
        api_response = api_instance.customers_id_entitlements_get(id, feature_ids=feature_ids, subscription_ids=subscription_ids)
        print("The response of CustomersApi->customers_id_entitlements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_id_entitlements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 
 **feature_ids** | [**List[str]**](str.md)|  | [optional] 
 **subscription_ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**DtoCustomerEntitlementsResponse**](DtoCustomerEntitlementsResponse.md)

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

# **customers_id_get**
> DtoCustomerResponse customers_id_get(id)

Get a customer

Get a customer

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_customer_response import DtoCustomerResponse
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
    api_instance = flexprice.CustomersApi(api_client)
    id = 'id_example' # str | Customer ID

    try:
        # Get a customer
        api_response = api_instance.customers_id_get(id)
        print("The response of CustomersApi->customers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 

### Return type

[**DtoCustomerResponse**](DtoCustomerResponse.md)

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

# **customers_id_put**
> DtoCustomerResponse customers_id_put(id, customer)

Update a customer

Update a customer

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_customer_response import DtoCustomerResponse
from flexprice.models.dto_update_customer_request import DtoUpdateCustomerRequest
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
    api_instance = flexprice.CustomersApi(api_client)
    id = 'id_example' # str | Customer ID
    customer = flexprice.DtoUpdateCustomerRequest() # DtoUpdateCustomerRequest | Customer

    try:
        # Update a customer
        api_response = api_instance.customers_id_put(id, customer)
        print("The response of CustomersApi->customers_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 
 **customer** | [**DtoUpdateCustomerRequest**](DtoUpdateCustomerRequest.md)| Customer | 

### Return type

[**DtoCustomerResponse**](DtoCustomerResponse.md)

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

# **customers_id_usage_get**
> DtoCustomerUsageSummaryResponse customers_id_usage_get(id, feature_ids=feature_ids, subscription_ids=subscription_ids)

Get customer usage summary

Get customer usage summary

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_customer_usage_summary_response import DtoCustomerUsageSummaryResponse
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
    api_instance = flexprice.CustomersApi(api_client)
    id = 'id_example' # str | Customer ID
    feature_ids = ['feature_ids_example'] # List[str] |  (optional)
    subscription_ids = ['subscription_ids_example'] # List[str] |  (optional)

    try:
        # Get customer usage summary
        api_response = api_instance.customers_id_usage_get(id, feature_ids=feature_ids, subscription_ids=subscription_ids)
        print("The response of CustomersApi->customers_id_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_id_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 
 **feature_ids** | [**List[str]**](str.md)|  | [optional] 
 **subscription_ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**DtoCustomerUsageSummaryResponse**](DtoCustomerUsageSummaryResponse.md)

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

# **customers_lookup_lookup_key_get**
> DtoCustomerResponse customers_lookup_lookup_key_get(lookup_key)

Get a customer by lookup key

Get a customer by lookup key (external_id)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_customer_response import DtoCustomerResponse
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
    api_instance = flexprice.CustomersApi(api_client)
    lookup_key = 'lookup_key_example' # str | Customer Lookup Key (external_id)

    try:
        # Get a customer by lookup key
        api_response = api_instance.customers_lookup_lookup_key_get(lookup_key)
        print("The response of CustomersApi->customers_lookup_lookup_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_lookup_lookup_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_key** | **str**| Customer Lookup Key (external_id) | 

### Return type

[**DtoCustomerResponse**](DtoCustomerResponse.md)

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

# **customers_post**
> DtoCustomerResponse customers_post(customer)

Create a customer

Create a customer

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_create_customer_request import DtoCreateCustomerRequest
from flexprice.models.dto_customer_response import DtoCustomerResponse
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
    api_instance = flexprice.CustomersApi(api_client)
    customer = flexprice.DtoCreateCustomerRequest() # DtoCreateCustomerRequest | Customer

    try:
        # Create a customer
        api_response = api_instance.customers_post(customer)
        print("The response of CustomersApi->customers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**DtoCreateCustomerRequest**](DtoCreateCustomerRequest.md)| Customer | 

### Return type

[**DtoCustomerResponse**](DtoCustomerResponse.md)

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

# **customers_search_post**
> DtoListCustomersResponse customers_search_post(filter)

List customers by filter

List customers by filter

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_list_customers_response import DtoListCustomersResponse
from flexprice.models.types_customer_filter import TypesCustomerFilter
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
    api_instance = flexprice.CustomersApi(api_client)
    filter = flexprice.TypesCustomerFilter() # TypesCustomerFilter | Filter

    try:
        # List customers by filter
        api_response = api_instance.customers_search_post(filter)
        print("The response of CustomersApi->customers_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**TypesCustomerFilter**](TypesCustomerFilter.md)| Filter | 

### Return type

[**DtoListCustomersResponse**](DtoListCustomersResponse.md)

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

