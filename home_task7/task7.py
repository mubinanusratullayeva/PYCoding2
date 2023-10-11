class Person:
    def __init__(self, name, birth_year, nation):
        self._name = name
        self.__birth_year = birth_year
        self.__nation = nation

    @property
    def year_of_birth(self):
        return self.__birth_year

    @property
    def nation(self):
        return self.__nation


class Person1:
    def __init__(self, name, birth_year, nation):
        self._name = name
        self.__birth_year = birth_year
        self.__nation = nation

    @property
    def year_of_birth(self):
        return self.__birth_year

    @property
    def nation(self):
        return self.__nation

    class Person2:
        def __init__(self, name, birth_year, nation):
            self._name = name
            self.__birth_year = birth_year
            self.__nation = nation

        @property
        def year_of_birth(self):
            return self.__birth_year

        @property
        def nation(self):
            return self.__nation


class Person3:
    def __init__(self, name, birth_year, nation):
        self._name = name
        self.__birth_year = birth_year
        self.__nation = nation

    @property
    def year_of_birth(self):
        return self.__birth_year

    @property
    def nation(self):
        return self.__nation