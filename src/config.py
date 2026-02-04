import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class PGConfig:
    host: str = os.getenv("PG_HOST", "localhost")
    port: int = int(os.getenv("PG_PORT", "5432"))
    database: str = os.getenv("PG_DATABASE", "fintech")
    user: str = os.getenv("PG_USER", "dev")
    password: str = os.getenv("PG_PASSWORD", "dev_password")

    @property
    def dsn(self) -> str:
        return (
            f"host={self.host} port={self.port} dbname={self.database} "
            f"user={self.user} password={self.password}"
        )
