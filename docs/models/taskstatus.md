# TaskStatus

## Example Usage

```python
from flexprice.models import TaskStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TaskStatus = "PENDING"
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `PENDING`    | PENDING      |
| `PROCESSING` | PROCESSING   |
| `COMPLETED`  | COMPLETED    |
| `FAILED`     | FAILED       |