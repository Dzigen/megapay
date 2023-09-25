CREATE TABLE test (
    id serial PRIMARY KEY,
    text_d VARCHAR(100)
);

INSERT INTO test(text_d) VALUES('Hello, from DB!');