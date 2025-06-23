-- Computes the score average
ALTER TABLE second_table ADD COLUMN average float;
SET average = (SELECT AVG(score) FROM second_table);
