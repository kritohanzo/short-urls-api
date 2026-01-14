from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse

from sources.dependencies import Session
from sources.short_urls.exceptions import GenerateSlugException
from sources.short_urls.repositories import ShortUrlRepository
from sources.short_urls.schemas import ShortUrlSchema
from sources.short_urls.services import ShortUrlService

router = APIRouter(prefix='/short-urls', tags=['Короткие URL'])


@router.get(path='/{slug}', summary='Перенаправление по короткому URL')
async def redirect_by_slug(slug: str, session: Session) -> RedirectResponse:
    repository = ShortUrlRepository(session=session)
    service = ShortUrlService(repository=repository)

    short_url = await service.get(slug=slug)
    await service.visit(short_url=short_url)

    return RedirectResponse(url=short_url.source_url, status_code=status.HTTP_302_FOUND)


@router.get(path='/', summary='Получение коротких URL')
async def get_short_urls(session: Session) -> list[ShortUrlSchema]:
    repository = ShortUrlRepository(session=session)
    service = ShortUrlService(repository=repository)

    short_urls = await service.all()

    return [ShortUrlSchema.model_validate(obj=short_url) for short_url in short_urls]


@router.post(path='/', summary='Создание короткого URL')
async def create_short_url(source_url: str, session: Session) -> ShortUrlSchema:
    repository = ShortUrlRepository(session=session)
    service = ShortUrlService(repository=repository)

    try:
        short_url = await service.create(source_url=source_url)
    except GenerateSlugException as exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=exception.message,
        )

    return ShortUrlSchema.model_validate(obj=short_url)
