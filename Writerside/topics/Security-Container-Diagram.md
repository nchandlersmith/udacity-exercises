# Security Container Diagram

```D2
direction: down

dashboard: Web Dashboard
gateway: API gateway
sensor_container: Sensor Container
ingestion: Device Ingestion Service
controller_bus: Controller Event Bus
ingestion_bus: Ingestion Event Bus
central: Central Control Service
auth: Auth Server
userDB: User Database (Relational)
sensorDB: Sensor Database (Time-Series)
device_exfil: Device Command Outgress

dashboard.shape: person
dashboard.width: 50
userDB.shape:cylinder
sensorDB.shape: cylinder

sensor_container: {
    Light Sensor
    Temp Sensor
    Humidity Sensor
    Occupancy Sensor
}
sensor_container -> ingestion: sensor data
ingestion -> central: sensor data {
    style: {
        stroke-dash: 3
    }
}
central -> sensorDB: consumable sensor data
controller_bus: {
    Light Controller
    HVAC Controller
}
central -> controller_bus: transformed data
controller_bus -> device_exfil
device_exfil -> Devices

Devices:{
    Lights
    HVAC Syste
}

dashboard <-> gateway: data and commands
gateway <-> auth: auth & user information
auth -> userDB: auth & user information
gateway -> central: data and commands
```