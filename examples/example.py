#!/usr/bin/env python3
"""
FlexPrice Python SDK Example

This example demonstrates how to use the FlexPrice Python SDK
to interact with the FlexPrice API.
"""

import os
import time
import datetime
from pprint import pprint

# Import the FlexPrice SDK
import flexprice_client
from flexprice_client.api import customers_api, events_api
from flexprice_client.model.dto_create_customer_request import DtoCreateCustomerRequest
from flexprice_client.model.dto_ingest_event_request import DtoIngestEventRequest

# Optional: Load environment variables from .env file
# Uncomment if you have python-dotenv installed
# from dotenv import load_dotenv
# load_dotenv()


def run_example():
    """Main example function demonstrating FlexPrice SDK usage."""
    print("Starting FlexPrice Python SDK example...")

    try:
        # Configure the API client
        api_key = os.getenv("FLEXPRICE_API_KEY")
        api_host = os.getenv("FLEXPRICE_API_HOST", "api.flexprice.io")

        if not api_key:
            raise ValueError("FLEXPRICE_API_KEY environment variable is required")

        # Configure API key authorization
        configuration = flexprice_client.Configuration(
            host=f"https://{api_host}"
        )
        
        # Add API key header
        configuration.api_key['ApiKeyAuth'] = api_key
        configuration.api_key_prefix['ApiKeyAuth'] = ''
        
        # Set the X-API-Key header name
        configuration.api_key['x-api-key'] = api_key

        # Create API client
        with flexprice_client.ApiClient(configuration) as api_client:
            # Create API instances
            customers_api_instance = customers_api.CustomersApi(api_client)
            events_api_instance = events_api.EventsApi(api_client)

            # Generate a unique customer ID for this example
            customer_id = f"sample-customer-{int(time.time())}"
            
            # Step 1: Create a customer
            print(f"Creating customer with ID: {customer_id}...")
            
            customer_request = DtoCreateCustomerRequest(
                external_id=customer_id,
                email=f"example-{customer_id}@example.com",
                name="Example Customer",
                metadata={
                    "source": "python-sdk-example",
                    "created_at": datetime.datetime.now().isoformat()
                }
            )
            
            customers_api_instance.customers_post(dto_create_customer_request=customer_request)
            print("Customer created successfully!")

            # Step 2: Create an event
            print("Creating event...")
            
            event_request = DtoIngestEventRequest(
                event_name="Sample Event",
                external_customer_id=customer_id,
                properties={
                    "source": "python_sample_app",
                    "environment": "test",
                    "timestamp": datetime.datetime.now().isoformat()
                },
                source="python_sample_app",
                timestamp=datetime.datetime.now().isoformat()
            )
            
            event_result = events_api_instance.events_post(dto_ingest_event_request=event_request)
            print(f"Event created successfully! ID: {event_result.get('event_id')}")

            # Step 3: Retrieve events for this customer
            print(f"Retrieving events for customer {customer_id}...")
            
            events = events_api_instance.events_get(external_customer_id=customer_id)
            
            print(f"Found {len(events.events)} events:")
            
            for i, event in enumerate(events.events):
                print(f"Event {i+1}: {event.id} - {event.event_name}")
                print(f"Properties: {event.properties}")
            
            print("Example completed successfully!")

    except flexprice_client.ApiException as e:
        print(f"Exception when calling FlexPrice API: {e}")
        print(f"Status code: {e.status}")
        print(f"Reason: {e.reason}")
        print(f"HTTP response headers: {e.headers}")
        print(f"HTTP response body: {e.body}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    run_example() 