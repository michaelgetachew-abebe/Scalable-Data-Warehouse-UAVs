create table if not exists vehicles
(
id serial primary key,
track_id int not null,
vehicle_type varchar(500) NOT null,
traveled_d varchar(500) NOT null,
avg_speed float NOT null,
lat float NOT null,
lon float NOT null,
speed float NOT null,
loan_acc float NOT null,
lat_acc float NOT null,
record_time float NOT null
);