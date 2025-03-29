# flexprice_client.FeaturesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**features_get**](FeaturesApi.md#features_get) | **GET** /features | List features
[**features_id_delete**](FeaturesApi.md#features_id_delete) | **DELETE** /features/{id} | Delete a feature
[**features_id_get**](FeaturesApi.md#features_id_get) | **GET** /features/{id} | Get a feature by ID
[**features_id_put**](FeaturesApi.md#features_id_put) | **PUT** /features/{id} | Update a feature
[**features_post**](FeaturesApi.md#features_post) | **POST** /features | Create a new feature


# **features_get**
> DtoListFeaturesResponse features_get(end_time=end_time, expand=expand, feature_ids=feature_ids, limit=limit, lookup_key=lookup_key, meter_ids=meter_ids, offset=offset, order=order, sort=sort, start_time=start_time, status=status)

List features

List features with optional filtering

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice_client
from flexprice_client.models.dto_list_features_response import DtoListFeaturesResponse
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
    api_instance = flexprice_client.FeaturesApi(api_client)
    end_time = 'end_time_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    feature_ids = ['feature_ids_example'] # List[str] | Feature specific filters (optional)
    limit = 56 # int |  (optional)
    lookup_key = 'lookup_key_example' # str |  (optional)
    meter_ids = ['meter_ids_example'] # List[str] |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # List features
        api_response = api_instance.features_get(end_time=end_time, expand=expand, feature_ids=feature_ids, limit=limit, lookup_key=lookup_key, meter_ids=meter_ids, offset=offset, order=order, sort=sort, start_time=start_time, status=status)
        print("The response of FeaturesApi->features_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->features_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **feature_ids** | [**List[str]**](str.md)| Feature specific filters | [optional] 
 **limit** | **int**|  | [optional] 
 **lookup_key** | **str**|  | [optional] 
 **meter_ids** | [**List[str]**](str.md)|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**DtoListFeaturesResponse**](DtoListFeaturesResponse.md)

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

# **features_id_delete**
> Dict[str, object] features_id_delete(id)

Delete a feature

Delete a feature by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice_client
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
    api_instance = flexprice_client.FeaturesApi(api_client)
    id = 'id_example' # str | Feature ID

    try:
        # Delete a feature
        api_response = api_instance.features_id_delete(id)
        print("The response of FeaturesApi->features_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->features_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Feature ID | 

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

# **features_id_get**
> DtoFeatureResponse features_id_get(id)

Get a feature by ID

Get a feature by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice_client
from flexprice_client.models.dto_feature_response import DtoFeatureResponse
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
    api_instance = flexprice_client.FeaturesApi(api_client)
    id = 'id_example' # str | Feature ID

    try:
        # Get a feature by ID
        api_response = api_instance.features_id_get(id)
        print("The response of FeaturesApi->features_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->features_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Feature ID | 

### Return type

[**DtoFeatureResponse**](DtoFeatureResponse.md)

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

# **features_id_put**
> DtoFeatureResponse features_id_put(id, feature)

Update a feature

Update a feature by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice_client
from flexprice_client.models.dto_feature_response import DtoFeatureResponse
from flexprice_client.models.dto_update_feature_request import DtoUpdateFeatureRequest
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
    api_instance = flexprice_client.FeaturesApi(api_client)
    id = 'id_example' # str | Feature ID
    feature = flexprice_client.DtoUpdateFeatureRequest() # DtoUpdateFeatureRequest | Feature update data

    try:
        # Update a feature
        api_response = api_instance.features_id_put(id, feature)
        print("The response of FeaturesApi->features_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->features_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Feature ID | 
 **feature** | [**DtoUpdateFeatureRequest**](DtoUpdateFeatureRequest.md)| Feature update data | 

### Return type

[**DtoFeatureResponse**](DtoFeatureResponse.md)

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

# **features_post**
> DtoFeatureResponse features_post(feature)

Create a new feature

Create a new feature

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice_client
from flexprice_client.models.dto_create_feature_request import DtoCreateFeatureRequest
from flexprice_client.models.dto_feature_response import DtoFeatureResponse
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
    api_instance = flexprice_client.FeaturesApi(api_client)
    feature = flexprice_client.DtoCreateFeatureRequest() # DtoCreateFeatureRequest | Feature to create

    try:
        # Create a new feature
        api_response = api_instance.features_post(feature)
        print("The response of FeaturesApi->features_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeaturesApi->features_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | [**DtoCreateFeatureRequest**](DtoCreateFeatureRequest.md)| Feature to create | 

### Return type

[**DtoFeatureResponse**](DtoFeatureResponse.md)

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

