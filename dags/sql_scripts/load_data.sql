COPY vehicles(track_id, vehicle_type, traveled_d, avg_speed, lat, lon, speed, loan_acc, lat_acc, record_time)
FROM './location1.csv'
DELIMITER ','
CSV HEADER;