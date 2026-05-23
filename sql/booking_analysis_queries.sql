-- 1. Monthly cancellation and pricing trend
SELECT
    arrival_date_month_number,
    arrival_date_month,
    COUNT(*) AS bookings,
    SUM(is_canceled) AS cancellations,
    AVG(is_canceled) AS cancellation_rate,
    AVG(adr) AS average_adr,
    SUM(revenue_realized) AS realized_revenue
FROM hotel_bookings_clean
GROUP BY arrival_date_month_number, arrival_date_month
ORDER BY arrival_date_month_number;

-- 2. High-risk market segments
SELECT
    market_segment,
    COUNT(*) AS bookings,
    AVG(is_canceled) AS cancellation_rate,
    AVG(lead_time) AS average_lead_time,
    AVG(adr) AS average_adr
FROM hotel_bookings_clean
GROUP BY market_segment
HAVING COUNT(*) >= 50
ORDER BY cancellation_rate DESC;

