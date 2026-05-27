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
