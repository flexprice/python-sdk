# Integrations

## Overview

### Available Operations

* [link_integration_mapping](#link_integration_mapping) - Link integration mapping

## link_integration_mapping

Link a FlexPrice entity to provider entity with provider-specific side effects.

### Example Usage

<!-- UsageSnippet language="python" operationID="linkIntegrationMapping" method="post" path="/integrations/link" -->
```python
from flexprice import Flexprice


with Flexprice(
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.integrations.link_integration_mapping(entity_id="<id>", entity_type="item_price", provider_entity_id="<id>", provider_type="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `entity_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `entity_type`                                                         | [models.IntegrationEntityType](../../models/integrationentitytype.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `provider_entity_id`                                                  | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `provider_type`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `metadata`                                                            | Dict[str, *Any*]                                                      | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.DtoLinkIntegrationMappingResponse](../../models/dtolinkintegrationmappingresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorsErrorResponse   | 400                                 | application/json                    |
| models.errors.ErrorsErrorResponse   | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |