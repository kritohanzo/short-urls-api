from dataclasses import dataclass, field

from sources.settings import settings


@dataclass(kw_only=True)
class ShortUrlDomain:
    id: int | None = None

    slug: str
    source_url: str

    visitors: int = field(default=0)

    @property
    def short_url(self) -> str:
        return f"{settings.server_url}/short-urls/{self.slug}/"
