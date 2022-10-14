#!/usr/bin/env python
# coding: utf-8
# Κώδικας κλάσεων της εφαρμογής

import random as rn
import itertools as it
import json as js


class SakClass:
    def __init__(self):

        self.number_of_letters_left = 102
        self.letters = {}
        self.letter_dictionary_keys = []
        self.letters_that_cannot_be_used_anymore = []

    def __repr__(self):
        return f'Class: {self.__class__}, letter_number:{self.number_of_letters_left},letter_dict{self.letters},' \
               f'letters_that_cannot_be_used:{self.letters_that_cannot_be_used_anymore}, ' \
               f'letter_keys:{self.letter_dictionary_keys}'

    # Ετοιμασία για το σακουλάκι με τα γράμματα
    def randomize_sak(self):
        self.letters = {'Α': [12, 1], 'Β': [1, 8], 'Γ': [2, 4], 'Δ': [2, 4], 'Ε': [8, 1],
                        'Ζ': [1, 10], 'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1], 'Κ': [4, 2],
                        'Λ': [3, 3], 'Μ': [3, 3], 'Ν': [6, 1], 'Ξ': [1, 10], 'Ο': [9, 1],
                        'Π': [4, 2], 'Ρ': [5, 2], 'Σ': [7, 1], 'Τ': [8, 1], 'Υ': [4, 2],
                        'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]}

        self.letter_dictionary_keys = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π',
                                       'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']

    # Ο παίκτης παίρνει γράμματα μέσα από το σακουλάκι
    def getletters(self, number_of_letters):
        random_letter_list = []
        letter_to_check = -1
        if number_of_letters == 0:
            return random_letter_list
        for i in range(number_of_letters):
            see_if_letter_can_be_selected = -1

            while see_if_letter_can_be_selected == -1:
                letter_to_check = self.letter_dictionary_keys[rn.randint(0, 23)]
                see_if_letter_can_be_selected = self.check_if_letter_can_be_selected(letter_to_check)

            random_letter_list.append(letter_to_check)
            self.decrease_number_of_letters()
            self.decrease_letter_appearances_in_sak(letter_to_check)
            self.check_if_letter_cannot_be_used_anymore(letter_to_check)
        rn.shuffle(random_letter_list)
        return random_letter_list

    def decrease_number_of_letters(self):
        self.number_of_letters_left -= 1

    def increase_number_of_letters(self, number_of_letters):
        self.number_of_letters_left += number_of_letters

    def decrease_letter_appearances_in_sak(self, letter):
        self.letters[letter][0] -= 1

    def increase_letter_appearances_in_sak(self, letter):
        self.letters[letter][0] += 1

    def check_if_letter_can_be_selected(self, letter):
        if letter in self.letters_that_cannot_be_used_anymore:
            return -1
        else:
            return letter

    def check_if_letter_cannot_be_used_anymore(self, letter):
        if self.letters[letter][0] == 0:
            self.letters_that_cannot_be_used_anymore.append(letter)

    def define_how_many_letters_can_be_taken_from_sak(self):
        return self.number_of_letters_left

    def show_number_of_letters_in_sak(self):
        print('\nΤα γράμματα που υπάρχουν στο σακουλάκι είναι:', self.number_of_letters_left)

    # Επιστρέφει τα γράμματα που δε χρησιμοποιήθηκαν από τον παίκτη
    def putbackletters(self, letters_to_return):
        for letter in letters_to_return:
            self.increase_letter_appearances_in_sak(letter)
            if letter in self.letters_that_cannot_be_used_anymore:
                self.letters_that_cannot_be_used_anymore.remove(letter)
        self.increase_number_of_letters(len(letters_to_return))


class Player:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.letters = []

    @staticmethod
    def score_decorator(function):
        def show_s(self):
            print()
            print(self.name, ',το Σκορ σου είναι:', end=' ')
            function(self)

        return show_s

    @staticmethod
    def final_score_decorator(function):
        def show_f_s(self):
            print(self.name, ': το τελικό σου σκορ είναι:', end=' ')
            function(self)

        return show_f_s

    def show_letters(self):
        print('\nΤα γράμματα που έχεις στη διάθεσή σου είναι:')
        print(self.letters)

    def increase_score(self, points_of_word):
        self.score += points_of_word

    def __repr__(self):
        return f'Class: {self.__class__}, name:{self.name}, score:{self.score}, letters: {self.letters}'


class Human(Player):
    def __init__(self):
        super().__init__()
        self.value_of_letters = []

    @Player.score_decorator
    def show_score(self):
        print(self.score)

    @Player.final_score_decorator
    def show_final_score(self):
        print(3 * '*', self.score, 3 * '*')

    def show_letters(self):
        print('\nΤα γράμματα που έχεις στη διάθεσή σου μαζί με την αξία τους είναι:')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        for index, letter in enumerate(self.letters):
            print(letter, self.value_of_letters[index], sep=':', end=' ')
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')

    def increase_score(self, points_of_word):
        super().increase_score(points_of_word)
        print('Τώρα το Σκορ σου είναι:', self.score)

    def __repr__(self):
        return f'Class: {self.__class__}, name:{self.name}, score:{self.score}, letters:{self.letters}, ' \
               f'value_of_letters:{self.value_of_letters}'

    def check_if_letters_are_right_in_word(self, word):
        letter_list_to_string = ''.join(self.letters)
        return all(letter_list_to_string.count(letter) >= word.count(letter) for letter in word)

    def remove_letters_of_word(self, word_without_spaces):
        for letter in word_without_spaces:
            self.letters.remove(letter)

    def clear_list_with_values_of_letters(self):
        self.value_of_letters.clear()

    def play(self):
        word = input('\nΉρθε η ώρα να βρεις μια λέξη: ')

        # Αφαιρούνται τα κενά στην αρχή και το τέλος που ίσως έχει εισαγάγει ο παίκτης
        word_no_spaces = word.strip()

        # Έλεγχος της ορθότητας των γραμμάτων που έδωσε ο παίκτης
        while True:
            if self.check_if_letters_are_right_in_word(word_no_spaces):

                # Εάν ο παίκτης εισαγάγει την κενή λέξη, εμφανίζεται μήνυμα λάθους
                if word_no_spaces == '':
                    print('Έχεις πατήσει Enter δίχως να βάλεις κάποια λέξη... Ξαναπροσπάθησε!')
                    word = input('\nΠροσπάθησε να σκεφτείς ξανά μια λέξη: ')
                    word_no_spaces = word.strip()

                else:
                    print('\nΈχεις αξιοποιήσει σωστά τα γράμματά σου,τώρα θα περιμένεις να ελέγξω αν η λέξη υπάρχει στο'
                          ' μεγάλο λεξικό του Scrabble Master!')
                    break

            elif word_no_spaces == 'p' or word_no_spaces == 'q':
                return word_no_spaces

            else:
                print('\nΔεν έχεις χρησιμοποιήσει τα γράμματα που σου έδωσα :(')
                word = input('\nΠροσπάθησε να σκεφτείς ξανά μια λέξη: ')
                word_no_spaces = word.strip()

        return word_no_spaces


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.value_of_letters = []

    def __repr__(self):
        return f'Class: {self.__class__}, name:{self.name}, score:{self.score}, letters:{self.letters},' \
               f' value_of_letters:{self.value_of_letters}'

    @Player.score_decorator
    def show_score(self):
        print(self.score)

    @Player.final_score_decorator
    def show_final_score(self):
        print('=', '*', '=', self.score, '=', '*', '=')

    def show_letters(self):
        print('\nΤα γράμματα που έχεις στη διάθεσή σου μαζί με την αξία τους είναι:')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
        for index, letter in enumerate(self.letters):
            print(letter, self.value_of_letters[index], sep=':', end=' ')
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')

    def increase_score(self, value_of_word):
        super().increase_score(value_of_word)
        print('Τώρα το Σκορ σου είναι:', self.score)

    def get_word_with_min_mode_of_game(self, words):
        word = ''
        found_any_words = False
        for length_of_word in range(2, len(self.letters) + 1):
            permutations = it.permutations(self.letters, length_of_word)
            list_of_permutations = [''.join(letters) for letters in permutations]
            for possible_word in list_of_permutations:
                found_any_words = False
                if words.get(possible_word, 'Does not exist') != 'Does not exist':
                    found_any_words = True
                    word = possible_word
                    break
            if found_any_words:
                break

        return word

    def get_word_with_max_mode_of_game(self, words):
        word = ''
        found_any_words = False

        for length_of_word in range(len(self.letters), 1, -1):
            permutations = it.permutations(self.letters, length_of_word)
            list_of_permutations = [''.join(letters) for letters in permutations]
            for possible_word in list_of_permutations:
                found_any_words = False
                if words.get(possible_word, 'Does not exist') != 'Does not exist':
                    found_any_words = True
                    word = possible_word
                    break
            if found_any_words:
                break

        return word

    def get_word_with_smart_mode_of_game(self, words):
        max_score = 0
        max_word = ''
        for length_of_word in range(2, len(self.letters) + 1):
            permutations = it.permutations(self.letters, length_of_word)
            list_of_permutations = [''.join(letters) for letters in permutations]
            for possible_word in list_of_permutations:

                if words.get(possible_word, 'Does not exist') != 'Does not exist' and \
                        words.get(possible_word, 'Does not exist') > max_score:
                    max_score = words.get(possible_word)
                    max_word = possible_word

        return max_word

    def remove_letters_of_word(self, word_without_spaces):
        for letter in word_without_spaces:
            self.letters.remove(letter)

    def clear_list_with_values_of_letters(self):
        self.value_of_letters.clear()

    def play(self, words, mode):

        if mode == 'Min':
            word = self.get_word_with_min_mode_of_game(words)
        elif mode == 'Max':
            word = self.get_word_with_max_mode_of_game(words)
        else:
            word = self.get_word_with_smart_mode_of_game(words)

        return word


class Game:
    def __init__(self, mode='Smart'):  # Ο default τρόπος παιχνιδιού είναι ο Smart
        self.mode = mode  # Τρόπος παιχνιδιού
        self.word_dictionary = {}  # Οι λέξεις του παιχνιδιού
        self.moves = 0  # Οι κινήσεις του παιχνιδιού
        self.sak = SakClass()
        self.human_player = Human()
        self.computer_player = Computer()
        self.setup()  # Ξεκίνημα και εμφάνιση μενού

    def __repr__(self):
        return f'Class: {self.__class__}, mode:{self.mode}, s:{self.sak.__class__},h:{self.human_player.__class__}' \
               f',c: {self.computer_player.__class__},words:{self.word_dictionary},total_moves: ,{self.moves}'

    def write_statistics_to_file(self):
        # Νέα στατιστικά της παρτίδας που μόλις έλαβε τέλος
        this_game_statistics = {}
        this_game_statistics['Κινήσεις:'] = self.moves
        this_game_statistics['Σκορ παίκτη:'] = self.human_player.score
        this_game_statistics['Σκορ υπολογιστή:'] = self.computer_player.score

        # Νέα λίστα με στοιχεία τα Σκορ και στατιστικά των παιχνιδιών. Αυτή η λίστα θα συμπεριλαμβάνει και τα νέα
        # στατιστικά από την παρτίδα που μόλις ολοκληρώθηκε
        new_scores_list = []

        # Αρχικά φορτώνεται η παλιά λίστα με τα στατιστικά
        with open('scores_file.json') as scores_file:
            new_scores_list = js.load(scores_file)
            new_scores_list.append(this_game_statistics)

        # Και αυτή ανανεώνεται με την προσθήκη των στατιστικών της τελευταίας παρτίδας που μόλις παίχτηκε
        with open('scores_file.json', 'w') as scores_file:
            js.dump(new_scores_list, scores_file)

    def announce_winner_and_scores(self):
        if self.computer_player.score > self.human_player.score:
            print('\n-=-=-=GAME OVER=-=-=-')
            print('Ο νικητής/τρια είναι ο/η :', self.computer_player.name, 'με Σκορ :', self.computer_player.score)
            print('Το Σκορ του/της:', self.human_player.name, 'είναι:', self.human_player.score)
        elif self.human_player.score > self.computer_player.score:
            print('\n-=-=-=GAME OVER=-=-=-')
            print('Ο νικητής/τρια είναι ο/η :', self.human_player.name, 'με Σκορ :', self.human_player.score)
            print('Το Σκορ του/της:', self.computer_player.name, 'είναι:', self.computer_player.score)
        else:
            print('\n-=-=-=GAME OVER=-=-=-')
            print('Είναι ισοπαλία! Το Σκορ και των δύο είναι: ', self.computer_player.score)

    def setup(self):
        # Ετοιμασία των γραμμάτων με τις αξίες τους στο σακουλάκι
        self.sak.randomize_sak()

        # Φόρτωμα λέξεων στον κώδικα ως δομή λεξικού
        with open('greek7.txt', encoding='utf-8') as words_file:
            for line in words_file:
                word = line.strip('\n')
                word_score = 0
                for letter in word:
                    word_score += self.sak.letters[letter][1]
                self.word_dictionary[word] = word_score  # Σκορ της λέξης
        print('Καλώς ήρθατε στο διαχρονικότερο παιχνίδι λέξεων!')

        # Μήνυμα εμφάνισης μενού
        self.print_menu()

        # Μενού επιλογών και ρυθμίσεων για τον χρήστη
        while True:
            user_input = input('\nΕπιλογή: ')

            # Προβολή αρχείου με τα στατιστικά του παιχνιδιού
            if user_input == '1':
                try:
                    print('\n=*=*=ΣΤΑΤΙΣΤΙΚΑ=*=*=')
                    with open('scores_file.json') as scores_and_statistics:
                        file_with_scores = js.load(scores_and_statistics)

                except FileNotFoundError:
                    print('Δυστυχώς τα στατιστικά δεν είναι διαθέσιμα αυτήν τη στιγμή :(')

                else:

                    for dictionary in file_with_scores:
                        for key, value in dictionary.items():
                            print(key, value)
                        print(20 * '*')

                print('\nΠίσω στο μενού...')
                self.print_menu()

                # Ρυθμίσεις παιχνιδιού που αφορούν τον αλγόριθμο σύμφωνα με τον οποίο θα παίζει ο υπολογιστής(Min-Max-Smart)
            elif user_input == '2':
                print('\n========Ρυθμίσεις========',
                      'Επίλεξε τρόπο παιχνιδιού: ',
                      '\n1) Min: Ο υπολογιστής θα παίζει τη μικρότερη και πρώτη αποδεκτή λέξη που βρει!',
                      '2) Max: Ο υπολογιστής θα παίζει τη μεγαλύτερη αποδεκτή λέξη που θα βρει!',
                      '3) Smart: Ο υπολογιστής θα παίζει τη λέξη με το μεγαλύτερο σκορ!', sep='\n')

                while True:
                    user_input = input('\nΕπιλογή τρόπου παιχνιδιού: ')

                    if user_input == '1':
                        print('Έχεις επιλέξει το Min τρόπο παιχνιδιού!')
                        self.mode = 'Min'
                        break
                    elif user_input == '2':
                        print('Έχεις επιλέξει το Max τρόπο παιχνιδιού!')
                        self.mode = 'Max'
                        break
                    elif user_input == '3':
                        print('Έχεις επιλέξει το Smart τρόπο παιχνιδιού!')
                        self.mode = 'Smart'
                        break
                    else:
                        print('Παρακαλώ πληκτρολόγησε: 1 ή 2 ή 3!')

                print('\nΠίσω στο μενού...')
                self.print_menu()

            # Έναρξη παιχνιδιού
            elif user_input == '3':
                self.run()
                break

            # Έξοδος από το παιχνίδι
            elif user_input == 'q':
                print('Κατάλαβα... Θες να αποχωρήσεις :(')
                print('Ακολουθεί έξοδος από το παιχνίδι...')
                break

            else:
                print('\nΠαρακαλώ πληκτρολόγησε: 1 ή 2 ή 3 ή q!')

    @staticmethod
    def print_menu():
        print()
        print(15 * '~', 'S C R A B B L E', 15 * '~', sep=' ')
        print(19 * '=', 'M E N U', 19 * '=')
        print('Επίλεξε ένα από τα παρακάτω: ', '1: Σκορ', '2: Ρυθμίσεις', '3: Νέο Παιχνίδι', 'q: Έξοδος', sep='\n')

    def run(self):
        print('\nΤο παιχνίδι μόλις ξεκίνησε! Ετοιμάσου για μια παρτίδα από το συναρπαστικότερο παιχνίδι λέξεων!')
        self.human_player.name = input('Ποιο είναι το όνομά σου; ')
        self.computer_player.name = input('Ποιο θες να είναι το όνομα του Scrabble Master Ηλεκτρονικού Υπολογιστή; ')

        # Δίνονται εκ των προτέρων 7 γράμματα στον παίκτη με την αξία τους
        human_player_letters = self.sak.getletters(7)
        self.human_player.letters = [letter for letter in human_player_letters]
        self.human_player.value_of_letters = [self.sak.letters.get(letter)[1] for letter in human_player_letters]

        # Έπειτα, δίνονται 7 γράμματα στον υπολογιστή μαζί με την αξία τους
        computer_player_letters = self.sak.getletters(7)
        self.computer_player.letters = [letter for letter in computer_player_letters]
        self.computer_player.value_of_letters = [self.sak.letters.get(letter)[1] for letter in computer_player_letters]

        # Υποδηλώνει πως ήρθε η ώρα να λήξει το παιχνίδι
        end_the_game_flag = False
        while not end_the_game_flag:
            # Ξεκινάει ο χρήσης. Εμφανίζεται μήνυμα που τον ενημερώνει ότι είναι η σειρά του και του δείχνει το Σκορ του
            self.human_player.show_score()

            # Μήνυμα που ενημερώνει τον χρήστη για το πλήθος των γραμμάτων που έχουν απομείνει στο σακουλάκι, αφού έχουν
            # δοθεί γράμματα στον ίδιο αλλά και στον υπολογιστή
            self.sak.show_number_of_letters_in_sak()

            while True:
                # Δείχνονται τα γράμματα στον παίκτη και παίζει εισάγοντας μια λέξη στα πλαίσια τα αλγορίθμου της play
                self.human_player.show_letters()
                word_no_spaces = self.human_player.play()

                # Εάν ο παίκτης θέλει να σταματήσει
                if word_no_spaces == 'q':
                    end_the_game_flag = True
                    break

                # Ο παίκτης πάει πάσο πατώντας p και του δίνονται άλλα γράμματα αλλά χάνει τη σειρά του
                elif word_no_spaces == 'p':
                    print('Ζήτησες να αλλάξεις τα γράμματά σου...για να δούμε τι μπορεί να γίνει!')

                    # Αυξάνεται ο αριθμός των συνολικών κινήσεων του παιχνιδιού (ακόμα και με το πάσο)
                    self.moves += 1

                    # Γίνεται έλεγχος εάν υπάρχουν άλλα γράμματα για να δοθούν
                    number_of_human_letters_already_given = len(self.human_player.letters)
                    number_of_new_letters_for_human_player = self.sak.define_how_many_letters_can_be_taken_from_sak()

                    if number_of_new_letters_for_human_player >= number_of_human_letters_already_given and \
                            number_of_new_letters_for_human_player > 0 :
                        print('Ο Scrabble Master κατόρθωσε να βρει νέα γράμματα! Σε καλή μεριά...απλώς...χάνεις τη'
                              ' σειρά σου και το σκορ σου μένει το ίδιο!')

                        # Εφόσον υπάρχουν αρκετά γράμματα μέσα στο σακουλάκι, δίνονται στον παίκτη τόσα γράμματα όσα είχε
                        new_letters_for_human_player = self.sak.getletters(number_of_human_letters_already_given)

                        # Επιστρέφονται στο σακουλάκι τα γράμματα με τα οποία ο παίκτης δεν μπόρεσε να βρει έγκυρη λέξη
                        self.sak.putbackletters(human_player_letters)

                        # Τα νέα γράμματα αντικαθιστούν τα παλιά
                        human_player_letters = new_letters_for_human_player
                        self.human_player.letters = [letter for letter in human_player_letters]
                        self.human_player.value_of_letters = [self.sak.letters.get(letter)[1] for letter in
                                                              human_player_letters]

                    else:
                        # Εάν όχι, τότε το παιχνίδι σταματάει.
                        print(
                            'Δυστυχώς δεν γίνεται να πας πάσο γιατί τα γράμματα τελείωσαν. Το παιχνίδι έλαβε τέλος :(')

                        # Πρέπει να πατηθεί ο χαρακτήρας 'q' από τον χρήστη για να λάβει η παρτίδα τέλος
                        quit_input = input('Πάτησε q για να τελειώσει το παιχνίδι')
                        while quit_input != 'q':
                            quit_input = input('Πάτησε q για να τελειώσει το παιχνίδι: ')
                        end_the_game_flag = True
                    break

                else:
                    # Έλεγχος για το εάν είναι αποδεκτή η λέξη που εισήγαγε ο παίκτης
                    is_word_found = self.word_dictionary.get(word_no_spaces, 'Does not exist')

                    # Εάν όχι, τότε δε θα σταματήσει ο βρόγχος που καλεί τον αλγόριθμο play για τον human player μέχρι
                    # να βρεθεί λέξη(ή να πατηθεί το 'p')
                    if is_word_found == 'Does not exist':
                        print('Δυστυχώς η λέξη αυτή δεν υπάρχει στο λεξικό...Προσπάθησε να βάλεις μια άλλη!')

                    else:
                        word_score = self.word_dictionary.get(word_no_spaces)

                        print('Μπράβο σου! Η λέξη υπάρχει στο λεξικό του Scrabble Master!')
                        print('\nΟι συνολικοί βαθμοί της λέξης είναι:', word_score)

                        # Ενημέρωση του Σκορ του χρήστη/παίκτη και εμφάνιση μηνύματος για το τρέχον Σκορ
                        self.human_player.increase_score(word_score)

                        # Αυξάνεται ο αριθμός των συνολικών κινήσεων του παιχνιδιού
                        self.moves += 1

                        # Τα γράμματα που χρησιμοποιήθηκαν στη λέξη, αντικαθίστανται εάν είναι εφικτό
                        length_of_word_played = len(word_no_spaces)

                        number_of_new_letters_for_human_player = self.sak.define_how_many_letters_can_be_taken_from_sak()
                        if number_of_new_letters_for_human_player >= length_of_word_played:

                            # Τα γράμματα που χρησιμοποιήθηκαν αφαιρούνται από τα διαθέσιμα γράμματα του παίκτη
                            self.human_player.remove_letters_of_word(word_no_spaces)

                            # Ετοιμάζονται για τον παίκτη τόσα γράμματα όσα είχε η λέξη που έβαλε
                            new_letters_for_human_player = self.sak.getletters(length_of_word_played)

                            # Στα ήδη υπάρχοντα γράμματα του παίκτη (που δεν αντικαταστάθηκαν), προστίθενται τα
                            # καινούργια
                            for letter in new_letters_for_human_player:
                                self.human_player.letters.append(letter)

                            # Η λίστα με την αξία των γραμμάτων αδειάζει για να αντικατασταθεί με τις αξίες των νέων
                            # γραμμάτων
                            self.human_player.clear_list_with_values_of_letters()

                            # Υπολογίζονται οι αξίες των νέων γραμμάτων
                            for letter in self.human_player.letters:
                                self.human_player.value_of_letters.append(self.sak.letters.get(letter)[1])

                            # Τα νέα γράμματα αντικαθιστούν τα παλιά
                            human_player_letters = self.human_player.letters

                            # Προτροπή του παίκτη να συνεχίσει το παιχνίδι
                            enter_input = input('\nΠάτησε Enter για να συνεχίσουμε το παιχνίδι!')
                            while enter_input != '':
                                enter_input = input('\nΠάτησε Enter για να συνεχίσουμε το παιχνίδι!')

                        else:

                            # Τα γράμματα που χρησιμοποιήθηκαν αφαιρούνται από τα διαθέσιμα γράμματα του παίκτη
                            self.human_player.remove_letters_of_word(word_no_spaces)

                            # Εάν υπάρχει έστω και ένα γράμμα στο σακουλάκι διαθέσιμο για αντικατάσταση, ο χρήστης
                            # μπορεί να ανανεώσει τα γράμματά του
                            number_of_new_letters_for_human_player = self.sak.define_how_many_letters_can_be_taken_from_sak()
                            if number_of_new_letters_for_human_player > 0:
                                new_letters_for_human_player = self.sak.getletters(number_of_new_letters_for_human_player)

                                # Στα ήδη υπάρχοντα γράμματα (που δεν αντικαταστάθηκαν), προστίθενται τα καινούργια
                                for letter in new_letters_for_human_player:
                                    self.human_player.letters.append(letter)

                            # Η λίστα με την αξία των γραμμάτων αδειάζει για να ανανεωθεί παρακάτω
                            self.human_player.clear_list_with_values_of_letters()

                            # Υπολογίζονται οι αξίες των νέων γραμμάτων
                            for letter in self.human_player.letters:
                                self.human_player.value_of_letters.append(self.sak.letters.get(letter)[1])

                            # Τα νέα γράμματα αντικαθιστούν τα παλιά
                            human_player_letters = self.human_player.letters

                            # Προτροπή του παίκτη να συνεχίσει το παιχνίδι
                            enter_input = input('\nΠάτησε Enter για να συνεχίσουμε το παιχνίδι!')
                            while enter_input != '':
                                enter_input = input('\nΠάτησε Enter για να συνεχίσουμε το παιχνίδι!')

                        break

            if end_the_game_flag:
                self.end()
                break

            # Σειρά του υπολογιστή: Εμφανίζεται πρώτα το πλήθος των γραμμάτων στο σακουλάκι
            self.sak.show_number_of_letters_in_sak()

            # Έπειτα, εμφανίζει το Σκορ του υπολογιστή
            self.computer_player.show_score()

            # Εμφανίζονται τα γράμματα με την αξία τους στην οθόνη
            self.computer_player.show_letters()

            # Εμφανίζεται η λέξη που βρήκε ο υπολογιστής, αλλιώς εμφανίζεται μήνυμα πως είναι αδύνατη η εύρεση λέξης
            computer_word = self.computer_player.play(self.word_dictionary, self.mode)
            if computer_word == '':
                print('Είναι αδύνατο να βρεθεί λέξη με αυτά τα γράμματα')

                # Γίνεται έλεγχος εάν υπάρχουν άλλα γράμματα για να δοθούν στον υπολογιστή
                number_of_computer_letters_already_given = len(self.computer_player.letters)
                number_of_new_letters_for_computer_player = self.sak.define_how_many_letters_can_be_taken_from_sak()

                if number_of_new_letters_for_computer_player >= number_of_computer_letters_already_given and\
                        number_of_new_letters_for_computer_player>0 :
                    print('Ο Scrabble Master κατόρθωσε να βρει νέα γράμματα για τον υπολογιστή αλλά θα χάσει τη'
                          ' σειρά του!')

                    # Εφόσον υπάρχουν αρκετά γράμματα μέσα στο σακουλάκι, δίνονται στον υπολογιστή τόσα γράμματα όσα είχε
                    new_letters_for_computer_player = self.sak.getletters(number_of_computer_letters_already_given)

                    # Επιστρέφονται στο σακουλάκι τα γράμματα με τα οποία ο παίκτης δεν μπόρεσε να βρει έγκυρη λέξη
                    self.sak.putbackletters(computer_player_letters)

                    # Τα νέα γράμματα αντικαθιστούν τα παλιά
                    computer_player_letters = new_letters_for_computer_player
                    self.computer_player.letters = [letter for letter in computer_player_letters]
                    self.computer_player.value_of_letters = [self.sak.letters.get(letter)[1] for letter in
                                                             computer_player_letters]

                else:
                    # Εάν δεν υπάρχουν διαθέσιμα γράμματα και ο υπολογιστής δεν έχει βρει λέξη, τότε το παιχνίδι
                    # σταματάει
                    print('Δυστυχώς το παιχνίδι τελείωσε γιατί ο Υπολογιστής δεν μπορεί να βρει λέξη και το σακουλάκι'
                          ' δεν έχει άλλα γράμματα :(')
                    end_the_game_flag = True
                    self.end()

            else:
                # Εμφανίζεται η λέξη με τη βαθμολογία της και το ανανεωμένο Σκορ του υπολογιστή
                computer_word_value = self.word_dictionary.get(computer_word)
                print('Η λέξη που βρέθηκε είναι:', computer_word, 'με βαθμολογία:', computer_word_value)

                # Αυξάνεται το Σκορ του υπολογιστή
                self.computer_player.increase_score(computer_word_value)

                # Τα γράμματα που χρησιμοποιήθηκαν στη λέξη, αντικαθίστανται εάν είναι εφικτό
                length_of_word_played_by_computer = len(computer_word)
                number_of_new_letters_for_computer_player = self.sak.define_how_many_letters_can_be_taken_from_sak()
                if number_of_new_letters_for_computer_player >= length_of_word_played_by_computer:

                    # Τα γράμματα που χρησιμοποιήθηκαν αφαιρούνται από τα διαθέσιμα γράμματα του υπολογιστή
                    self.computer_player.remove_letters_of_word(computer_word)

                    # Ετοιμάζονται για τον υπολογιστή τόσα γράμματα όσα είχε η λέξη που έβαλε
                    new_letters_for_computer_player = self.sak.getletters(length_of_word_played_by_computer)

                    # Στα ήδη υπάρχοντα γράμματα του υπολογιστή (που δεν αντικαταστάθηκαν), προστίθενται τα καινούργια
                    for letter in new_letters_for_computer_player:
                        self.computer_player.letters.append(letter)

                    # Η λίστα με την αξία των γραμμάτων αδειάζει για να αντικατασταθεί με τις αξίες των νέων γραμμάτων
                    self.computer_player.clear_list_with_values_of_letters()

                    # Υπολογίζονται οι αξίες των νέων γραμμάτων
                    for letter in self.computer_player.letters:
                        self.computer_player.value_of_letters.append(self.sak.letters.get(letter)[1])

                    # Τα νέα γράμματα αντικαθιστούν τα παλιά
                    computer_player_letters = self.computer_player.letters

                else:
                    # Τα γράμματα που χρησιμοποιήθηκαν αφαιρούνται από τα διαθέσιμα γράμματα του υπολογιστή
                    self.computer_player.remove_letters_of_word(computer_word)

                    # Εάν υπάρχει έστω και ένα γράμμα στο σακουλάκι διαθέσιμο για αντικατάσταση, ο Υπολογιστής μπορεί να
                    # ανανεώσει τα γράμματά του
                    number_of_new_letters_for_computer_player = self.sak.define_how_many_letters_can_be_taken_from_sak()
                    if number_of_new_letters_for_computer_player > 0:
                        new_letters_for_computer_player = self.sak.getletters(number_of_new_letters_for_computer_player)

                        # Στα ήδη υπάρχοντα γράμματα του υπολογιστή (που δεν αντικαταστάθηκαν), προστίθενται τα καινούργια
                        for letter in new_letters_for_computer_player:
                          self.computer_player.letters.append(letter)

                    # Η λίστα με την αξία των γραμμάτων αδειάζει για να αντικατασταθεί με τις αξίες των νέων
                    # γραμμάτων
                    self.computer_player.clear_list_with_values_of_letters()

                    # Υπολογίζονται οι αξίες των νέων γραμμάτων
                    for letter in self.computer_player.letters:
                        self.computer_player.value_of_letters.append(self.sak.letters.get(letter)[1])

                    # Τα νέα γράμματα αντικαθιστούν τα παλιά
                    computer_player_letters = self.computer_player.letters

            # Αυξάνεται ο αριθμός των συνολικών κινήσεων του παιχνιδιού
            self.moves += 1

    def end(self):
        # Ανακηρύσσεται ο νικητής
        self.announce_winner_and_scores()

        # Και καταγράφονται στο αρχείο με τα στατιστικά τα στοιχεία της παρτίδας
        print('Δώσε μου ένα λεπτό να καταγράψω τα στατιστικά της παρτίδας!')
        self.write_statistics_to_file()
