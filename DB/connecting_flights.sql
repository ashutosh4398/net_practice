WITH RECURSIVE FlightPath AS (
    SELECT 
        id,
        source_airport,
        destination_airport,
        source_airport as sp, 
        destination_airport as lp, 
        id as initial
    FROM flights
    WHERE source_airport = 'AirportA'
    
    UNION
    
    SELECT 
        f.id,
        f.source_airport, 
        f.destination_airport,
        fp.sp,
        f.destination_airport as lp,
        fp.initial
        
    FROM flights f
    JOIN FlightPath fp ON f.source_airport = fp.destination_airport
)

SELECT * FROM FlightPath where initial in (select initial from FlightPath where sp="AirportA" and lp="AirportE");