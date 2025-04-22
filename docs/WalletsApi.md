# flexprice.WalletsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_id_wallets_get**](WalletsApi.md#customers_id_wallets_get) | **GET** /customers/{id}/wallets | Get wallets by customer ID
[**customers_wallets_get**](WalletsApi.md#customers_wallets_get) | **GET** /customers/wallets | Get Customer Wallets
[**wallets_id_balance_real_time_get**](WalletsApi.md#wallets_id_balance_real_time_get) | **GET** /wallets/{id}/balance/real-time | Get wallet balance
[**wallets_id_get**](WalletsApi.md#wallets_id_get) | **GET** /wallets/{id} | Get wallet by ID
[**wallets_id_put**](WalletsApi.md#wallets_id_put) | **PUT** /wallets/{id} | Update a wallet
[**wallets_id_terminate_post**](WalletsApi.md#wallets_id_terminate_post) | **POST** /wallets/{id}/terminate | Terminate a wallet
[**wallets_id_top_up_post**](WalletsApi.md#wallets_id_top_up_post) | **POST** /wallets/{id}/top-up | Top up wallet
[**wallets_id_transactions_get**](WalletsApi.md#wallets_id_transactions_get) | **GET** /wallets/{id}/transactions | Get wallet transactions
[**wallets_post**](WalletsApi.md#wallets_post) | **POST** /wallets | Create a new wallet


# **customers_id_wallets_get**
> List[DtoWalletResponse] customers_id_wallets_get(id)

Get wallets by customer ID

Get all wallets for a customer

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_wallet_response import DtoWalletResponse
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
    api_instance = flexprice.WalletsApi(api_client)
    id = 'id_example' # str | Customer ID

    try:
        # Get wallets by customer ID
        api_response = api_instance.customers_id_wallets_get(id)
        print("The response of WalletsApi->customers_id_wallets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->customers_id_wallets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 

### Return type

[**List[DtoWalletResponse]**](DtoWalletResponse.md)

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

# **customers_wallets_get**
> List[DtoWalletResponse] customers_wallets_get(id=id, include_real_time_balance=include_real_time_balance, lookup_key=lookup_key)

Get Customer Wallets

Get all wallets for a customer by lookup key or id

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_wallet_response import DtoWalletResponse
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
    api_instance = flexprice.WalletsApi(api_client)
    id = 'id_example' # str |  (optional)
    include_real_time_balance = False # bool |  (optional) (default to False)
    lookup_key = 'lookup_key_example' # str |  (optional)

    try:
        # Get Customer Wallets
        api_response = api_instance.customers_wallets_get(id=id, include_real_time_balance=include_real_time_balance, lookup_key=lookup_key)
        print("The response of WalletsApi->customers_wallets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->customers_wallets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **include_real_time_balance** | **bool**|  | [optional] [default to False]
 **lookup_key** | **str**|  | [optional] 

### Return type

[**List[DtoWalletResponse]**](DtoWalletResponse.md)

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

# **wallets_id_balance_real_time_get**
> DtoWalletBalanceResponse wallets_id_balance_real_time_get(id)

Get wallet balance

Get real-time balance of a wallet

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_wallet_balance_response import DtoWalletBalanceResponse
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
    api_instance = flexprice.WalletsApi(api_client)
    id = 'id_example' # str | Wallet ID

    try:
        # Get wallet balance
        api_response = api_instance.wallets_id_balance_real_time_get(id)
        print("The response of WalletsApi->wallets_id_balance_real_time_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->wallets_id_balance_real_time_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet ID | 

### Return type

[**DtoWalletBalanceResponse**](DtoWalletBalanceResponse.md)

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

# **wallets_id_get**
> DtoWalletResponse wallets_id_get(id)

Get wallet by ID

Get a wallet by its ID

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_wallet_response import DtoWalletResponse
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
    api_instance = flexprice.WalletsApi(api_client)
    id = 'id_example' # str | Wallet ID

    try:
        # Get wallet by ID
        api_response = api_instance.wallets_id_get(id)
        print("The response of WalletsApi->wallets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->wallets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet ID | 

### Return type

[**DtoWalletResponse**](DtoWalletResponse.md)

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

# **wallets_id_put**
> DtoWalletResponse wallets_id_put(id, request)

Update a wallet

Update a wallet's details including auto top-up configuration

### Example


```python
import flexprice
from flexprice.models.dto_update_wallet_request import DtoUpdateWalletRequest
from flexprice.models.dto_wallet_response import DtoWalletResponse
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
    api_instance = flexprice.WalletsApi(api_client)
    id = 'id_example' # str | Wallet ID
    request = flexprice.DtoUpdateWalletRequest() # DtoUpdateWalletRequest | Update wallet request

    try:
        # Update a wallet
        api_response = api_instance.wallets_id_put(id, request)
        print("The response of WalletsApi->wallets_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->wallets_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet ID | 
 **request** | [**DtoUpdateWalletRequest**](DtoUpdateWalletRequest.md)| Update wallet request | 

### Return type

[**DtoWalletResponse**](DtoWalletResponse.md)

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

# **wallets_id_terminate_post**
> DtoWalletResponse wallets_id_terminate_post(id)

Terminate a wallet

Terminates a wallet by closing it and debiting remaining balance

### Example


```python
import flexprice
from flexprice.models.dto_wallet_response import DtoWalletResponse
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
    api_instance = flexprice.WalletsApi(api_client)
    id = 'id_example' # str | Wallet ID

    try:
        # Terminate a wallet
        api_response = api_instance.wallets_id_terminate_post(id)
        print("The response of WalletsApi->wallets_id_terminate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->wallets_id_terminate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet ID | 

### Return type

[**DtoWalletResponse**](DtoWalletResponse.md)

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

# **wallets_id_top_up_post**
> DtoWalletResponse wallets_id_top_up_post(id, request)

Top up wallet

Add credits to a wallet

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_top_up_wallet_request import DtoTopUpWalletRequest
from flexprice.models.dto_wallet_response import DtoWalletResponse
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
    api_instance = flexprice.WalletsApi(api_client)
    id = 'id_example' # str | Wallet ID
    request = flexprice.DtoTopUpWalletRequest() # DtoTopUpWalletRequest | Top up request

    try:
        # Top up wallet
        api_response = api_instance.wallets_id_top_up_post(id, request)
        print("The response of WalletsApi->wallets_id_top_up_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->wallets_id_top_up_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet ID | 
 **request** | [**DtoTopUpWalletRequest**](DtoTopUpWalletRequest.md)| Top up request | 

### Return type

[**DtoWalletResponse**](DtoWalletResponse.md)

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

# **wallets_id_transactions_get**
> DtoListWalletTransactionsResponse wallets_id_transactions_get(id, credits_available_gt=credits_available_gt, end_time=end_time, expand=expand, expiry_date_after=expiry_date_after, expiry_date_before=expiry_date_before, id2=id2, limit=limit, offset=offset, order=order, reference_id=reference_id, reference_type=reference_type, sort=sort, start_time=start_time, status=status, transaction_reason=transaction_reason, transaction_status=transaction_status, type=type)

Get wallet transactions

Get transactions for a wallet with pagination

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_list_wallet_transactions_response import DtoListWalletTransactionsResponse
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
    api_instance = flexprice.WalletsApi(api_client)
    id = 'id_example' # str | Wallet ID
    credits_available_gt = 3.4 # float |  (optional)
    end_time = 'end_time_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    expiry_date_after = 'expiry_date_after_example' # str |  (optional)
    expiry_date_before = 'expiry_date_before_example' # str |  (optional)
    id2 = 'id_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    reference_id = 'reference_id_example' # str |  (optional)
    reference_type = 'reference_type_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    transaction_reason = 'transaction_reason_example' # str |  (optional)
    transaction_status = 'transaction_status_example' # str |  (optional)
    type = 'type_example' # str |  (optional)

    try:
        # Get wallet transactions
        api_response = api_instance.wallets_id_transactions_get(id, credits_available_gt=credits_available_gt, end_time=end_time, expand=expand, expiry_date_after=expiry_date_after, expiry_date_before=expiry_date_before, id2=id2, limit=limit, offset=offset, order=order, reference_id=reference_id, reference_type=reference_type, sort=sort, start_time=start_time, status=status, transaction_reason=transaction_reason, transaction_status=transaction_status, type=type)
        print("The response of WalletsApi->wallets_id_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->wallets_id_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet ID | 
 **credits_available_gt** | **float**|  | [optional] 
 **end_time** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **expiry_date_after** | **str**|  | [optional] 
 **expiry_date_before** | **str**|  | [optional] 
 **id2** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **reference_id** | **str**|  | [optional] 
 **reference_type** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **transaction_reason** | **str**|  | [optional] 
 **transaction_status** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**DtoListWalletTransactionsResponse**](DtoListWalletTransactionsResponse.md)

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

# **wallets_post**
> DtoWalletResponse wallets_post(request)

Create a new wallet

Create a new wallet for a customer

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_create_wallet_request import DtoCreateWalletRequest
from flexprice.models.dto_wallet_response import DtoWalletResponse
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
    api_instance = flexprice.WalletsApi(api_client)
    request = flexprice.DtoCreateWalletRequest() # DtoCreateWalletRequest | Create wallet request

    try:
        # Create a new wallet
        api_response = api_instance.wallets_post(request)
        print("The response of WalletsApi->wallets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->wallets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoCreateWalletRequest**](DtoCreateWalletRequest.md)| Create wallet request | 

### Return type

[**DtoWalletResponse**](DtoWalletResponse.md)

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

