# AlertType

## Example Usage

```python
from flexprice.models import AlertType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AlertType = "low_ongoing_balance"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"low_ongoing_balance"`
- `"low_credit_balance"`
- `"feature_wallet_balance"`
