# flexprice.EventsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_bulk_post**](EventsApi.md#events_bulk_post) | **POST** /events/bulk | Bulk Ingest events
[**events_post**](EventsApi.md#events_post) | **POST** /events | Ingest event
[**events_query_post**](EventsApi.md#events_query_post) | **POST** /events/query | List raw events
[**events_usage_meter_post**](EventsApi.md#events_usage_meter_post) | **POST** /events/usage/meter | Get usage by meter
[**events_usage_post**](EventsApi.md#events_usage_post) | **POST** /events/usage | Get usage statistics


# **events_bulk_post**
> Dict[str, str] events_bulk_post(event)

Bulk Ingest events

Ingest bulk events into the system

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_bulk_ingest_event_request import DtoBulkIngestEventRequest
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
    api_instance = flexprice.EventsApi(api_client)
    event = flexprice.DtoBulkIngestEventRequest() # DtoBulkIngestEventRequest | Event data

    try:
        # Bulk Ingest events
        api_response = api_instance.events_bulk_post(event)
        print("The response of EventsApi->events_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | [**DtoBulkIngestEventRequest**](DtoBulkIngestEventRequest.md)| Event data | 

### Return type

**Dict[str, str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | message:Event accepted for processing |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_post**
> Dict[str, str] events_post(event)

Ingest event

Ingest a new event into the system

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_ingest_event_request import DtoIngestEventRequest
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
    api_instance = flexprice.EventsApi(api_client)
    event = flexprice.DtoIngestEventRequest() # DtoIngestEventRequest | Event data

    try:
        # Ingest event
        api_response = api_instance.events_post(event)
        print("The response of EventsApi->events_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | [**DtoIngestEventRequest**](DtoIngestEventRequest.md)| Event data | 

### Return type

**Dict[str, str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | message:Event accepted for processing |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_query_post**
> DtoGetEventsResponse events_query_post(request)

List raw events

Retrieve raw events with pagination and filtering

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_get_events_request import DtoGetEventsRequest
from flexprice.models.dto_get_events_response import DtoGetEventsResponse
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
    api_instance = flexprice.EventsApi(api_client)
    request = flexprice.DtoGetEventsRequest() # DtoGetEventsRequest | Request body

    try:
        # List raw events
        api_response = api_instance.events_query_post(request)
        print("The response of EventsApi->events_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoGetEventsRequest**](DtoGetEventsRequest.md)| Request body | 

### Return type

[**DtoGetEventsResponse**](DtoGetEventsResponse.md)

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

# **events_usage_meter_post**
> DtoGetUsageResponse events_usage_meter_post(request)

Get usage by meter

Retrieve aggregated usage statistics using meter configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_get_usage_by_meter_request import DtoGetUsageByMeterRequest
from flexprice.models.dto_get_usage_response import DtoGetUsageResponse
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
    api_instance = flexprice.EventsApi(api_client)
    request = flexprice.DtoGetUsageByMeterRequest() # DtoGetUsageByMeterRequest | Request body

    try:
        # Get usage by meter
        api_response = api_instance.events_usage_meter_post(request)
        print("The response of EventsApi->events_usage_meter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_usage_meter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoGetUsageByMeterRequest**](DtoGetUsageByMeterRequest.md)| Request body | 

### Return type

[**DtoGetUsageResponse**](DtoGetUsageResponse.md)

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

# **events_usage_post**
> DtoGetUsageResponse events_usage_post(request)

Get usage statistics

Retrieve aggregated usage statistics for events

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_get_usage_request import DtoGetUsageRequest
from flexprice.models.dto_get_usage_response import DtoGetUsageResponse
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
    api_instance = flexprice.EventsApi(api_client)
    request = flexprice.DtoGetUsageRequest() # DtoGetUsageRequest | Request body

    try:
        # Get usage statistics
        api_response = api_instance.events_usage_post(request)
        print("The response of EventsApi->events_usage_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_usage_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoGetUsageRequest**](DtoGetUsageRequest.md)| Request body | 

### Return type

[**DtoGetUsageResponse**](DtoGetUsageResponse.md)

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

