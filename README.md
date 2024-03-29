# Snowplow IoT Project
## Project Description
We will be using a Raspberry Pi Pico W as the Microcontroller which will connect wirelessly and Snowplow will validate and send my events to my data warehouse. This project is a proof of concept showing you how Snowplow can be used to track data from IoT devices, specifically we've made a satisfaction meter which tracks environmental data along with the events triggered by users. 

For more information on this project's code or build check out the full [blog post](https://snowplowanalytics.com/blog/2022/08/12/the-missed-opportunity-of-behavioral-data-in-iot-snowplow/).

## Code
```rgb.py``` is the main file which I execute on the Raspberry Pi. This could be named ```main.py``` to automatically run on its own. 
The other files: ```myrequest.py```, ```wifi.py```, ```dht11.py``` are used within ```rgb.py``` and need to also be stored on the Raspberry Pi.

## Author
My name is Bryan and I'm a 18 year old Snowplow Intern, looking to study Computer Science at University shortly after this. 

## Snowplow
Snowplow Analytics holds the throne when it comes to tracking behavioral data; IoT devices can be a gold mine. This is because IoT devices have the capability to send lots of small events as they get interacted with, these events can then be highly enriched by sensor data, APIs and Snowplow's automatic enrichment process.
What makes Snowplow the best in terms of tracking is their unique and flexible JSON schema architecture. Where engineers can define the data structure that they want to track, assign the type of data they expect, minimum and maximum values, etc. Once these are made and events are sent through these schemas, Snowplow validates each event to these rules. This gives you the flexibility and control of your data!
