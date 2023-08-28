class Phonebook:
    def __init__(self):
        self.entries = {"POLICIA": "190"}

    @staticmethod
    def validate_name(name: str) -> bool:
        invalid_list = ["!", "@", "%", "$", "#"]
        for invalid_char in invalid_list:
            if invalid_char in name:
                return False
        return True

    @staticmethod
    def validate_number(number: str) -> bool:
        if number.strip() == "":
            return False
        return True

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        if not Phonebook.validate_name(name):  # BUG: retorno com erro de
            return "Nome invalido"

        if not Phonebook.validate_number(number):  # BUG: erro de logica do tamanho
            return "Numero invalido"

        if name not in self.entries:
            self.entries[name] = number
            return "Numero adicionado"

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if not Phonebook.validate_name(name):  # BUG: retorno com erro de
            return "Nome invalido"

        if name in self.entries:  # BUG: Quebra ao buscar por nome inexistente
            return self.entries[name]
        else:
            None

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return "phonebook limpado"

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name not in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return sorted(self.entries)  # BUG: dict uses hash

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return self.entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return "Numero deletado"

    def change_number(self, name, number):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if name in self.entries:
            self.entries[name]=number
            return 'Numero alterado'
        return "Numero nao encontrado"

    def get_name_by_number(self, number):
        """
        Given a number return the name
        :param number: String with name
        :return: return the number for the given name
        """

        for entry_name, entry_number in self.entries.items():
            if   number == entry_number:
                return  entry_name
        return 'Nao encontrado'



