# FailurePointType

## Example Usage

```python
from flexprice.models import FailurePointType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FailurePointType = "customer_lookup"
```


## Values

| Name                            | Value                           |
| ------------------------------- | ------------------------------- |
| `CUSTOMER_LOOKUP`               | customer_lookup                 |
| `METER_LOOKUP`                  | meter_lookup                    |
| `PRICE_LOOKUP`                  | price_lookup                    |
| `SUBSCRIPTION_LINE_ITEM_LOOKUP` | subscription_line_item_lookup   |