# CheckoutPaymentProvider

## Example Usage

```python
from flexprice.models import CheckoutPaymentProvider

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CheckoutPaymentProvider = "razorpay"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"razorpay"`
- `"chargebee"`
