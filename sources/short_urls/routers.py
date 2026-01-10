from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse

from sources.dependencies import Session
from sources.short_urls.exceptions import GenerateSlugException
from sources.short_urls.schemas import CreateShortUrlRequestSchema, ShortUrlSchema
from sources.short_urls.services import ShortUrlService

router = APIRouter()


@router.get(path="/short-urls/{slug}/", summary="Короткие URL", description="Перенаправление по SLUG")
async def redirect_by_slug(slug: str, session: Session):
    service = ShortUrlService(session=session)
    domain = await service.get(slug=slug, as_visitor=True)
    response = RedirectResponse(url=domain.source_url, status_code=status.HTTP_302_FOUND)
    return response


@router.get(path="/short-urls/", summary="Короткие URL", description="Получение коротких URL")
async def get_short_urls(session: Session) -> list[ShortUrlSchema]:
    service = ShortUrlService(session=session)
    domains = await service.all()

    schemas = [
        ShortUrlSchema(
            source_url=domain.source_url,
            short_url=domain.short_url,
            visitors=domain.visitors,
        )
        for domain in domains
    ]

    return schemas


@router.post(path="/short-urls/", summary="Короткие URL", description="Создание короткого URL")
async def create_short_url(data: CreateShortUrlRequestSchema, session: Session) -> ShortUrlSchema:
    service = ShortUrlService(session=session)

    try:
        domain = await service.create(source_url=data.source_url)
    except GenerateSlugException as exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=exception.message,
        )

    schema = ShortUrlSchema(
        short_url=domain.short_url,
        source_url=domain.source_url,
        visitors=domain.visitors,
    )

    return schema
