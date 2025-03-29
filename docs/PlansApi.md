# flexprice.PlansApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plans_get**](PlansApi.md#plans_get) | **GET** /plans | Get plans
[**plans_id_delete**](PlansApi.md#plans_id_delete) | **DELETE** /plans/{id} | Delete a plan
[**plans_id_get**](PlansApi.md#plans_id_get) | **GET** /plans/{id} | Get a plan
[**plans_id_put**](PlansApi.md#plans_id_put) | **PUT** /plans/{id} | Update a plan
[**plans_post**](PlansApi.md#plans_post) | **POST** /plans | Create a new plan


# **plans_get**
> DtoListPlansResponse plans_get(end_time=end_time, expand=expand, limit=limit, offset=offset, order=order, plan_ids=plan_ids, sort=sort, start_time=start_time, status=status)

Get plans

Get plans with optional filtering

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_list_plans_response import DtoListPlansResponse
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
    api_instance = flexprice.PlansApi(api_client)
    end_time = 'end_time_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    plan_ids = ['plan_ids_example'] # List[str] |  (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Get plans
        api_response = api_instance.plans_get(end_time=end_time, expand=expand, limit=limit, offset=offset, order=order, plan_ids=plan_ids, sort=sort, start_time=start_time, status=status)
        print("The response of PlansApi->plans_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_get: %s\n" % e)
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
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**DtoListPlansResponse**](DtoListPlansResponse.md)

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

# **plans_id_delete**
> Dict[str, object] plans_id_delete(id)

Delete a plan

Delete a plan by ID

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
    api_instance = flexprice.PlansApi(api_client)
    id = 'id_example' # str | Plan ID

    try:
        # Delete a plan
        api_response = api_instance.plans_id_delete(id)
        print("The response of PlansApi->plans_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plan ID | 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plans_id_get**
> DtoPlanResponse plans_id_get(id)

Get a plan

Get a plan by ID

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
    api_instance = flexprice.PlansApi(api_client)
    id = 'id_example' # str | Plan ID

    try:
        # Get a plan
        api_response = api_instance.plans_id_get(id)
        print("The response of PlansApi->plans_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_id_get: %s\n" % e)
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

# **plans_id_put**
> DtoPlanResponse plans_id_put(id, plan)

Update a plan

Update a plan by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_plan_response import DtoPlanResponse
from flexprice.models.dto_update_plan_request import DtoUpdatePlanRequest
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
    api_instance = flexprice.PlansApi(api_client)
    id = 'id_example' # str | Plan ID
    plan = flexprice.DtoUpdatePlanRequest() # DtoUpdatePlanRequest | Plan update

    try:
        # Update a plan
        api_response = api_instance.plans_id_put(id, plan)
        print("The response of PlansApi->plans_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Plan ID | 
 **plan** | [**DtoUpdatePlanRequest**](DtoUpdatePlanRequest.md)| Plan update | 

### Return type

[**DtoPlanResponse**](DtoPlanResponse.md)

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

# **plans_post**
> DtoPlanResponse plans_post(plan)

Create a new plan

Create a new plan with the specified configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_create_plan_request import DtoCreatePlanRequest
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
    api_instance = flexprice.PlansApi(api_client)
    plan = flexprice.DtoCreatePlanRequest() # DtoCreatePlanRequest | Plan configuration

    try:
        # Create a new plan
        api_response = api_instance.plans_post(plan)
        print("The response of PlansApi->plans_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | [**DtoCreatePlanRequest**](DtoCreatePlanRequest.md)| Plan configuration | 

### Return type

[**DtoPlanResponse**](DtoPlanResponse.md)

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

