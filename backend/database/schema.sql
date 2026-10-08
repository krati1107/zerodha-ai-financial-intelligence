-- Zerodha AI Financial Intelligence Platform — Database Schema

CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    portfolio_id VARCHAR(100),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS insights (
    id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES jobs(id),
    summary TEXT,
    confidence VARCHAR(20),
    validation_status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS recommendation_cards (
    id SERIAL PRIMARY KEY,
    insight_id INTEGER REFERENCES insights(id),
    category VARCHAR(50),
    signal TEXT,
    rationale TEXT,
    metric VARCHAR(200),
    confidence FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS audit_logs (
    id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES jobs(id),
    model_version VARCHAR(100),
    prompt_version VARCHAR(50),
    tool_calls JSONB,
    validation_result VARCHAR(50),
    reviewer_decision VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_feedback (
    id SERIAL PRIMARY KEY,
    insight_id INTEGER REFERENCES insights(id),
    feedback_type VARCHAR(20),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
