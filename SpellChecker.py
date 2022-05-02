from ErrorFinderFixer import ErrorFinderFixer
from Suggester import Suggester


class SpellChecker:
    def __init__(self, filename):
        self.filename = filename
        self.finder_fixer = ErrorFinderFixer(filename)
        self.errors = self.finder_fixer.get_errors()
        self.suggester = Suggester(self.finder_fixer.english)

    def spellcheck(self):
        print('\n***Spell-checking file***\n')
        suggestions_list = []
        if len(self.errors) == 0:
            print('***No errors found! Exiting...***')
            return
        for error in self.errors:
            suggestions = self.suggester.get_suggestions(self.finder_fixer.prep_word(error))
            suggestions_list.append(suggestions)
        while len(self.errors) > 0:
            try:
                error_count = 1
                curr_suggestion = 0
                print('Errors:')
                for error in self.errors:
                    print('[', error_count, '.] ', error, sep='')
                    error_count += 1
                    suggestion_count = 1
                    for suggestion in suggestions_list[curr_suggestion]:
                        print('\t', suggestion_count, '. ', suggestion, sep='')
                        suggestion_count += 1
                    curr_suggestion += 1
                print()
                word_select = int(input('Enter the error to correct, or 0 to finish: '))
                if word_select == 0:
                    break
                correct_select = int(input('Enter suggestion to use, or 0 to input custom '
                                           'word, or -1 to ignore error: '))
                if correct_select == 0:
                    replacement = input('Enter word to use as replacement: ')
                    self.finder_fixer.fix_error(self.errors[word_select-1], replacement)
                elif correct_select > 0:
                    self.finder_fixer.fix_error(self.errors[word_select-1],
                                                suggestions_list[word_select-1][correct_select-1])
                del self.errors[word_select-1]
                del suggestions_list[word_select-1]
            except IndexError:
                print('\n***Inputted invalid error or suggestion #, try again!***\n')
            except ValueError:
                print('\n***Inputted invalid type as error or suggestion, try again!***\n')
        if len(self.errors) == 0:
            print('\n***All errors in file fixed! Exiting...***')
        else:
            print('\n***Exiting...***')
