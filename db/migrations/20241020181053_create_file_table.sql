-- migrate:up
CREATE TABLE "files_record"
(
    id integer GENERATED ALWAYS AS identity PRIMARY KEY,
    record_id integer not null,
    name varchar not null,
    bird_date DATE not null,
    email varchar not null,
    amount float not null,

    UNIQUE(record_id)
);
-- migrate:down

