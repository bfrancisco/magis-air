CREATE DATABASE magis_air;
\c magis_air
CREATE TABLE city (
    name VARCHAR(255) NOT NULL PRIMARY KEY,
    country VARCHAR(255) NOT NULL 
);

INSERT INTO city (name, country) VALUES ('Cebu', 'Philippines');
INSERT INTO city (name, country) VALUES ('Tokyo', 'Japan');
INSERT INTO city (name, country) VALUES ('Paris', 'France');
INSERT INTO city (name, country) VALUES ('New York', 'United States');
INSERT INTO city (name, country) VALUES ('Sydney', 'Australia');
INSERT INTO city (name, country) VALUES ('Cape Town', 'South Africa');
INSERT INTO city (name, country) VALUES ('Rio de Janeiro', 'Brazil');
INSERT INTO city (name, country) VALUES ('Mumbai', 'India');
INSERT INTO city (name, country) VALUES ('Toronto', 'Canada');
INSERT INTO city (name, country) VALUES ('Berlin', 'Germany');
INSERT INTO city (name, country) VALUES ('Beijing', 'China');

CREATE TABLE route (
    route_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    distance FLOAT(2) NOT NULL,
    city_origin VARCHAR(255) NOT NULL,
    city_destination VARCHAR(255) NOT NULL,
    UNIQUE (city_destination, city_origin),
    FOREIGN KEY (city_origin) REFERENCES city(name),
    FOREIGN KEY (city_destination) REFERENCES city(name)
);

INSERT INTO route (city_origin, city_destination, distance) VALUES ('Cebu', 'Tokyo', 3000);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Cebu', 'Paris', 11300);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Cebu', 'New York', 13800);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Tokyo', 'Sydney', 7800);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Tokyo', 'Cape Town', 14500);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Tokyo', 'Rio de Janeiro', 18500);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Paris', 'Sydney', 17000);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Paris', 'Cape Town', 9400);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Paris', 'Berlin', 880);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Paris', 'Beijing', 8200);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('New York', 'Rio de Janeiro', 7700);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('New York', 'Toronto', 550);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('New York', 'Beijing', 11000);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Sydney', 'Mumbai', 10400);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Cape Town', 'Rio de Janeiro', 6700);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Rio de Janeiro', 'Mumbai', 14600);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Rio de Janeiro', 'Toronto', 8150);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Rio de Janeiro', 'Berlin', 9800);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Rio de Janeiro', 'Beijing', 17200);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Mumbai', 'Toronto', 12500);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Mumbai', 'Berlin', 6200);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Mumbai', 'Beijing', 3800);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Toronto', 'Berlin', 6400);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Toronto', 'Beijing', 10500);
INSERT INTO route (city_origin, city_destination, distance) VALUES ('Berlin', 'Beijing', 7400);


CREATE TABLE flight_schedule (
    flight_code SERIAL NOT NULL UNIQUE PRIMARY KEY,
    departure_time TIME NOT NULL,
    arrival_time TIME GENERATED ALWAYS AS (departure_time + duration) STORED,
    duration INTERVAL NOT NULL,
    departure_date DATE NOT NULL,
    route_id INT NOT NULL,
    FOREIGN KEY (route_id) REFERENCES route(route_id)
);

INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '08:15:00', INTERVAL '2 Hours 15 Minutes', DATE '2024-11-30', 1
);
INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '13:30:00', INTERVAL '5 Hours', DATE '2024-12-01', 2
);
INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '06:45:00', INTERVAL '8 Hours 30 Minutes', DATE '2024-12-02', 3
);
INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '10:00:00', INTERVAL '10 Hours 45 Minutes', DATE '2024-11-29', 4
);
INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '15:20:00', INTERVAL '3 Hours 10 Minutes', DATE '2024-12-03', 5
);
INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '19:45:00', INTERVAL '12 Hours 50 Minutes', DATE '2024-12-05', 6
);
INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '23:30:00', INTERVAL '4 Hours 20 Minutes', DATE '2024-12-07', 7
);
INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '04:00:00', INTERVAL '7 Hours', DATE '2024-11-28', 8
);
INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '11:15:00', INTERVAL '6 Hours 45 Minutes', DATE '2024-12-06', 9
);
INSERT INTO flight_schedule (departure_time, duration, departure_date, route_id) VALUES (
    TIME '17:50:00', INTERVAL '9 Hours 30 Minutes', DATE '2024-11-30', 10
);


CREATE TABLE passenger (
    passenger_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    gender VARCHAR(6) NOT NULL,
    CHECK (gender IN ('Male', 'Female'))
);

INSERT INTO passenger (name, birth_date, gender) VALUES ('John Smith', DATE '1985-06-15', 'Male');
INSERT INTO passenger (name, birth_date, gender) VALUES ('Emily Davis', DATE '1992-03-22', 'Female');
INSERT INTO passenger (name, birth_date, gender) VALUES ('Michael Johnson', DATE '1978-11-10', 'Male');
INSERT INTO passenger (name, birth_date, gender) VALUES ('Sophia Martinez', DATE '2000-08-05', 'Female');
INSERT INTO passenger (name, birth_date, gender) VALUES ('Daniel Kim', DATE '1990-12-30', 'Male');
INSERT INTO passenger (name, birth_date, gender) VALUES ('Olivia Brown', DATE '1988-09-17', 'Female');
INSERT INTO passenger (name, birth_date, gender) VALUES ('Ethan Wilson', DATE '2003-07-08', 'Male');
INSERT INTO passenger (name, birth_date, gender) VALUES ('Isabella Lee', DATE '1995-05-25', 'Female');
INSERT INTO passenger (name, birth_date, gender) VALUES ('Alexander Taylor', DATE '1982-02-13', 'Male');
INSERT INTO passenger (name, birth_date, gender) VALUES ('Mia Clark', DATE '1999-04-18', 'Female');

CREATE TABLE booking (
    booking_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    booking_date DATE NOT NULL,
    total_cost FLOAT(2),
    passenger_id INT NOT NULL,
    FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id),
    flight_code INT NOT NULL,
    FOREIGN KEY (flight_code) REFERENCES flight_schedule(flight_code)
);

CREATE TABLE crew (
    crew_id SERIAL NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE additional_item(
    item_name VARCHAR(255) NOT NULL,
    booking_id INT NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES booking(booking_id) ON DELETE CASCADE,
    PRIMARY KEY (item_name, booking_id)
);

CREATE TABLE booking_flight_schedule(
    booking_id INT NOT NULL,
    flight_code INT NOT NULL,
    flight_type VARCHAR(255) NOT NULL,
    flight_cost FLOAT(2) NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES booking(booking_id),
    FOREIGN KEY (flight_code) REFERENCES flight_schedule(flight_code),
    PRIMARY KEY (booking_id, flight_code)
);

CREATE TABLE booking_additional_item(
    booking_id INT NOT NULL,
    item_name VARCHAR(255) NOT NULL, 
    qty INT NOT NULL,
    cost FLOAT(2) NOT NULL,
    FOREIGN KEY (booking_id, item_name) REFERENCES additional_item(booking_id, item_name) ON DELETE CASCADE,
    PRIMARY KEY (booking_id, item_name)
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