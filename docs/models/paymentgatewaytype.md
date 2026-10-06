# PaymentGatewayType

## Example Usage

```python
from flexprice.models import PaymentGatewayType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PaymentGatewayType = "stripe"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"stripe"`
- `"razorpay"`
- `"nomod"`
- `"moyasar"`
- `"paddle"`
- `"whop"`
- `"chargebee"`
