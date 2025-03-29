# flexprice.PricesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prices_get**](PricesApi.md#prices_get) | **GET** /prices | Get prices
[**prices_id_delete**](PricesApi.md#prices_id_delete) | **DELETE** /prices/{id} | Delete a price
[**prices_id_get**](PricesApi.md#prices_id_get) | **GET** /prices/{id} | Get a price by ID
[**prices_id_put**](PricesApi.md#prices_id_put) | **PUT** /prices/{id} | Update a price
[**prices_post**](PricesApi.md#prices_post) | **POST** /prices | Create a new price


# **prices_get**
> DtoListPricesResponse prices_get(end_time=end_time, expand=expand, limit=limit, offset=offset, order=order, plan_ids=plan_ids, price_ids=price_ids, sort=sort, start_time=start_time, status=status)

Get prices

Get prices with the specified filter

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_list_prices_response import DtoListPricesResponse
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
    api_instance = flexprice.PricesApi(api_client)
    end_time = 'end_time_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    plan_ids = ['plan_ids_example'] # List[str] |  (optional)
    price_ids = ['price_ids_example'] # List[str] |  (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Get prices
        api_response = api_instance.prices_get(end_time=end_time, expand=expand, limit=limit, offset=offset, order=order, plan_ids=plan_ids, price_ids=price_ids, sort=sort, start_time=start_time, status=status)
        print("The response of PricesApi->prices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **plan_ids** | [**List[str]**](str.md)|  | [optional] 
 **price_ids** | [**List[str]**](str.md)|  | [optional] 
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**DtoListPricesResponse**](DtoListPricesResponse.md)

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

# **prices_id_delete**
> Dict[str, object] prices_id_delete(id)

Delete a price

Delete a price

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
    api_instance = flexprice.PricesApi(api_client)
    id = 'id_example' # str | Price ID

    try:
        # Delete a price
        api_response = api_instance.prices_id_delete(id)
        print("The response of PricesApi->prices_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price ID | 

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

# **prices_id_get**
> DtoPriceResponse prices_id_get(id)

Get a price by ID

Get a price by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_price_response import DtoPriceResponse
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
    api_instance = flexprice.PricesApi(api_client)
    id = 'id_example' # str | Price ID

    try:
        # Get a price by ID
        api_response = api_instance.prices_id_get(id)
        print("The response of PricesApi->prices_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price ID | 

### Return type

[**DtoPriceResponse**](DtoPriceResponse.md)

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

# **prices_id_put**
> DtoPriceResponse prices_id_put(id, price)

Update a price

Update a price with the specified configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_price_response import DtoPriceResponse
from flexprice.models.dto_update_price_request import DtoUpdatePriceRequest
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
    api_instance = flexprice.PricesApi(api_client)
    id = 'id_example' # str | Price ID
    price = flexprice.DtoUpdatePriceRequest() # DtoUpdatePriceRequest | Price configuration

    try:
        # Update a price
        api_response = api_instance.prices_id_put(id, price)
        print("The response of PricesApi->prices_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Price ID | 
 **price** | [**DtoUpdatePriceRequest**](DtoUpdatePriceRequest.md)| Price configuration | 

### Return type

[**DtoPriceResponse**](DtoPriceResponse.md)

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

# **prices_post**
> DtoPriceResponse prices_post(price)

Create a new price

Create a new price with the specified configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_create_price_request import DtoCreatePriceRequest
from flexprice.models.dto_price_response import DtoPriceResponse
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
    api_instance = flexprice.PricesApi(api_client)
    price = flexprice.DtoCreatePriceRequest() # DtoCreatePriceRequest | Price configuration

    try:
        # Create a new price
        api_response = api_instance.prices_post(price)
        print("The response of PricesApi->prices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price** | [**DtoCreatePriceRequest**](DtoCreatePriceRequest.md)| Price configuration | 

### Return type

[**DtoPriceResponse**](DtoPriceResponse.md)

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

