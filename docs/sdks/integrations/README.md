# Integrations

## Overview

### Available Operations

* [get_integration](#get_integration) - Get integration details
* [create_or_update_integration](#create_or_update_integration) - Create or update an integration
* [list_linked_integrations](#list_linked_integrations) - List linked integrations
* [delete_integration](#delete_integration) - Delete an integration

## get_integration

Use when you need to check or display integration config (e.g. which provider is linked). Sensitive values may be redacted.

### Example Usage

<!-- UsageSnippet language="python" operationID="getIntegration" method="get" path="/secrets/integrations/by-provider/{provider}" -->
```python
from flexprice import Flexprice


with Flexprice(
    "https://api.example.com",
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.integrations.get_integration(provider="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Integration provider                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DtoSecretResponse](../../models/dtosecretresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorsErrorResponse   | 404                                 | application/json                    |
| models.errors.ErrorsErrorResponse   | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |

## create_or_update_integration

Use when storing or updating credentials for an external integration (e.g. Stripe, HubSpot). Secrets are encrypted at rest.

### Example Usage

<!-- UsageSnippet language="python" operationID="createOrUpdateIntegration" method="post" path="/secrets/integrations/create/{provider}" -->
```python
from flexprice import Flexprice


with Flexprice(
    "https://api.example.com",
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.integrations.create_or_update_integration(provider_param="<value>", credentials={
        "key": "<value>",
    }, name="<value>", provider="chargebee")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider_param`                                                    | *str*                                                               | :heavy_check_mark:                                                  | Integration provider                                                |
| `credentials`                                                       | Dict[str, *str*]                                                    | :heavy_check_mark:                                                  | N/A                                                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `provider`                                                          | [models.SecretProvider](../../models/secretprovider.md)             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DtoSecretResponse](../../models/dtosecretresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorsErrorResponse   | 400                                 | application/json                    |
| models.errors.ErrorsErrorResponse   | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |

## list_linked_integrations

Use when showing which integrations are connected (e.g. settings page). Returns providers that have valid linked credentials.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLinkedIntegrations" method="get" path="/secrets/integrations/linked" -->
```python
from flexprice import Flexprice


with Flexprice(
    "https://api.example.com",
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.integrations.list_linked_integrations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DtoLinkedIntegrationsResponse](../../models/dtolinkedintegrationsresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorsErrorResponse   | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |

## delete_integration

Use when disconnecting an integration (e.g. switching provider or removing OAuth). Deletes stored credentials.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteIntegration" method="delete" path="/secrets/integrations/{id}" -->
```python
from flexprice import Flexprice


with Flexprice(
    "https://api.example.com",
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    f_client.integrations.delete_integration(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Integration ID                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorsErrorResponse   | 404                                 | application/json                    |
| models.errors.ErrorsErrorResponse   | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |