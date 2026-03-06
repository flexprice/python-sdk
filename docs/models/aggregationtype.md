# AggregationType

## Example Usage

```python
from flexprice.models import AggregationType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AggregationType = "COUNT"
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `COUNT`               | COUNT                 |
| `SUM`                 | SUM                   |
| `AVG`                 | AVG                   |
| `COUNT_UNIQUE`        | COUNT_UNIQUE          |
| `LATEST`              | LATEST                |
| `SUM_WITH_MULTIPLIER` | SUM_WITH_MULTIPLIER   |
| `MAX`                 | MAX                   |
| `WEIGHTED_SUM`        | WEIGHTED_SUM          |