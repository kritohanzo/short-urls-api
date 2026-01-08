from dataclasses import dataclass


@dataclass(kw_only=True)
class ShortUrlDomain:
    id: int | None = None
    slug: str
    source_url: str

    @property
    def short_url(self) -> str:
        return f"http://localhost:8000/short-urls/{self.slug}/"
