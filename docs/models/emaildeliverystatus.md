# EmailDeliveryStatus

## Example Usage

```python
from flexprice.models import EmailDeliveryStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EmailDeliveryStatus = "queued"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"queued"`
- `"sent"`
- `"delivery_delayed"`
- `"delivered"`
- `"bounced"`
- `"complained"`
- `"failed"`
- `"suppressed"`
- `"skipped"`
