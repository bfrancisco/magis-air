CREATE DATABASE magis_air;
\c magis_air

CREATE TABLE city (
    name VARCHAR(255) NOT NULL PRIMARY KEY,
    country VARCHAR(255) NOT NULL 
);

CREATE TABLE route (
    route_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    distance FLOAT(2) NOT NULL,
    city_origin VARCHAR(255) NOT NULL,
    city_destination VARCHAR(255) NOT NULL,
    UNIQUE (city_destination, city_origin),
    FOREIGN KEY (city_origin) REFERENCES city(name),
    FOREIGN KEY (city_destination) REFERENCES city(name)
);

CREATE TABLE flight_schedule (
    flight_code SERIAL NOT NULL UNIQUE PRIMARY KEY,
    departure_time TIME NOT NULL,
    arrival_time TIME GENERATED ALWAYS AS (departure_time + duration) STORED,
    duration INTERVAL NOT NULL,
    departure_date DATE NOT NULL,
    flight_cost FLOAT(2) NOT NULL,
    route_id INT NOT NULL,
    FOREIGN KEY (route_id) REFERENCES route(route_id)
);

CREATE TABLE passenger (
    passenger_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    gender VARCHAR(6) NOT NULL,
    CHECK (gender IN ('Male', 'Female', 'Nonbinary', 'Prefer not to say'))
);

CREATE TABLE booking (
    booking_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    booking_date DATE NOT NULL,
    total_cost FLOAT(2),
    passenger_id INT NOT NULL,
    FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id),
    flight_code INT NOT NULL,
    FOREIGN KEY (flight_code) REFERENCES flight_schedule(flight_code)
);

CREATE TABLE additional_item (
    item_no SERIAL NOT NULL UNIQUE PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    cost FLOAT(2) NOT NULL
);

CREATE TABLE booking_additional_item(
    booking_id INT NOT NULL,
    item_no INT NOT NULL, 
    qty INT NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES booking(booking_id) ON DELETE CASCADE,
    FOREIGN KEY (item_no) REFERENCES additional_item(item_no) ON DELETE CASCADE,
    PRIMARY KEY (booking_id, item_no)
);

CREATE TABLE crew (
    crew_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE flight_schedule_crew (
    flight_code INT NOT NULL,
    crew_id INT NOT NULL,
    assignment_date DATE NOT NULL,
    role VARCHAR(255) NOT NULL,
    FOREIGN KEY (flight_code) REFERENCES flight_schedule(flight_code),
    FOREIGN KEY (crew_id) REFERENCES crew(crew_id),
    PRIMARY KEY (flight_code, crew_id)
);