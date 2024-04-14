import paho.mqtt.client as mqtt

# Define your MQTT broker connection details here
broker_address = "_IP_ADDRESS_"
broker_port = 1883

def on_connect(mqttc, obj, flags, reason_code, properties):
  print("Connected to MQTT Broker with reason code: " + str(reason_code))

def publish_message(client, topic, message):
  # This function publishes a message to the specified topic
  client.publish(topic, message)
  print("Published message: '" + message + "' to topic: " + topic)

def main():
  # Create an MQTT client object
  client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

  # Set the on_connect callback function
  client.on_connect = on_connect

  # Connect to the MQTT broker
  client.connect(broker_address, broker_port)

  # Get user input for the message
  message = input("Enter the message to publish: ")

  # Publish the message to the topic "my_val"
  publish_message(client, "_MQTT_TOPIC_", message)

  # Disconnect from the MQTT broker
  client.disconnect()

if __name__ == "__main__":
  while(1):
  	main()

