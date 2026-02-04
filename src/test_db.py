from src.db import get_conn

def main():
    with get_conn() as conn:
        print(conn.execute("select 1;").fetchone())

if __name__ == "__main__":
    main()
