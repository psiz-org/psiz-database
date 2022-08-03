CREATE DATABASE IF NOT EXISTS psiz03;
USE psiz03;

CREATE TABLE IF NOT EXISTS participant (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    personal_id CHAR(255) UNIQUE NOT NULL,
    anonymous_id CHAR(255) UNIQUE NOT NULL,
    is_amt_worker_id INT UNSIGNED DEFAULT 0
);

CREATE TABLE IF NOT EXISTS domain_pz (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id36 VARCHAR(10) NOT NULL,
    label VARCHAR(255) NOT NULL,
    asset_count BIGINT UNSIGNED DEFAULT 0
);

CREATE TABLE IF NOT EXISTS design (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    project CHAR(255) NOT NULL,
    stimulus_set CHAR(255) DEFAULT 'NA',
    protocol CHAR(255) DEFAULT 'NA',
    factor_d CHAR(255) DEFAULT 'NA',
    factor_e CHAR(255) DEFAULT 'NA',
    UNIQUE KEY unique_id (project, stimulus_set, protocol, factor_d, factor_e)
);

CREATE TABLE IF NOT EXISTS sequence (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    anonymous_id CHAR(255) NOT NULL,
    design_id INT NOT NULL,
    time_begin TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    time_end TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    n_timestep INT NOT NULL DEFAULT -1,
    grade INT NOT NULL DEFAULT -1,
    is_exported INT NOT NULL DEFAULT 0,
    FOREIGN KEY (anonymous_id) REFERENCES participant(anonymous_id),
    FOREIGN KEY (design_id) REFERENCES design(id)
);

CREATE TABLE IF NOT EXISTS client_machine (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sequence_id INT NOT NULL,
    browser CHAR(128) NOT NULL,
    platform CHAR(128) NOT NULL,
    ipaddress CHAR(128),
    language_code CHAR(128) DEFAULT 'unknown',
    FOREIGN KEY (sequence_id)
        REFERENCES sequence(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS amazon_mechanical_turk (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sequence_id INT NOT NULL,
    hit_id CHAR(255) NOT NULL,
    assignment_id CHAR(255) NOT NULL,
    FOREIGN KEY (sequence_id)
        REFERENCES sequence(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS timestep (
    id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sequence_id INT NOT NULL,
    position INT NOT NULL,
    kind CHAR(255) NOT NULL,
    time_begin TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    time_end TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    response_time_ms INT UNSIGNED NOT NULL DEFAULT 0,
    -- grade_earnest INT NOT NULL DEFAULT -1,
    -- grade_primary INT NOT NULL DEFAULT -1,
    FOREIGN KEY (sequence_id)
        REFERENCES sequence(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS interaction (
    id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    timestep_id BIGINT NOT NULL,
    time_begin TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    kind CHAR(255) NOT NULL,
    info CHAR(255) NOT NULL,
    FOREIGN KEY (timestep_id)
        REFERENCES timestep(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS interaction_feedback (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    timestep_id BIGINT NOT NULL,
    time_begin TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    kind CHAR(255) NOT NULL,
    info TEXT,
    FOREIGN KEY (timestep_id)
        REFERENCES timestep(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS counter (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    counter_name CHAR(255) NOT NULL,
    counter_value INT NOT NULL DEFAULT 0
);
