CREATE TABLE IF NOT EXISTS phone_numbers (
  id SERIAL PRIMARY KEY,
  phone_e164 TEXT NOT NULL UNIQUE,        
  active BOOLEAN NOT NULL DEFAULT TRUE,   
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS daily_message_log (
  id SERIAL PRIMARY KEY,
  phone_id INT NOT NULL REFERENCES phone_numbers(id) ON DELETE CASCADE,
  template_name TEXT NOT NULL,
  send_date DATE NOT NULL,                
  status TEXT NOT NULL,
  provider_message_id TEXT,
  error_text TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(phone_id, template_name, send_date)  -- enforces "once per day"
);
