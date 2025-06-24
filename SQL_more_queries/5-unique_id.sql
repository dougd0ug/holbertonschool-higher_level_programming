-- Create a table with an unique and not null id
CREATE TABLE IF NOT EXISTS unique_id(
    id DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
