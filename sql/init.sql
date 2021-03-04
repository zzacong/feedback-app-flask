DROP DATABASE IF EXISTS "lexus";

CREATE DATABASE "lexus";

\connect "lexus";

DROP TABLE IF EXISTS "feedback";

CREATE TABLE "feedback" (
  id SERIAL PRIMARY KEY,
  customer VARCHAR(200) UNIQUE,
  dealer VARCHAR(200),
  rating INT,
  comments TEXT
);