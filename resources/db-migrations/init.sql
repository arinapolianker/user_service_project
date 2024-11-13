DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id INT(11) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(300) NOT NULL DEFAULT '',
    last_name VARCHAR(300) NOT NULL DEFAULT '',
    email VARCHAR(300) NOT NULL DEFAULT '',
    age INT(3) NOT NULL,
    address VARCHAR(300) NOT NULL DEFAULT '',
    joining_date DATE NOT NULL,
    registered BOOLEAN DEFAULT TRUE NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO users (id, first_name, last_name, email, age, address, joining_date, registered)
VALUES
    (1, 'Alice', 'Johnson', 'alice.johnson@example.com', 28, '123 Elm St, Springfield', '2023-01-15', 1),
    (2, 'Bob', 'Smith', 'bob.smith@example.com', 34, '456 Maple Ave, Riverdale', '2022-11-20', 1),
    (3, 'Catherine', 'Brown', 'catherine.brown@example.com', 26, '789 Oak Dr, Westfield', '2023-06-01', 1),
    (4, 'David', 'Wilson', 'david.wilson@example.com', 40, '101 Pine Ln, Center ville', '2021-09-10', 0),
    (5, 'Ella', 'Taylor', 'ella.taylor@example.com', 31, '202 Birch Blvd, Lakeview', '2022-12-25', 1),
    (6, 'Frank', 'Moore', 'frank.moore@example.com', 45, '303 Cedar Ct, Hilton', '2020-08-15', 0);
