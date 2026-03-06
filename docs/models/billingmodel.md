# BillingModel

## Example Usage

```python
from flexprice.models import BillingModel

# Open enum: unrecognized values are captured as UnrecognizedStr
value: BillingModel = "FLAT_FEE"
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `FLAT_FEE` | FLAT_FEE   |
| `PACKAGE`  | PACKAGE    |
| `TIERED`   | TIERED     |