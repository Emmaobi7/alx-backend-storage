-- script for index

-- first letter of name and scorte
CREATE INDEX idx_name_first_score ON names(name(1), score);
