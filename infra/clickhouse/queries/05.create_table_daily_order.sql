USE analytics;
CREATE TABLE IF NOT EXISTS daily_order (
    date_ Date,
    order_count UInt64
)
ENGINE = MergeTree()
ORDER BY date_;