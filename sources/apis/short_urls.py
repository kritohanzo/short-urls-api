from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse
from sources.apis.dependencies import Session
from sources.schemas.short_urls import CreateShortUrlRequestSchema, ShortUrlSchema
from sources.services.short_urls import ShortUrlService


router = APIRouter()


@router.get(path='/short-urls/{slug}/', summary='Короткие URL', description='Перенаправление по SLUG')
async def redirect_by_slug(slug: str, session: Session):
    service = ShortUrlService(session=session)
    domain = await service.get(slug=slug)
    response = RedirectResponse(url=domain.source_url, status_code=status.HTTP_302_FOUND)
    return response


@router.get(path='/short-urls/', summary='Короткие URL', description='Получение коротких URL')
async def get_short_urls(session: Session) -> list[ShortUrlSchema]:
    service = ShortUrlService(session=session)
    domains = await service.all()
    schemas = [ShortUrlSchema(source_url=domain.source_url, short_url=domain.short_url) for domain in domains]
    return schemas


@router.post(path='/short-urls/', summary='Короткие URL', description='Создание короткого URL')
async def create_short_url(schema: CreateShortUrlRequestSchema, session: Session) -> ShortUrlSchema:
    service = ShortUrlService(session=session)
    domain = await service.create(source_url=schema.source_url)
    schema = ShortUrlSchema(short_url=domain.short_url, source_url=domain.source_url)
    return schema


