CREATE TABLE IF NOT EXISTS cicd_test_event_db.banner_view (
  id INT AUTO_INCREMENT PRIMARY KEY,
  event_time DATETIME,
  banner_id INT,
  user_id INT
);
