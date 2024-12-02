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

INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '08:15:00', INTERVAL '2 Hours 15 Minutes', 1000, DATE '2024-11-30', 1
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '13:30:00', INTERVAL '5 Hours', 1000, DATE '2024-12-01', 2
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '06:45:00', INTERVAL '8 Hours 30 Minutes', 1000, DATE '2024-12-02', 3
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '10:00:00', INTERVAL '10 Hours 45 Minutes', 1000, DATE '2024-11-29', 4
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '15:20:00', INTERVAL '3 Hours 10 Minutes', 1000, DATE '2024-12-03', 5
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '19:45:00', INTERVAL '12 Hours 50 Minutes', 1000, DATE '2024-12-05', 6
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '23:30:00', INTERVAL '4 Hours 20 Minutes', 1000, DATE '2024-12-07', 7
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '04:00:00', INTERVAL '7 Hours', 1000, DATE '2024-11-28', 8
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '11:15:00', INTERVAL '6 Hours 45 Minutes', 1000, DATE '2024-12-06', 9
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '17:50:00', INTERVAL '9 Hours 30 Minutes', 1000, DATE '2024-11-30', 10
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '09:15:00', INTERVAL '2 Hours 15 Minutes', 1000, DATE '2024-11-30', 1
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '01:00:00', INTERVAL '2 Hours', 1000, DATE '2024-12-01', 1
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '13:00:00', INTERVAL '2 Hours', 1000, DATE '2024-12-01', 1
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '20:00:00', INTERVAL '2 Hours', 1000, DATE '2024-12-01', 1
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '08:15:00', INTERVAL '2 Hours 15 Minutes', 1000, DATE '2024-12-04', 1
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '09:30:00', INTERVAL '3 Hours', 1200, DATE '2024-12-05', 2
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '12:45:00', INTERVAL '1 Hour 45 Minutes', 800, DATE '2024-12-06', 3
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '15:20:00', INTERVAL '2 Hours 30 Minutes', 1500, DATE '2024-12-07', 4
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '18:00:00', INTERVAL '4 Hours', 2000, DATE '2024-12-08', 5
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '06:00:00', INTERVAL '3 Hours 15 Minutes', 1300, DATE '2024-12-09', 1
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '07:45:00', INTERVAL '2 Hours', 1100, DATE '2024-12-10', 2
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '14:10:00', INTERVAL '1 Hour 30 Minutes', 900, DATE '2024-12-11', 3
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '20:30:00', INTERVAL '5 Hours', 2500, DATE '2024-12-12', 4
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '10:20:00', INTERVAL '2 Hours 45 Minutes', 1400, DATE '2024-12-13', 5
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '11:30:00', INTERVAL '3 Hours 30 Minutes', 1600, DATE '2024-12-14', 1
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '17:45:00', INTERVAL '4 Hours 15 Minutes', 2100, DATE '2024-12-15', 2
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '08:25:00', INTERVAL '2 Hours 10 Minutes', 1050, DATE '2024-12-16', 3
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '13:35:00', INTERVAL '1 Hour 20 Minutes', 800, DATE '2024-12-17', 4
);
INSERT INTO flight_schedule (departure_time, duration, flight_cost, departure_date, route_id) VALUES (
    TIME '21:00:00', INTERVAL '5 Hours 30 Minutes', 2700, DATE '2024-12-18', 5
);

INSERT INTO additional_item (item_name, cost) VALUES ('Additional Baggage Allowance (5kg)', 237.0);
INSERT INTO additional_item (item_name, cost) VALUES ('Terminal Fees', 273.0);
INSERT INTO additional_item (item_name, cost) VALUES ('Travel Insurance', 208.0);