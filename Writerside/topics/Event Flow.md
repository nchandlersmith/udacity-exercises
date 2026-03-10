# Event Flow
```D2
HVAC Control via Occupancy Sensor: {
    direction: down
    
    sensor: Occupancy Sensor
    ingestion: Device Ingestion Service
    bus: Event Bus
    controller: Central Controller
    lighting: Lighting Controller
    ac: AirConditioner
    database: Time-Series Database
    
    sensor -> ingestion
    ingestion -> controller
    controller -> bus
    bus -> lighting
    bus -> ac
    bus -> database
}
```