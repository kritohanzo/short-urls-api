from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from sources.models.bases import Base


class ShortUrlModel(Base):
    __tablename__ = "short_urls"

    id: Mapped[int] = mapped_column(primary_key=True)

    slug: Mapped[str]
    source_url: Mapped[str]

    visitors: Mapped[int] = mapped_column(server_default=text("0"))
