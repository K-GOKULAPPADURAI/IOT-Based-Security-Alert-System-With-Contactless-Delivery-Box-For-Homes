# IOT-Based-Security-Alert-System-With-Contactless-Delivery-Box-For-Homes
An effective solution of covid-19 pandemic situtation and security alert system for home in case abnormal activities  
# Home Security and Contactless Delivery System

The Home Security and Contactless Delivery System is an IoT project that aims to enhance home security and facilitate contactless product delivery. The system utilizes various sensors and technologies to provide a secure and convenient experience for homeowners.

## Abstract

The Home Security and Contactless Delivery System is designed to address the growing need for home security and contactless services. The project integrates motion detection, live video streaming, and remote lock control to ensure the safety of homes and enable secure product delivery. This project provides an overview of the existing system's limitations and proposes an advanced system with several advantages, including improved security, remote monitoring, and COVID-19 safety measures.

## Existing System with Disadvantages

The existing home security systems lack comprehensive features and face the following disadvantages:

1. Limited Security: Traditional security systems rely on basic alarms and surveillance cameras, which may not provide robust protection against intrusions.

2. Lack of Remote Monitoring: Most existing systems lack remote monitoring capabilities, preventing homeowners from monitoring their properties in real-time.

3. Physical Contact during Delivery: Traditional product delivery methods involve direct physical contact, which can pose risks, especially during the COVID-19 pandemic.

## Proposed System with Advantages

The proposed Home Security and Contactless Delivery System offers the following advantages:

1. Enhanced Security: The system integrates motion sensors that detect any unauthorized movements and trigger immediate alerts, allowing homeowners to take necessary action promptly.

2. Remote Monitoring: With the live video streaming feature, homeowners can remotely monitor their homes using a web page interface. This enables real-time surveillance and provides peace of mind.

3. Contactless Delivery: The project incorporates a contactless delivery drop box, which allows for safe and secure product delivery without direct physical contact. Homeowners can remotely control the drop box, ensuring secure deliveries even when they are not present.

4. Firebase Integration: The system integrates with Firebase for storage and retrieval of captured images and videos. Homeowners can easily store and access captured data for future reference.

5. Solenoid Lock Control: The project includes a 12V solenoid lock controlled by a relay, enabling remote locking and unlocking of the drop box. This feature adds an extra layer of security and control over the delivery process.

6. COVID-19 Safety Measures: The system incorporates contactless delivery and remote monitoring capabilities, minimizing physical contact during product delivery and reducing the risk of transmission. It ensures the safety and well-being of homeowners, especially during the COVID-19 pandemic.

## Module Split-Up

The Home Security and Contactless Delivery System can be divided into the following modules:

1. Motion Detection: This module includes the PIR motion sensor, which detects any motion within its range and triggers the system to capture images or videos.

2. Video and Image Capture: This module captures images or videos when motion is detected and stores them for further processing.

3. Alert System: The alert system generates real-time notifications or alerts to inform homeowners about potential intrusions or suspicious activities.

4. Contactless Delivery Drop Box: This module controls the contactless delivery drop box, allowing secure and convenient product delivery.

5. Remote Monitoring and Control: This module enables homeowners to remotely monitor their homes, control the drop box, and receive updates on the system's status through a web page interface.

6. Firebase Integration: The system integrates with Firebase for storing and retrieving captured images and videos.

## Demo Video

[Click here to watch the demo video](https://www.youtube.com/watch?v=YOUR_DEMO_VIDEO_LINK)

## Running Each Sensor Separately

To run each sensor separately, follow these steps:

1. Set up the required hardware components for each sensor (e.g., PIR motion sensor, solenoid lock, etc.)

2. Connect the sensors to the appropriate GPIO pins of the

Raspberry Pi.

3. Install the necessary libraries and dependencies for each sensor by running the following commands:

   ```shell
   pip install <library_name>
   ```

4. Run the following code lines in separate Python files to test each sensor:

- Ultrasonic Sensor (`ultrasonic.py`):

  ```shell
  python ultrasonic.py
  ```

- Motion Sensor (`motionsensor.py`):

  ```shell
  python motionsensor.py
  ```

- Solenoid Lock (`solenoidlock.py`):

  ```shell
  python solenoidlock.py
  ```

- PiCamera (`camera.py`):

  ```shell
  python camera.py
  ```

Make sure to replace `<library_name>` with the actual library name required for each sensor. Additionally, ensure that you have the necessary hardware components connected to the Raspberry Pi.

## Running the Whole Project

To run the entire Home Security and Contactless Delivery System, follow these steps:

1. Set up the hardware components for each sensor and ensure they are connected to the Raspberry Pi.

2. Install the required libraries and dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

3. Open the `main.py` file and configure any necessary settings or parameters.

4. Run the following command to start the system:

   ```shell
   python main.py
   ```

The system will now be up and running, providing home security and contactless delivery functionalities.

Note: It is essential to refer to the project's documentation and README file for any specific instructions or additional details on configuring and running the system.

## Conclusion

The Home Security and Contactless Delivery System offers an effective solution to enhance home security and facilitate secure product delivery. By integrating motion detection, remote monitoring, contactless delivery, and advanced features, the system provides homeowners with peace of mind and convenience. The project's modular approach allows for easy customization and expansion, making it a versatile solution for various home security requirements.


