# Tenants

## Overview

### Available Operations

* [get_tenant_billing_usage](#get_tenant_billing_usage) - Get billing usage for the current tenant
* [update_tenant](#update_tenant) - Update a tenant
* [get_tenant_by_id](#get_tenant_by_id) - Get tenant by ID

## get_tenant_billing_usage

Use when showing the current tenant's billing usage (e.g. admin billing page or usage caps). Returns subscription and usage for the tenant.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTenantBillingUsage" method="get" path="/tenant/billing" -->
```python
from flexprice import Flexprice


with Flexprice(
    "https://api.example.com",
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.tenants.get_tenant_billing_usage()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DtoTenantBillingUsage](../../models/dtotenantbillingusage.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorsErrorResponse   | 400, 404                            | application/json                    |
| models.errors.ErrorsErrorResponse   | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |

## update_tenant

Use when changing tenant details (e.g. name or billing info). Request body contains the fields to update.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTenant" method="put" path="/tenants/update" -->
```python
from flexprice import Flexprice


with Flexprice(
    "https://api.example.com",
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.tenants.update_tenant()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `billing_details`                                                                   | [Optional[models.DtoTenantBillingDetails]](../../models/dtotenantbillingdetails.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `metadata`                                                                          | Dict[str, *str*]                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `name`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.DtoTenantResponse](../../models/dtotenantresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorsErrorResponse   | 400, 404                            | application/json                    |
| models.errors.ErrorsErrorResponse   | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |

## get_tenant_by_id

Get tenant by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="getTenantById" method="get" path="/tenants/{id}" -->
```python
from flexprice import Flexprice


with Flexprice(
    "https://api.example.com",
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.tenants.get_tenant_by_id(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Tenant ID                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DtoTenantResponse](../../models/dtotenantresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorsErrorResponse   | 404                                 | application/json                    |
| models.errors.ErrorsErrorResponse   | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |