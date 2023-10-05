This readme file provides instructions for running a performance test using Locust for two scenarios:

1.User with authentication create a booking and update the booking order.
2.User without authentication creates a booking and fetch the booking order.

Prerequisites

Before running the Locust performance test, ensure you have the following prerequisites installed on your system:

1.Python 3.7 or higher
2.Locust: You can install Locust using pip with pip install locust

To run a test ,

locust -f core/locust_exec_AddBooking.py<path/file name> --host https://restful-booker.herokuapp.com <host url>

Admin creds -> admin_user.csv
Data used for performance test-> booking_details.json

