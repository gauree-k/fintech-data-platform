create schema if not exists raw;
create schema if not exists wh;

-- Raw tables (landing zone)
create table if not exists raw.customers (
  customer_id uuid primary key,
  signup_date date not null,
  country text not null
);

create table if not exists raw.merchants (
  merchant_id uuid primary key,
  category text not null,
  risk_tier text not null
);

create table if not exists raw.transactions (
  tx_id uuid primary key,
  customer_id uuid not null,
  merchant_id uuid not null,
  tx_time timestamptz not null,
  amount numeric(12,2) not null check (amount > 0),
  currency text not null,
  status text not null check (status in ('approved','declined'))
);

-- Curated star schema
create table if not exists wh.dim_customer (
  customer_sk bigserial primary key,
  customer_id uuid unique not null,
  signup_date date not null,
  country text not null
);

create table if not exists wh.dim_merchant (
  merchant_sk bigserial primary key,
  merchant_id uuid unique not null,
  category text not null,
  risk_tier text not null
);

create table if not exists wh.fact_transaction (
  tx_id uuid primary key,
  customer_sk bigint not null references wh.dim_customer(customer_sk),
  merchant_sk bigint not null references wh.dim_merchant(merchant_sk),
  tx_time timestamptz not null,
  amount numeric(12,2) not null check (amount > 0),
  currency text not null,
  status text not null check (status in ('approved','declined'))
);

create index if not exists idx_fact_tx_time on wh.fact_transaction(tx_time);
create index if not exists idx_fact_customer on wh.fact_transaction(customer_sk);
create index if not exists idx_fact_merchant on wh.fact_transaction(merchant_sk);
