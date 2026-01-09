class ShortUrlServiceException(Exception):
    message: str


class GenerateSlugException(ShortUrlServiceException):
    message: str = 'Ошибка при генерации SLUG для короткого URL'