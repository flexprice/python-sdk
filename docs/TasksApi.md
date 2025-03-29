# flexprice.TasksApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_get**](TasksApi.md#tasks_get) | **GET** /tasks | List tasks
[**tasks_id_get**](TasksApi.md#tasks_id_get) | **GET** /tasks/{id} | Get a task by ID
[**tasks_id_process_post**](TasksApi.md#tasks_id_process_post) | **POST** /tasks/{id}/process | Process a task
[**tasks_id_status_put**](TasksApi.md#tasks_id_status_put) | **PUT** /tasks/{id}/status | Update task status
[**tasks_post**](TasksApi.md#tasks_post) | **POST** /tasks | Create a new task


# **tasks_get**
> DtoListTasksResponse tasks_get(created_by=created_by, end_time=end_time, entity_type=entity_type, expand=expand, limit=limit, offset=offset, order=order, sort=sort, start_time=start_time, status=status, task_status=task_status, task_type=task_type)

List tasks

List tasks with optional filtering

### Example


```python
import flexprice
from flexprice.models.dto_list_tasks_response import DtoListTasksResponse
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
    api_instance = flexprice.TasksApi(api_client)
    created_by = 'created_by_example' # str |  (optional)
    end_time = 'end_time_example' # str |  (optional)
    entity_type = 'entity_type_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order = 'order_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    start_time = 'start_time_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    task_status = 'task_status_example' # str |  (optional)
    task_type = 'task_type_example' # str |  (optional)

    try:
        # List tasks
        api_response = api_instance.tasks_get(created_by=created_by, end_time=end_time, entity_type=entity_type, expand=expand, limit=limit, offset=offset, order=order, sort=sort, start_time=start_time, status=status, task_status=task_status, task_type=task_type)
        print("The response of TasksApi->tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_by** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 
 **entity_type** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **task_status** | **str**|  | [optional] 
 **task_type** | **str**|  | [optional] 

### Return type

[**DtoListTasksResponse**](DtoListTasksResponse.md)

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

# **tasks_id_get**
> DtoTaskResponse tasks_id_get(id)

Get a task by ID

Get detailed information about a task

### Example


```python
import flexprice
from flexprice.models.dto_task_response import DtoTaskResponse
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
    api_instance = flexprice.TasksApi(api_client)
    id = 'id_example' # str | Task ID

    try:
        # Get a task by ID
        api_response = api_instance.tasks_id_get(id)
        print("The response of TasksApi->tasks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task ID | 

### Return type

[**DtoTaskResponse**](DtoTaskResponse.md)

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

# **tasks_id_process_post**
> Dict[str, object] tasks_id_process_post(id)

Process a task

Start processing a task

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
    api_instance = flexprice.TasksApi(api_client)
    id = 'id_example' # str | Task ID

    try:
        # Process a task
        api_response = api_instance.tasks_id_process_post(id)
        print("The response of TasksApi->tasks_id_process_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_id_process_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task ID | 

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_status_put**
> DtoTaskResponse tasks_id_status_put(id, status)

Update task status

Update the status of a task

### Example


```python
import flexprice
from flexprice.models.dto_task_response import DtoTaskResponse
from flexprice.models.dto_update_task_status_request import DtoUpdateTaskStatusRequest
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
    api_instance = flexprice.TasksApi(api_client)
    id = 'id_example' # str | Task ID
    status = flexprice.DtoUpdateTaskStatusRequest() # DtoUpdateTaskStatusRequest | New status

    try:
        # Update task status
        api_response = api_instance.tasks_id_status_put(id, status)
        print("The response of TasksApi->tasks_id_status_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_id_status_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task ID | 
 **status** | [**DtoUpdateTaskStatusRequest**](DtoUpdateTaskStatusRequest.md)| New status | 

### Return type

[**DtoTaskResponse**](DtoTaskResponse.md)

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

# **tasks_post**
> DtoTaskResponse tasks_post(task)

Create a new task

Create a new import/export task

### Example


```python
import flexprice
from flexprice.models.dto_create_task_request import DtoCreateTaskRequest
from flexprice.models.dto_task_response import DtoTaskResponse
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
    api_instance = flexprice.TasksApi(api_client)
    task = flexprice.DtoCreateTaskRequest() # DtoCreateTaskRequest | Task details

    try:
        # Create a new task
        api_response = api_instance.tasks_post(task)
        print("The response of TasksApi->tasks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->tasks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | [**DtoCreateTaskRequest**](DtoCreateTaskRequest.md)| Task details | 

### Return type

[**DtoTaskResponse**](DtoTaskResponse.md)

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

