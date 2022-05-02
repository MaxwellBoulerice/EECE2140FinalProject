class ErrorFinderFixer:
    def __init__(self, filename):
        self.filename = filename
        self.words = []
        self.english = []
        try:
            with open('engmix.txt') as eng:
                for line in eng:
                    self.english.append(line.strip())
        except FileNotFoundError:
            print('Dictionary file \"engmix.txt\" not found! please include in current directory.')
        while len(self.words) == 0:
            try:
                with open(self.filename) as file:
                    for line in file:
                        for word in line.strip().split():
                            self.words.append(word)
            except FileNotFoundError:
                self.filename = input('File not found! Input a different name/path or enter \"EXIT\" to exit: ')
                if self.filename == 'EXIT':
                    quit()

    def get_errors(self):
        errors = []
        for word in self.words:
            test = self.prep_word(word)
            if not(test in self.english):
                errors.append(word)
        return errors

    def fix_error(self, error, replacement):
        if error[0].isupper():
            x = error[0]
            error = self.prep_word(error)
            error = x + error[1:]
            replacement = replacement.capitalize()
        else:
            error = self.prep_word(error)
        with open(self.filename) as file:
            text = file.read()
            text = text.replace(error, replacement)
        with open(self.filename, 'w') as file:
            file.write(text)

    @staticmethod
    def prep_word(word):
        word = word.lower()
        punc = '''“’”—!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        for ele in punc:
            word = word.replace(ele, '')
        return word
