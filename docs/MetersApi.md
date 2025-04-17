# flexprice.MetersApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meters_get**](MetersApi.md#meters_get) | **GET** /meters | List meters
[**meters_id_delete**](MetersApi.md#meters_id_delete) | **DELETE** /meters/{id} | Delete meter
[**meters_id_disable_post**](MetersApi.md#meters_id_disable_post) | **POST** /meters/{id}/disable | Disable meter [TODO: Deprecate]
[**meters_id_get**](MetersApi.md#meters_id_get) | **GET** /meters/{id} | Get meter
[**meters_id_put**](MetersApi.md#meters_id_put) | **PUT** /meters/{id} | Update meter
[**meters_post**](MetersApi.md#meters_post) | **POST** /meters | Create meter


# **meters_get**
> DtoListMetersResponse meters_get(end_time=end_time, event_name=event_name, expand=expand, limit=limit, meter_ids=meter_ids, offset=offset, order=order, sort=sort, start_time=start_time, status=status)

List meters

Get all meters

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_list_meters_response import DtoListMetersResponse
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
    api_instance = flexprice.MetersApi(api_client)
    end_time = 'end_time_example' # str |  (optional)
    event_name = 'event_name_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    limit = 56 # int |  (optional)
    meter_ids = ['meter_ids_example'] # List[str] |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # List meters
        api_response = api_instance.meters_get(end_time=end_time, event_name=event_name, expand=expand, limit=limit, meter_ids=meter_ids, offset=offset, order=order, sort=sort, start_time=start_time, status=status)
        print("The response of MetersApi->meters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **str**|  | [optional] 
 **event_name** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **meter_ids** | [**List[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**DtoListMetersResponse**](DtoListMetersResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meters_id_delete**
> Dict[str, str] meters_id_delete(id)

Delete meter

Delete an existing meter

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
    api_instance = flexprice.MetersApi(api_client)
    id = 'id_example' # str | Meter ID

    try:
        # Delete meter
        api_response = api_instance.meters_id_delete(id)
        print("The response of MetersApi->meters_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Meter ID | 

### Return type

**Dict[str, str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | message:Meter deleted successfully |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meters_id_disable_post**
> Dict[str, str] meters_id_disable_post(id)

Disable meter [TODO: Deprecate]

Disable an existing meter

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
    api_instance = flexprice.MetersApi(api_client)
    id = 'id_example' # str | Meter ID

    try:
        # Disable meter [TODO: Deprecate]
        api_response = api_instance.meters_id_disable_post(id)
        print("The response of MetersApi->meters_id_disable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_id_disable_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Meter ID | 

### Return type

**Dict[str, str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | message:Meter disabled successfully |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meters_id_get**
> DtoMeterResponse meters_id_get(id)

Get meter

Get a specific meter by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_meter_response import DtoMeterResponse
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
    api_instance = flexprice.MetersApi(api_client)
    id = 'id_example' # str | Meter ID

    try:
        # Get meter
        api_response = api_instance.meters_id_get(id)
        print("The response of MetersApi->meters_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Meter ID | 

### Return type

[**DtoMeterResponse**](DtoMeterResponse.md)

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

# **meters_id_put**
> DtoMeterResponse meters_id_put(id, meter)

Update meter

Update an existing meter

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_meter_response import DtoMeterResponse
from flexprice.models.dto_update_meter_request import DtoUpdateMeterRequest
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
    api_instance = flexprice.MetersApi(api_client)
    id = 'id_example' # str | Meter ID
    meter = flexprice.DtoUpdateMeterRequest() # DtoUpdateMeterRequest | Meter configuration

    try:
        # Update meter
        api_response = api_instance.meters_id_put(id, meter)
        print("The response of MetersApi->meters_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Meter ID | 
 **meter** | [**DtoUpdateMeterRequest**](DtoUpdateMeterRequest.md)| Meter configuration | 

### Return type

[**DtoMeterResponse**](DtoMeterResponse.md)

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

# **meters_post**
> DtoMeterResponse meters_post(meter)

Create meter

Create a new meter with the specified configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_create_meter_request import DtoCreateMeterRequest
from flexprice.models.dto_meter_response import DtoMeterResponse
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
    api_instance = flexprice.MetersApi(api_client)
    meter = flexprice.DtoCreateMeterRequest() # DtoCreateMeterRequest | Meter configuration

    try:
        # Create meter
        api_response = api_instance.meters_post(meter)
        print("The response of MetersApi->meters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter** | [**DtoCreateMeterRequest**](DtoCreateMeterRequest.md)| Meter configuration | 

### Return type

[**DtoMeterResponse**](DtoMeterResponse.md)

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

