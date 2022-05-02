alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


class Suggester:
    def __init__(self, english):
        self.english = english

    def get_suggestions(self, word):
        suggestions = self._add_letter(word)
        if len(word) < 8:
            suggestions.extend(self._check_perms(word))
        suggestions.extend(self._replace_letter(word))
        suggestions.extend(self._double_letter(word))
        suggestions.extend(self._split_word(word))
        suggestions = list(set(suggestions))
        if len(suggestions) > 10:
            suggestions = suggestions[:10]
        return suggestions

    def _add_letter(self, word):
        suggestions = []
        for i in range(len(word) + 1):
            for char in alphabet:
                if word[:i] + char + word[i:] in self.english:
                    suggestions.append(word[:i] + char + word[i:])
        return suggestions

    def _check_perms(self, word):
        suggestions = []
        perms = Suggester._get_perms(word)
        for perm in perms:
            if perm in self.english:
                suggestions.append(perm)
        return suggestions

    def _replace_letter(self, word):
        suggestions = []
        for i in range(len(word) + 1):
            for char in alphabet:
                if word[:i] + char + word[i+1:] in self.english:
                    suggestions.append(word[:i] + char + word[i+1:])
        return suggestions

    def _double_letter(self, word):
        suggestions = []
        for i in range(len(word) - 1):
            if word[i] == word[i+1]:
                if word[:i] + word[i+1:] in self.english:
                    suggestions.append(word[:i] + word[i+1:])
        return suggestions

    def _split_word(self, word):
        suggestions = []
        for i in range(1, len(word)):
            if (word[:i] in self.english) and (word[i:] in self.english):
                suggestions.append(word[:i] + ' ' + word[i:])
        return suggestions

    @staticmethod
    def _get_perms(word):
        if len(word) == 1:
            return word
        perms = []
        for piece in Suggester._get_perms(word[1:]):
            for i in range(len(word)):
                perms.append(piece[:i] + word[:1] + piece[i:])
        return perms
