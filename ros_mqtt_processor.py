#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String
import paho.mqtt.client as mqtt


def on_connect(mqttc, obj, flags, reason_code, properties):
    print("reason_code: " + str(reason_code))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    value = msg.payload.decode('utf-8')  # Decode payload to string
    pub.publish(value)


def on_subscribe(mqttc, obj, mid, reason_code_list, properties):
    print("Subscribed: " + str(mid) + " " + str(reason_code_list))


def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.connect("_IP_ADDRESS_", 1883, 60)
mqttc.subscribe("_MQTT_TOPIC_")
pub = rospy.Publisher("_ROS_TOPIC_", String, queue_size=10)
rospy.init_node("ROS_MQTT_PROCESSOR")
mqttc.loop_forever()
