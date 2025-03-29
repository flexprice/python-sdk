# flexprice.PaymentsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_get**](PaymentsApi.md#payments_get) | **GET** /payments | List payments
[**payments_id_delete**](PaymentsApi.md#payments_id_delete) | **DELETE** /payments/{id} | Delete a payment
[**payments_id_get**](PaymentsApi.md#payments_id_get) | **GET** /payments/{id} | Get a payment by ID
[**payments_id_process_post**](PaymentsApi.md#payments_id_process_post) | **POST** /payments/{id}/process | Process a payment
[**payments_id_put**](PaymentsApi.md#payments_id_put) | **PUT** /payments/{id} | Update a payment
[**payments_post**](PaymentsApi.md#payments_post) | **POST** /payments | Create a new payment


# **payments_get**
> DtoListPaymentsResponse payments_get(currency=currency, destination_id=destination_id, destination_type=destination_type, end_time=end_time, expand=expand, limit=limit, offset=offset, order=order, payment_gateway=payment_gateway, payment_ids=payment_ids, payment_method_type=payment_method_type, payment_status=payment_status, sort=sort, start_time=start_time, status=status)

List payments

List payments with the specified filter

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_list_payments_response import DtoListPaymentsResponse
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
    api_instance = flexprice.PaymentsApi(api_client)
    currency = 'currency_example' # str |  (optional)
    destination_id = 'destination_id_example' # str |  (optional)
    destination_type = 'destination_type_example' # str |  (optional)
    end_time = 'end_time_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    payment_gateway = 'payment_gateway_example' # str |  (optional)
    payment_ids = ['payment_ids_example'] # List[str] |  (optional)
    payment_method_type = 'payment_method_type_example' # str |  (optional)
    payment_status = 'payment_status_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # List payments
        api_response = api_instance.payments_get(currency=currency, destination_id=destination_id, destination_type=destination_type, end_time=end_time, expand=expand, limit=limit, offset=offset, order=order, payment_gateway=payment_gateway, payment_ids=payment_ids, payment_method_type=payment_method_type, payment_status=payment_status, sort=sort, start_time=start_time, status=status)
        print("The response of PaymentsApi->payments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | [optional] 
 **destination_id** | **str**|  | [optional] 
 **destination_type** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **payment_gateway** | **str**|  | [optional] 
 **payment_ids** | [**List[str]**](str.md)|  | [optional] 
 **payment_method_type** | **str**|  | [optional] 
 **payment_status** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**DtoListPaymentsResponse**](DtoListPaymentsResponse.md)

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

# **payments_id_delete**
> Dict[str, object] payments_id_delete(id)

Delete a payment

Delete a payment

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
    api_instance = flexprice.PaymentsApi(api_client)
    id = 'id_example' # str | Payment ID

    try:
        # Delete a payment
        api_response = api_instance.payments_id_delete(id)
        print("The response of PaymentsApi->payments_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment ID | 

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

# **payments_id_get**
> DtoPaymentResponse payments_id_get(id)

Get a payment by ID

Get a payment by ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_payment_response import DtoPaymentResponse
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
    api_instance = flexprice.PaymentsApi(api_client)
    id = 'id_example' # str | Payment ID

    try:
        # Get a payment by ID
        api_response = api_instance.payments_id_get(id)
        print("The response of PaymentsApi->payments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment ID | 

### Return type

[**DtoPaymentResponse**](DtoPaymentResponse.md)

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

# **payments_id_process_post**
> DtoPaymentResponse payments_id_process_post(id)

Process a payment

Process a payment

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_payment_response import DtoPaymentResponse
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
    api_instance = flexprice.PaymentsApi(api_client)
    id = 'id_example' # str | Payment ID

    try:
        # Process a payment
        api_response = api_instance.payments_id_process_post(id)
        print("The response of PaymentsApi->payments_id_process_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_id_process_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment ID | 

### Return type

[**DtoPaymentResponse**](DtoPaymentResponse.md)

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

# **payments_id_put**
> DtoPaymentResponse payments_id_put(id, payment)

Update a payment

Update a payment with the specified configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_payment_response import DtoPaymentResponse
from flexprice.models.dto_update_payment_request import DtoUpdatePaymentRequest
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
    api_instance = flexprice.PaymentsApi(api_client)
    id = 'id_example' # str | Payment ID
    payment = flexprice.DtoUpdatePaymentRequest() # DtoUpdatePaymentRequest | Payment configuration

    try:
        # Update a payment
        api_response = api_instance.payments_id_put(id, payment)
        print("The response of PaymentsApi->payments_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Payment ID | 
 **payment** | [**DtoUpdatePaymentRequest**](DtoUpdatePaymentRequest.md)| Payment configuration | 

### Return type

[**DtoPaymentResponse**](DtoPaymentResponse.md)

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

# **payments_post**
> DtoPaymentResponse payments_post(payment)

Create a new payment

Create a new payment with the specified configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_create_payment_request import DtoCreatePaymentRequest
from flexprice.models.dto_payment_response import DtoPaymentResponse
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
    api_instance = flexprice.PaymentsApi(api_client)
    payment = flexprice.DtoCreatePaymentRequest() # DtoCreatePaymentRequest | Payment configuration

    try:
        # Create a new payment
        api_response = api_instance.payments_post(payment)
        print("The response of PaymentsApi->payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment** | [**DtoCreatePaymentRequest**](DtoCreatePaymentRequest.md)| Payment configuration | 

### Return type

[**DtoPaymentResponse**](DtoPaymentResponse.md)

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

