##1View first records
SELECT * 
FROM hotel_bookings 
limit 10;
##2Count total bookings
SELECT 
COUNT(*) AS total_bookings
FROM hotel_bookings;
##3 Count cancelled and non-cancelled bookings
SELECT 
is_canceled,
COUNT(*) AS booking_count
FROM hotel_bookings
GROUP BY is_canceled;

##4 Overall cancellation rate
SELECT 
COUNT(*) AS total_bookings,
SUM(is_canceled) AS total_cancellation,
ROUND(SUM(is_canceled)*100.0/COUNT(*),2) AS cancellation_rate_percentage
FROM hotel_bookings;

##5 Cancellation rate by hotel type
SELECT hotel,
COUNT(*) AS total_bookings,
SUM(is_canceled) AS total_cancellations,
ROUND(SUM(is_canceled)*100.0/ COUNT(*),2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY hotel
ORDER BY cancellation_rate_percentage DESC;

##6 Cancellation rate by market segment
SELECT 
market_segment,
COUNT(*) AS total_bookings,
SUM(is_canceled) AS total_cancellations,
ROUND(SUM(is_canceled)*100.0/COUNT(*),2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY market_segment
ORDER BY cancellation_rate_percentage DESC;

##7 Cancellation rate by deposit type
SELECT 
deposit_type,
COUNT(*) AS total_bookings,
SUM(is_canceled) AS total_cancellations,
ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY deposit_type
ORDER BY cancellation_rate_percentage DESC;

##8 Cancellation rate by customer type
SELECT 
customer_type,
COUNT(*) AS total_bookings,
SUM(is_canceled) AS total_cancellations,
ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY customer_type
ORDER BY cancellation_rate_percentage DESC;


##9 Average Daily Rate by hotel type
SELECT 
hotel,
ROUND(AVG(adr), 2) AS average_daily_rate
FROM hotel_bookings
GROUP BY hotel
ORDER BY average_daily_rate DESC;

##10 Average Daily Rate by month
SELECT 
arrival_date_month,
ROUND(AVG(adr), 2) AS average_daily_rate
FROM hotel_bookings
GROUP BY arrival_date_month
ORDER BY average_daily_rate DESC;

##11 Month-wise booking volume
SELECT 
arrival_date_month,
COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY arrival_date_month
ORDER BY total_bookings DESC;

##12 Month-wise cancellations
SELECT 
arrival_date_month,
COUNT(*) AS total_bookings,
SUM(is_canceled) AS total_cancellations,
ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY arrival_date_month
ORDER BY cancellation_rate_percentage DESC;

##13. Seasonal pricing analysis
SELECT 
season,
COUNT(*) AS total_bookings,
ROUND(AVG(adr), 2) AS average_daily_rate,
ROUND(SUM(estimated_revenue), 2) AS estimated_revenue
FROM hotel_bookings
GROUP BY season
ORDER BY estimated_revenue DESC;

##14. Lead time category cancellation analysis
SELECT 
lead_time_category,
COUNT(*) AS total_bookings,
SUM(is_canceled) AS total_cancellations,
ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY lead_time_category
ORDER BY cancellation_rate_percentage DESC;

##15. Create lead time category directly in SQL
SELECT 
CASE
WHEN lead_time <= 7 THEN 'Last-Minute'
WHEN lead_time <= 30 THEN 'Short-Term'
WHEN lead_time <= 90 THEN 'Medium-Term'
ELSE 'Long-Term'
END AS lead_time_category,
COUNT(*) AS total_bookings,
SUM(is_canceled) AS total_cancellations,
ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY 
CASE
WHEN lead_time <= 7 THEN 'Last-Minute'
WHEN lead_time <= 30 THEN 'Short-Term'
WHEN lead_time <= 90 THEN 'Medium-Term'
ELSE 'Long-Term'
END
ORDER BY cancellation_rate_percentage DESC;

##16. Estimated revenue by hotel type
SELECT 
hotel,
ROUND(SUM(estimated_revenue), 2) AS total_estimated_revenue
FROM hotel_bookings
GROUP BY hotel
ORDER BY total_estimated_revenue DESC;

##17. Estimated revenue directly from ADR and stay duration
SELECT 
hotel,
ROUND(SUM(
CASE 
WHEN is_canceled = 0 
THEN adr * (stays_in_weekend_nights + stays_in_week_nights) ELSE 0 END), 2) AS total_estimated_revenue
FROM hotel_bookings
GROUP BY hotel
ORDER BY total_estimated_revenue DESC;

##18. Revenue by customer type
SELECT 
customer_type,
ROUND(SUM(estimated_revenue), 2) AS total_estimated_revenue
FROM hotel_bookings
GROUP BY customer_type
ORDER BY total_estimated_revenue DESC;

##19. Revenue by market segment
SELECT 
market_segment,
ROUND(SUM(estimated_revenue), 2) AS total_estimated_revenue
FROM hotel_bookings
GROUP BY market_segment
ORDER BY total_estimated_revenue DESC;

##20. Top 10 countries by bookings
SELECT 
country,
COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY country
ORDER BY total_bookings DESC
LIMIT 10;

##21. Top 10 countries by cancellations
SELECT 
    country,
    COUNT(*) AS total_bookings,
    SUM(is_canceled) AS total_cancellations,
    ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY country
HAVING COUNT(*) >= 100
ORDER BY total_cancellations DESC
LIMIT 10;
22. Repeated guest cancellation rate
SELECT 
    is_repeated_guest,
    COUNT(*) AS total_bookings,
    SUM(is_canceled) AS total_cancellations,
    ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY is_repeated_guest;
23. Special requests vs cancellation
SELECT 
    total_of_special_requests,
    COUNT(*) AS total_bookings,
    SUM(is_canceled) AS total_cancellations,
    ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY total_of_special_requests
ORDER BY total_of_special_requests;


##24. Parking requirement vs cancellation
SELECT 
    required_car_parking_spaces,
    COUNT(*) AS total_bookings,
    SUM(is_canceled) AS total_cancellations,
    ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage
FROM hotel_bookings
GROUP BY required_car_parking_spaces
ORDER BY required_car_parking_spaces;
25. Average lead time by booking status
SELECT 
    is_canceled,
    ROUND(AVG(lead_time), 2) AS average_lead_time
FROM hotel_bookings
GROUP BY is_canceled;


##26. ADR by cancellation status
SELECT 
    is_canceled,
    ROUND(AVG(adr), 2) AS average_daily_rate
FROM hotel_bookings
GROUP BY is_canceled;
27. Monthly revenue trend
SELECT 
    arrival_date_year,
    arrival_date_month,
    ROUND(SUM(estimated_revenue), 2) AS total_estimated_revenue
FROM hotel_bookings
GROUP BY arrival_date_year, arrival_date_month
ORDER BY arrival_date_year, total_estimated_revenue DESC;
28. Booking status label query
SELECT 
    CASE 
        WHEN is_canceled = 1 THEN 'Canceled'
        ELSE 'Not Canceled'
    END AS booking_status,
    COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY 
    CASE 
        WHEN is_canceled = 1 THEN 'Canceled'
        ELSE 'Not Canceled'
    END;


##29. Customer segmentation in SQL
SELECT 
    CASE 
        WHEN is_repeated_guest = 1 THEN 'Repeated Guest'
        WHEN lead_time <= 7 THEN 'Last-Minute Booker'
        WHEN lead_time > 90 THEN 'Early Planner'
        WHEN market_segment = 'Corporate' THEN 'Corporate Customer'
        ELSE 'Regular Customer'
    END AS customer_segment,
    COUNT(*) AS total_bookings,
    SUM(is_canceled) AS total_cancellations,
    ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage,
    ROUND(AVG(adr), 2) AS average_daily_rate
FROM hotel_bookings
GROUP BY 
    CASE 
        WHEN is_repeated_guest = 1 THEN 'Repeated Guest'
        WHEN lead_time <= 7 THEN 'Last-Minute Booker'
        WHEN lead_time > 90 THEN 'Early Planner'
        WHEN market_segment = 'Corporate' THEN 'Corporate Customer'
        ELSE 'Regular Customer'
    END
ORDER BY cancellation_rate_percentage DESC;


##30. Final business summary query
SELECT 
    COUNT(*) AS total_bookings,
    SUM(is_canceled) AS total_cancellations,
    ROUND(SUM(is_canceled) * 100.0 / COUNT(*), 2) AS cancellation_rate_percentage,
    ROUND(AVG(adr), 2) AS average_daily_rate,
    ROUND(SUM(estimated_revenue), 2) AS total_estimated_revenue
FROM hotel_bookings;
