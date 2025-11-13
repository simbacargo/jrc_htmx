CREATE DATABASE jrcdb;
GRANT ALL PRIVILEGES ON DATABASE jrcdb TO testuser;

GRANT ALL PRIVILEGES ON SCHEMA public TO testuser;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO testuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO testuser;

-- Grant usage and create permissions on the public schema
GRANT USAGE, CREATE ON SCHEMA public TO testuser;

-- Grant all privileges on all tables in the public schema
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO testuser;

-- Grant all privileges on all sequences in the public schema (important for auto-increment fields)
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO testuser;
