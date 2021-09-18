import abc

from liku_backend.birthday.domain.birthday import Birthday


class BirthdayRepository(abc.ABC):
    @abc.abstractmethod
    def store(self, birthday: Birthday):
        pass
