# Code

## Example Usage

```python
from flexprice.models import Code

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Code = "not_found"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"not_found"`
- `"already_exists"`
- `"version_conflict"`
- `"validation_error"`
- `"invalid_operation"`
- `"permission_denied"`
- `"http_client_error"`
- `"database_error"`
- `"system_error"`
- `"internal_error"`
- `"service_unavailable"`
