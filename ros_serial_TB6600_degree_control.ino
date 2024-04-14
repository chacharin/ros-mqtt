
#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;

#define directionPin _PIN_NUMBER_
#define stepPin _PIN_NUMBER_
#define stepsPerRevolution 6400

 
void callback_subscriber_obj(const std_msgs::String &cmd_msg)
{
    String cmd = cmd_msg.data; // Use std::string instead of String

    if (cmd.startsWith("cw"))
    {
        // Extract the degree value
        float degrees = cmd.substring(3).toFloat();
        // Rotate clockwise by the specified degrees
        rotateDegrees(degrees, true);
    }
    else if (cmd.startsWith("ccw"))
    {
        // Extract the degree value
        float degrees = cmd.substring(4).toFloat();
        // Rotate counterclockwise by the specified degrees
        rotateDegrees(degrees, false);
    }
}

ros::Subscriber<std_msgs::String> subscriber_obj("_ROS_TOPIC_", callback_subscriber_obj);


void setup()
{
  pinMode(13,OUTPUT);
  pinMode(directionPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
  nh.initNode();
  nh.subscribe(subscriber_obj);
}
 
void loop()
{
  nh.spinOnce();
  delay(1);
}

void rotateDegrees(float degrees, bool clockwise) {
  int stepsToTake = degrees / 360.0 * stepsPerRevolution;
  
  digitalWrite(directionPin, clockwise ? HIGH : LOW);
  for (int i = 0; i < stepsToTake; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(100); // Adjust speed here
    digitalWrite(stepPin, LOW);
    delayMicroseconds(100); // Adjust speed here
  }
}
