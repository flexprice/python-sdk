# MeterUsage

## Overview

### Available Operations

* [get_meter_usage_analytics](#get_meter_usage_analytics) - Get meter usage analytics
* [query_meter_usage](#query_meter_usage) - Query meter usage

## get_meter_usage_analytics

Query aggregated usage from meter_usage table for multiple meters

### Example Usage

<!-- UsageSnippet language="python" operationID="getMeterUsageAnalytics" method="post" path="/meter-usage/analytics" -->
```python
from flexprice import Flexprice
from flexprice.utils import parse_datetime


with Flexprice(
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.meter_usage.get_meter_usage_analytics(aggregation_type="COUNT", end_time=parse_datetime("2024-02-01T00:00:00Z"), external_customer_id="cust_123", meter_ids=[
        "mtr_abc",
        "mtr_def",
    ], start_time=parse_datetime("2024-01-01T00:00:00Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `aggregation_type`                                                   | [models.AggregationType](../../models/aggregationtype.md)            | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `end_time`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  | 2024-02-01T00:00:00Z                                                 |
| `external_customer_id`                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  | cust_123                                                             |
| `meter_ids`                                                          | List[*str*]                                                          | :heavy_check_mark:                                                   | N/A                                                                  | [<br/>"mtr_abc",<br/>"mtr_def"<br/>]                                 |
| `start_time`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  | 2024-01-01T00:00:00Z                                                 |
| `billing_anchor`                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `window_size`                                                        | [Optional[models.WindowSize]](../../models/windowsize.md)            | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.MeterUsageAnalyticsResponse](../../models/meterusageanalyticsresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorResponse         | 400                                 | application/json                    |
| models.errors.ErrorResponse         | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |

## query_meter_usage

Query aggregated usage from meter_usage table for a single meter with optional time-window bucketing

### Example Usage

<!-- UsageSnippet language="python" operationID="queryMeterUsage" method="post" path="/meter-usage/query" -->
```python
from flexprice import Flexprice
from flexprice.utils import parse_datetime


with Flexprice(
    api_key_auth="<YOUR_API_KEY_HERE>",
) as f_client:

    res = f_client.meter_usage.query_meter_usage(aggregation_type="WEIGHTED_SUM", end_time=parse_datetime("2024-02-01T00:00:00Z"), external_customer_id="cust_123", meter_id="mtr_abc", start_time=parse_datetime("2024-01-01T00:00:00Z"), billing_anchor=parse_datetime("2024-01-15T00:00:00Z"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `aggregation_type`                                                   | [models.AggregationType](../../models/aggregationtype.md)            | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `end_time`                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  | 2024-02-01T00:00:00Z                                                 |
| `external_customer_id`                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  | cust_123                                                             |
| `meter_id`                                                           | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  | mtr_abc                                                              |
| `start_time`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  | 2024-01-01T00:00:00Z                                                 |
| `billing_anchor`                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  | 2024-01-15T00:00:00Z                                                 |
| `window_size`                                                        | [Optional[models.WindowSize]](../../models/windowsize.md)            | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |                                                                      |

### Response

**[models.MeterUsageQueryResponse](../../models/meterusagequeryresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| models.errors.ErrorResponse         | 400                                 | application/json                    |
| models.errors.ErrorResponse         | 500                                 | application/json                    |
| models.errors.FlexpriceDefaultError | 4XX, 5XX                            | \*/\*                               |