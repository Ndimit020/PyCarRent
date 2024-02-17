CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- Assuming hashing will be used
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(50),
    model VARCHAR(50),
    year YEAR,
    registration_number VARCHAR(50) NOT NULL UNIQUE,
    status ENUM('available', 'rented', 'maintenance') NOT NULL DEFAULT 'available',
    daily_rate DECIMAL(10, 2) NOT NULL
);

CREATE TABLE rentals (
    rental_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    vehicle_id INT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
    status ENUM('booked', 'active', 'completed', 'cancelled') NOT NULL DEFAULT 'booked',
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);


INSERT INTO users (username, password, email) VALUES
('john_doe', 'hashed_password1', 'john.doe@example.com'),
('jane_doe', 'hashed_password2', 'jane.doe@example.com');

INSERT INTO vehicles (make, model, year, registration_number, daily_rate) VALUES
('Toyota', 'Camry', 2020, 'ABC123', 50.00),
('Honda', 'Civic', 2019, 'XYZ789', 45.00);

INSERT INTO rentals (user_id, vehicle_id, start_date, end_date, total_cost) VALUES
(1, 1, '2024-01-01', '2024-01-05', 250.00),
(2, 2, '2024-01-02', '2024-01-06', 180.00);