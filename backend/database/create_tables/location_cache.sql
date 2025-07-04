CREATE TABLE location_cache (
    id SERIAL PRIMARY KEY,
    country_code TEXT NOT NULL,
    top_tracks JSONB,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);