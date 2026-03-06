# PriceEntityType

## Example Usage

```python
from flexprice.models import PriceEntityType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PriceEntityType = "PLAN"
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `PLAN`         | PLAN           |
| `SUBSCRIPTION` | SUBSCRIPTION   |
| `ADDON`        | ADDON          |
| `PRICE`        | PRICE          |
| `COSTSHEET`    | COSTSHEET      |