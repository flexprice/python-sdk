# ScheduledTaskEntityType

## Example Usage

```python
from flexprice.models import ScheduledTaskEntityType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ScheduledTaskEntityType = "events"
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `EVENTS`        | events          |
| `INVOICE`       | invoice         |
| `CREDIT_TOPUPS` | credit_topups   |
| `CREDIT_USAGE`  | credit_usage    |