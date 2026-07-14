# RejectedEventReason

## Example Usage

```python
from flexprice.models import RejectedEventReason

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RejectedEventReason = "no_meter_for_event_name"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"no_meter_for_event_name"`
- `"no_matching_meter"`
