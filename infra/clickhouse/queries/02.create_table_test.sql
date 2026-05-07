USE cicd_test_event_db;
CREATE TABLE IF NOT EXISTS banner_view (
    event_time DateTime,
    banner_id UInt16,
    user_id UInt64
)
ENGINE = MergeTree()
ORDER BY event_time;