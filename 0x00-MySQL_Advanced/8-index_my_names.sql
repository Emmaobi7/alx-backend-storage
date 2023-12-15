-- script for index

-- firts letter of name
CREATE INDEX idx_name_first ON names(name(1));
