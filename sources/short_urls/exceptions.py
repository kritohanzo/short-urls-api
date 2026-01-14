class ShortUrlException(Exception):
    message: str


class GenerateSlugException(ShortUrlException):
    message: str = 'Ошибка при генерации SLUG для короткого URL'
