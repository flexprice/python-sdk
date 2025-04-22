# flexprice.SubscriptionsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_get**](SubscriptionsApi.md#subscriptions_get) | **GET** /subscriptions | List subscriptions
[**subscriptions_id_cancel_post**](SubscriptionsApi.md#subscriptions_id_cancel_post) | **POST** /subscriptions/{id}/cancel | Cancel subscription
[**subscriptions_id_get**](SubscriptionsApi.md#subscriptions_id_get) | **GET** /subscriptions/{id} | Get subscription
[**subscriptions_id_pause_post**](SubscriptionsApi.md#subscriptions_id_pause_post) | **POST** /subscriptions/{id}/pause | Pause a subscription
[**subscriptions_id_pauses_get**](SubscriptionsApi.md#subscriptions_id_pauses_get) | **GET** /subscriptions/{id}/pauses | List all pauses for a subscription
[**subscriptions_id_resume_post**](SubscriptionsApi.md#subscriptions_id_resume_post) | **POST** /subscriptions/{id}/resume | Resume a paused subscription
[**subscriptions_post**](SubscriptionsApi.md#subscriptions_post) | **POST** /subscriptions | Create subscription
[**subscriptions_usage_post**](SubscriptionsApi.md#subscriptions_usage_post) | **POST** /subscriptions/usage | Get usage by subscription


# **subscriptions_get**
> DtoListSubscriptionsResponse subscriptions_get(active_at=active_at, billing_cadence=billing_cadence, billing_period=billing_period, customer_id=customer_id, end_time=end_time, expand=expand, limit=limit, offset=offset, order=order, plan_id=plan_id, sort=sort, start_time=start_time, status=status, subscription_status=subscription_status, with_line_items=with_line_items)

List subscriptions

Get subscriptions with optional filtering

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_list_subscriptions_response import DtoListSubscriptionsResponse
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
    api_instance = flexprice.SubscriptionsApi(api_client)
    active_at = 'active_at_example' # str | ActiveAt filters subscriptions that are active at the given time (optional)
    billing_cadence = ['billing_cadence_example'] # List[str] | BillingCadence filters by billing cadence (optional)
    billing_period = ['billing_period_example'] # List[str] | BillingPeriod filters by billing period (optional)
    customer_id = 'customer_id_example' # str | CustomerID filters by customer ID (optional)
    end_time = 'end_time_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    plan_id = 'plan_id_example' # str | PlanID filters by plan ID (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    subscription_status = ['subscription_status_example'] # List[str] | SubscriptionStatus filters by subscription status (optional)
    with_line_items = True # bool | WithLineItems includes line items in the response (optional)

    try:
        # List subscriptions
        api_response = api_instance.subscriptions_get(active_at=active_at, billing_cadence=billing_cadence, billing_period=billing_period, customer_id=customer_id, end_time=end_time, expand=expand, limit=limit, offset=offset, order=order, plan_id=plan_id, sort=sort, start_time=start_time, status=status, subscription_status=subscription_status, with_line_items=with_line_items)
        print("The response of SubscriptionsApi->subscriptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active_at** | **str**| ActiveAt filters subscriptions that are active at the given time | [optional] 
 **billing_cadence** | [**List[str]**](str.md)| BillingCadence filters by billing cadence | [optional] 
 **billing_period** | [**List[str]**](str.md)| BillingPeriod filters by billing period | [optional] 
 **customer_id** | **str**| CustomerID filters by customer ID | [optional] 
 **end_time** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **plan_id** | **str**| PlanID filters by plan ID | [optional] 
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **subscription_status** | [**List[str]**](str.md)| SubscriptionStatus filters by subscription status | [optional] 
 **with_line_items** | **bool**| WithLineItems includes line items in the response | [optional] 

### Return type

[**DtoListSubscriptionsResponse**](DtoListSubscriptionsResponse.md)

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

# **subscriptions_id_cancel_post**
> Dict[str, object] subscriptions_id_cancel_post(id, cancel_at_period_end=cancel_at_period_end)

Cancel subscription

Cancel a subscription

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
    api_instance = flexprice.SubscriptionsApi(api_client)
    id = 'id_example' # str | Subscription ID
    cancel_at_period_end = True # bool | Cancel at period end (optional)

    try:
        # Cancel subscription
        api_response = api_instance.subscriptions_id_cancel_post(id, cancel_at_period_end=cancel_at_period_end)
        print("The response of SubscriptionsApi->subscriptions_id_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_id_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription ID | 
 **cancel_at_period_end** | **bool**| Cancel at period end | [optional] 

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

# **subscriptions_id_get**
> DtoSubscriptionResponse subscriptions_id_get(id)

Get subscription

Get a subscription by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_subscription_response import DtoSubscriptionResponse
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
    api_instance = flexprice.SubscriptionsApi(api_client)
    id = 'id_example' # str | Subscription ID

    try:
        # Get subscription
        api_response = api_instance.subscriptions_id_get(id)
        print("The response of SubscriptionsApi->subscriptions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription ID | 

### Return type

[**DtoSubscriptionResponse**](DtoSubscriptionResponse.md)

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

# **subscriptions_id_pause_post**
> DtoSubscriptionPauseResponse subscriptions_id_pause_post(id, request)

Pause a subscription

Pause a subscription with the specified parameters

### Example


```python
import flexprice
from flexprice.models.dto_pause_subscription_request import DtoPauseSubscriptionRequest
from flexprice.models.dto_subscription_pause_response import DtoSubscriptionPauseResponse
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
    api_instance = flexprice.SubscriptionsApi(api_client)
    id = 'id_example' # str | Subscription ID
    request = flexprice.DtoPauseSubscriptionRequest() # DtoPauseSubscriptionRequest | Pause subscription request

    try:
        # Pause a subscription
        api_response = api_instance.subscriptions_id_pause_post(id, request)
        print("The response of SubscriptionsApi->subscriptions_id_pause_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_id_pause_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription ID | 
 **request** | [**DtoPauseSubscriptionRequest**](DtoPauseSubscriptionRequest.md)| Pause subscription request | 

### Return type

[**DtoSubscriptionPauseResponse**](DtoSubscriptionPauseResponse.md)

### Authorization

No authorization required

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

# **subscriptions_id_pauses_get**
> List[DtoListSubscriptionPausesResponse] subscriptions_id_pauses_get(id)

List all pauses for a subscription

List all pauses for a subscription

### Example


```python
import flexprice
from flexprice.models.dto_list_subscription_pauses_response import DtoListSubscriptionPausesResponse
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
    api_instance = flexprice.SubscriptionsApi(api_client)
    id = 'id_example' # str | Subscription ID

    try:
        # List all pauses for a subscription
        api_response = api_instance.subscriptions_id_pauses_get(id)
        print("The response of SubscriptionsApi->subscriptions_id_pauses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_id_pauses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription ID | 

### Return type

[**List[DtoListSubscriptionPausesResponse]**](DtoListSubscriptionPausesResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_id_resume_post**
> DtoSubscriptionPauseResponse subscriptions_id_resume_post(id, request)

Resume a paused subscription

Resume a paused subscription with the specified parameters

### Example


```python
import flexprice
from flexprice.models.dto_resume_subscription_request import DtoResumeSubscriptionRequest
from flexprice.models.dto_subscription_pause_response import DtoSubscriptionPauseResponse
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
    api_instance = flexprice.SubscriptionsApi(api_client)
    id = 'id_example' # str | Subscription ID
    request = flexprice.DtoResumeSubscriptionRequest() # DtoResumeSubscriptionRequest | Resume subscription request

    try:
        # Resume a paused subscription
        api_response = api_instance.subscriptions_id_resume_post(id, request)
        print("The response of SubscriptionsApi->subscriptions_id_resume_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_id_resume_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription ID | 
 **request** | [**DtoResumeSubscriptionRequest**](DtoResumeSubscriptionRequest.md)| Resume subscription request | 

### Return type

[**DtoSubscriptionPauseResponse**](DtoSubscriptionPauseResponse.md)

### Authorization

No authorization required

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

# **subscriptions_post**
> DtoSubscriptionResponse subscriptions_post(subscription)

Create subscription

Create a new subscription

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_create_subscription_request import DtoCreateSubscriptionRequest
from flexprice.models.dto_subscription_response import DtoSubscriptionResponse
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
    api_instance = flexprice.SubscriptionsApi(api_client)
    subscription = flexprice.DtoCreateSubscriptionRequest() # DtoCreateSubscriptionRequest | Subscription Request

    try:
        # Create subscription
        api_response = api_instance.subscriptions_post(subscription)
        print("The response of SubscriptionsApi->subscriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**DtoCreateSubscriptionRequest**](DtoCreateSubscriptionRequest.md)| Subscription Request | 

### Return type

[**DtoSubscriptionResponse**](DtoSubscriptionResponse.md)

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

# **subscriptions_usage_post**
> DtoGetUsageBySubscriptionResponse subscriptions_usage_post(request)

Get usage by subscription

Get usage for a subscription

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_get_usage_by_subscription_request import DtoGetUsageBySubscriptionRequest
from flexprice.models.dto_get_usage_by_subscription_response import DtoGetUsageBySubscriptionResponse
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
    api_instance = flexprice.SubscriptionsApi(api_client)
    request = flexprice.DtoGetUsageBySubscriptionRequest() # DtoGetUsageBySubscriptionRequest | Usage request

    try:
        # Get usage by subscription
        api_response = api_instance.subscriptions_usage_post(request)
        print("The response of SubscriptionsApi->subscriptions_usage_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_usage_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoGetUsageBySubscriptionRequest**](DtoGetUsageBySubscriptionRequest.md)| Usage request | 

### Return type

[**DtoGetUsageBySubscriptionResponse**](DtoGetUsageBySubscriptionResponse.md)

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

