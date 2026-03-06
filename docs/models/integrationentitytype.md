# IntegrationEntityType

## Example Usage

```python
from flexprice.models import IntegrationEntityType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: IntegrationEntityType = "customer"
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `CUSTOMER`     | customer       |
| `PLAN`         | plan           |
| `INVOICE`      | invoice        |
| `SUBSCRIPTION` | subscription   |
| `PAYMENT`      | payment        |
| `CREDIT_NOTE`  | credit_note    |
| `ADDON`        | addon          |
| `ITEM`         | item           |
| `ITEM_PRICE`   | item_price     |
| `PRICE`        | price          |