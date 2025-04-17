# flexprice.InvoicesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_id_invoices_summary_get**](InvoicesApi.md#customers_id_invoices_summary_get) | **GET** /customers/{id}/invoices/summary | Get a customer invoice summary
[**invoices_get**](InvoicesApi.md#invoices_get) | **GET** /invoices | List invoices
[**invoices_id_finalize_post**](InvoicesApi.md#invoices_id_finalize_post) | **POST** /invoices/{id}/finalize | Finalize an invoice
[**invoices_id_get**](InvoicesApi.md#invoices_id_get) | **GET** /invoices/{id} | Get an invoice by ID
[**invoices_id_payment_attempt_post**](InvoicesApi.md#invoices_id_payment_attempt_post) | **POST** /invoices/{id}/payment/attempt | Attempt payment for an invoice
[**invoices_id_payment_put**](InvoicesApi.md#invoices_id_payment_put) | **PUT** /invoices/{id}/payment | Update invoice payment status
[**invoices_id_pdf_get**](InvoicesApi.md#invoices_id_pdf_get) | **GET** /invoices/{id}/pdf | Get PDF for an invoice
[**invoices_id_void_post**](InvoicesApi.md#invoices_id_void_post) | **POST** /invoices/{id}/void | Void an invoice
[**invoices_post**](InvoicesApi.md#invoices_post) | **POST** /invoices | Create a new invoice
[**invoices_preview_post**](InvoicesApi.md#invoices_preview_post) | **POST** /invoices/preview | Get a preview invoice


# **customers_id_invoices_summary_get**
> DtoCustomerMultiCurrencyInvoiceSummary customers_id_invoices_summary_get(id)

Get a customer invoice summary

Get a customer invoice summary

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_customer_multi_currency_invoice_summary import DtoCustomerMultiCurrencyInvoiceSummary
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
    api_instance = flexprice.InvoicesApi(api_client)
    id = 'id_example' # str | Customer ID

    try:
        # Get a customer invoice summary
        api_response = api_instance.customers_id_invoices_summary_get(id)
        print("The response of InvoicesApi->customers_id_invoices_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->customers_id_invoices_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 

### Return type

[**DtoCustomerMultiCurrencyInvoiceSummary**](DtoCustomerMultiCurrencyInvoiceSummary.md)

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

# **invoices_get**
> DtoListInvoicesResponse invoices_get(amount_due_gt=amount_due_gt, amount_remaining_gt=amount_remaining_gt, customer_id=customer_id, end_time=end_time, expand=expand, invoice_ids=invoice_ids, invoice_status=invoice_status, invoice_type=invoice_type, limit=limit, offset=offset, order=order, payment_status=payment_status, sort=sort, start_time=start_time, status=status, subscription_id=subscription_id)

List invoices

List invoices with optional filtering

### Example


```python
import flexprice
from flexprice.models.dto_list_invoices_response import DtoListInvoicesResponse
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
    api_instance = flexprice.InvoicesApi(api_client)
    amount_due_gt = 3.4 # float |  (optional)
    amount_remaining_gt = 3.4 # float |  (optional)
    customer_id = 'customer_id_example' # str |  (optional)
    end_time = 'end_time_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    invoice_ids = ['invoice_ids_example'] # List[str] |  (optional)
    invoice_status = ['invoice_status_example'] # List[str] |  (optional)
    invoice_type = 'invoice_type_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    payment_status = ['payment_status_example'] # List[str] |  (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    subscription_id = 'subscription_id_example' # str |  (optional)

    try:
        # List invoices
        api_response = api_instance.invoices_get(amount_due_gt=amount_due_gt, amount_remaining_gt=amount_remaining_gt, customer_id=customer_id, end_time=end_time, expand=expand, invoice_ids=invoice_ids, invoice_status=invoice_status, invoice_type=invoice_type, limit=limit, offset=offset, order=order, payment_status=payment_status, sort=sort, start_time=start_time, status=status, subscription_id=subscription_id)
        print("The response of InvoicesApi->invoices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount_due_gt** | **float**|  | [optional] 
 **amount_remaining_gt** | **float**|  | [optional] 
 **customer_id** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **invoice_ids** | [**List[str]**](str.md)|  | [optional] 
 **invoice_status** | [**List[str]**](str.md)|  | [optional] 
 **invoice_type** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **payment_status** | [**List[str]**](str.md)|  | [optional] 
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **subscription_id** | **str**|  | [optional] 

### Return type

[**DtoListInvoicesResponse**](DtoListInvoicesResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_id_finalize_post**
> Dict[str, object] invoices_id_finalize_post(id)

Finalize an invoice

Finalize a draft invoice

### Example


```python
import flexprice
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
    api_instance = flexprice.InvoicesApi(api_client)
    id = 'id_example' # str | Invoice ID

    try:
        # Finalize an invoice
        api_response = api_instance.invoices_id_finalize_post(id)
        print("The response of InvoicesApi->invoices_id_finalize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_id_finalize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invoice ID | 

### Return type

**Dict[str, object]**

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_id_get**
> DtoInvoiceResponse invoices_id_get(id)

Get an invoice by ID

Get detailed information about an invoice

### Example


```python
import flexprice
from flexprice.models.dto_invoice_response import DtoInvoiceResponse
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
    api_instance = flexprice.InvoicesApi(api_client)
    id = 'id_example' # str | Invoice ID

    try:
        # Get an invoice by ID
        api_response = api_instance.invoices_id_get(id)
        print("The response of InvoicesApi->invoices_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invoice ID | 

### Return type

[**DtoInvoiceResponse**](DtoInvoiceResponse.md)

### Authorization

No authorization required

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

# **invoices_id_payment_attempt_post**
> Dict[str, object] invoices_id_payment_attempt_post(id)

Attempt payment for an invoice

Attempt to pay an invoice using customer's available wallets

### Example


```python
import flexprice
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
    api_instance = flexprice.InvoicesApi(api_client)
    id = 'id_example' # str | Invoice ID

    try:
        # Attempt payment for an invoice
        api_response = api_instance.invoices_id_payment_attempt_post(id)
        print("The response of InvoicesApi->invoices_id_payment_attempt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_id_payment_attempt_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invoice ID | 

### Return type

**Dict[str, object]**

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

# **invoices_id_payment_put**
> DtoInvoiceResponse invoices_id_payment_put(id, request)

Update invoice payment status

Update the payment status of an invoice

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import flexprice
from flexprice.models.dto_invoice_response import DtoInvoiceResponse
from flexprice.models.dto_update_payment_status_request import DtoUpdatePaymentStatusRequest
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
    api_instance = flexprice.InvoicesApi(api_client)
    id = 'id_example' # str | Invoice ID
    request = flexprice.DtoUpdatePaymentStatusRequest() # DtoUpdatePaymentStatusRequest | Payment Status Update Request

    try:
        # Update invoice payment status
        api_response = api_instance.invoices_id_payment_put(id, request)
        print("The response of InvoicesApi->invoices_id_payment_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_id_payment_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invoice ID | 
 **request** | [**DtoUpdatePaymentStatusRequest**](DtoUpdatePaymentStatusRequest.md)| Payment Status Update Request | 

### Return type

[**DtoInvoiceResponse**](DtoInvoiceResponse.md)

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

# **invoices_id_pdf_get**
> bytearray invoices_id_pdf_get(id, url=url)

Get PDF for an invoice

Retrieve the PDF document for a specific invoice by its ID

### Example


```python
import flexprice
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
    api_instance = flexprice.InvoicesApi(api_client)
    id = 'id_example' # str | Invoice ID
    url = True # bool | Return presigned URL from s3 instead of PDF (optional)

    try:
        # Get PDF for an invoice
        api_response = api_instance.invoices_id_pdf_get(id, url=url)
        print("The response of InvoicesApi->invoices_id_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_id_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invoice ID | 
 **url** | **bool**| Return presigned URL from s3 instead of PDF | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_id_void_post**
> Dict[str, object] invoices_id_void_post(id)

Void an invoice

Void an invoice that hasn't been paid

### Example


```python
import flexprice
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
    api_instance = flexprice.InvoicesApi(api_client)
    id = 'id_example' # str | Invoice ID

    try:
        # Void an invoice
        api_response = api_instance.invoices_id_void_post(id)
        print("The response of InvoicesApi->invoices_id_void_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_id_void_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Invoice ID | 

### Return type

**Dict[str, object]**

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_post**
> DtoInvoiceResponse invoices_post(invoice)

Create a new invoice

Create a new invoice with the provided details

### Example


```python
import flexprice
from flexprice.models.dto_create_invoice_request import DtoCreateInvoiceRequest
from flexprice.models.dto_invoice_response import DtoInvoiceResponse
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
    api_instance = flexprice.InvoicesApi(api_client)
    invoice = flexprice.DtoCreateInvoiceRequest() # DtoCreateInvoiceRequest | Invoice details

    try:
        # Create a new invoice
        api_response = api_instance.invoices_post(invoice)
        print("The response of InvoicesApi->invoices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice** | [**DtoCreateInvoiceRequest**](DtoCreateInvoiceRequest.md)| Invoice details | 

### Return type

[**DtoInvoiceResponse**](DtoInvoiceResponse.md)

### Authorization

No authorization required

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

# **invoices_preview_post**
> DtoInvoiceResponse invoices_preview_post(request)

Get a preview invoice

Get a preview invoice

### Example


```python
import flexprice
from flexprice.models.dto_get_preview_invoice_request import DtoGetPreviewInvoiceRequest
from flexprice.models.dto_invoice_response import DtoInvoiceResponse
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
    api_instance = flexprice.InvoicesApi(api_client)
    request = flexprice.DtoGetPreviewInvoiceRequest() # DtoGetPreviewInvoiceRequest | Preview Invoice Request

    try:
        # Get a preview invoice
        api_response = api_instance.invoices_preview_post(request)
        print("The response of InvoicesApi->invoices_preview_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_preview_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoGetPreviewInvoiceRequest**](DtoGetPreviewInvoiceRequest.md)| Preview Invoice Request | 

### Return type

[**DtoInvoiceResponse**](DtoInvoiceResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

