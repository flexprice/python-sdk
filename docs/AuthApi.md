# flexprice.AuthApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_post**](AuthApi.md#auth_login_post) | **POST** /auth/login | Login
[**auth_signup_post**](AuthApi.md#auth_signup_post) | **POST** /auth/signup | Sign up


# **auth_login_post**
> DtoAuthResponse auth_login_post(login)

Login

Login a user

### Example


```python
import flexprice
from flexprice.models.dto_auth_response import DtoAuthResponse
from flexprice.models.dto_login_request import DtoLoginRequest
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
    api_instance = flexprice.AuthApi(api_client)
    login = flexprice.DtoLoginRequest() # DtoLoginRequest | Login request

    try:
        # Login
        api_response = api_instance.auth_login_post(login)
        print("The response of AuthApi->auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | [**DtoLoginRequest**](DtoLoginRequest.md)| Login request | 

### Return type

[**DtoAuthResponse**](DtoAuthResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_signup_post**
> DtoAuthResponse auth_signup_post(signup)

Sign up

Sign up a new user

### Example


```python
import flexprice
from flexprice.models.dto_auth_response import DtoAuthResponse
from flexprice.models.dto_sign_up_request import DtoSignUpRequest
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
    api_instance = flexprice.AuthApi(api_client)
    signup = flexprice.DtoSignUpRequest() # DtoSignUpRequest | Sign up request

    try:
        # Sign up
        api_response = api_instance.auth_signup_post(signup)
        print("The response of AuthApi->auth_signup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_signup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup** | [**DtoSignUpRequest**](DtoSignUpRequest.md)| Sign up request | 

### Return type

[**DtoAuthResponse**](DtoAuthResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

