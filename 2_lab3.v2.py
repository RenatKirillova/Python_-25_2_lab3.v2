class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name должен быть непустой строкой")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("author должен быть непустой строкой")

        self._name = name.strip()
        self._author = author.strip()

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("pages должен быть int")
        if value <= 0:
            raise ValueError("pages должен быть > 0")
        self._pages = value

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.pages!r})")


class AudioBook(Book):
    """Аудиокнига."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("duration должен быть числом (int или float)")
        value = float(value)
        if value <= 0:
            raise ValueError("duration должен быть > 0")
        self._duration = value

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.duration!r})")