# ScheduleStatus

## Example Usage

```python
from flexprice.models import ScheduleStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ScheduleStatus = "pending"
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `EXECUTING` | executing   |
| `EXECUTED`  | executed    |
| `CANCELLED` | cancelled   |
| `FAILED`    | failed      |