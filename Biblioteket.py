import re
from pathlib import Path

#Huvudklass - Media

class media:

    def __init__(self, title, purchaseprice, currentprice):

        """ Gemensamma attribut och funktioner för alla subklasser """

        self.title = title
        self.purchaseprice = purchaseprice
        self.currentprice = currentprice

    # Funktioner som används av alla klasser

    def set_currentprice(self, currentprice):

        """ Sätter det nuvarande priset """

        self.currentprice = currentprice
    
    def add_media(self):

        """ Registrerar mediatyp i registret """

        if "author" in self.__dict__:
            with open("BOOKS.txt", "a+", encoding="utf8") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                book_string = (f"Titel: {self.title} | Författare: {self.author} | Antal sidnummer: {self.pages} | Inköpsår: {self.purchaseyear} | Inköpspris: {self.purchaseprice} SEK | Nuvarande pris: {self.currentprice} SEK")
                file_object.write(book_string)
            print(f"Bok Registrerad!\n{book_string}")
        elif "director" in self.__dict__:
            with open("MOVIES.txt", "a+", encoding="utf8") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                movie_string = (f"Titel: {self.title} | Regissör: {self.director} | Längd: {self.length}min | Inköpsår: {self.purchaseyear} | Inköpspris: {self.purchaseprice} SEK | Nuvarande pris: {self.currentprice} SEK")
                file_object.write(movie_string)
                print(f"Film Registrerad!\n{movie_string}")
        elif "artist" in self.__dict__:
            with open("CD_RECORDS.txt", "a+", encoding="utf8") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                cd_string = (f"Titel: {self.title} | Artist: {self.artist} | Längd: {self.length}min | Spår: {self.tracks} | Inköpspris: {self.purchaseprice} SEK | Nuvarande pris: {self.currentprice} SEK")
                file_object.write(cd_string)
                print(f"CD Registrerad!\n{cd_string}")

#Subklasser - böcker, filmer, cd-skivor

class books(media):

    def __init__(self, title, author, pages, purchaseyear, purchaseprice, currentprice):

        """ Bok-klassen med dom egna attributen author, pages och purchaseyear """

        super().__init__(title, purchaseprice, currentprice)
        self.author = author
        self.pages = pages
        self.purchaseyear = purchaseyear

    # Funktioner som används för bok-klassen

    def book_value(self):

        """ Kalkylerar bokens nuvarande värde """

        book_age = 2020 - self.purchaseyear
        older_book_year_count = book_age - 50
        if book_age == 0:
            return round(self.purchaseprice)
        elif book_age in range(1, 50):
            return round(self.purchaseprice * 0.9**book_age)
        else:
            return round(self.purchaseprice * 1.08**older_book_year_count)


class movies(media):

    def __init__(self, title, director, length, purchaseyear, purchaseprice, currentprice):

        """ Film-klassen med dom egna attributen director, lenth och purchaseyear """

        super().__init__(title, purchaseprice, currentprice)
        self.director = director
        self.length = length
        self.purchaseyear = purchaseyear

    # Funktioner som används för film-klassen

    def movie_value(self):

        """ Kalkylerar filmens nuvarande värde """

        condition_level = 0
        while condition_level == 0 or condition_level >= 11:
            condition_level = int(input("Skriv in förslitningsgrad (1-10): "))
            if condition_level == 0 or condition_level >= 11:
                print("Skriv in ett nummer mellan 1-10")
        movie_age = 2020 - self.purchaseyear
        if condition_level == 10:
            return round(self.purchaseprice * 0.9**movie_age)
        elif condition_level in range(1, 10):
            updated_price = self.purchaseprice * 0.9**movie_age
            condition_level_string = "0." + str(condition_level)
            condition_level_value = float(condition_level_string)
            return round(updated_price * condition_level_value)


class cd_records(media):

    def __init__(self, title, artist, tracks, length, purchaseprice, currentprice):

        """ CD-klassen med dom egna attributen artist, tracks, length och purchaseyear """

        super().__init__(title, purchaseprice, currentprice)
        self.artist = artist
        self.tracks = tracks
        self.length = length

    # Funktioner som används för CD-klassen

    def copies_counter(self):

        """ Funktion som kalkyrerar antalet exemplar som finns i registret med samma titel och artist-namn """

        copies = 1
        if Path("CD_RECORDS.txt").is_file():
            with open("CD_RECORDS.txt", "r+", encoding="utf8") as file_object:
                for line in file_object:
                    if (f"Titel: {self.title} | Artist: {self.artist}") in line:
                        copies += 1
            file_object.close()
        else:
            pass
        return copies

    def cd_records_updater(self, amount_of_copies):

        """ Funktion som uppdaterar det nuvarande priset på gamla exemplar om en CD med samma titel och artist registraras"""

        if Path("CD_RECORDS.txt").is_file():
            with open("CD_RECORDS.txt", "r+", encoding="utf8") as file_object1, open("CD_RECORDS_UPDATER.txt", "w+", encoding="utf8") as file_object2:
                for line in file_object1:
                    if (f"Titel: {self.title} | Artist: {self.artist}") in line:
                        result1 = re.search("Inköpspris: (.*) SEK ", line)
                        purchase_price = result1.group(1)
                        updated_current_price = int(purchase_price)//amount_of_copies
                        result2 = re.search("Nuvarande pris: (.*) SEK", line)
                        previous_price = result2.group(1)
                        old_line_string = line
                        updated_line_string = line.replace((f"Nuvarande pris: {previous_price} SEK"), (f"Nuvarande pris: {updated_current_price} SEK"))
                        file_object2.write(line.replace(old_line_string, updated_line_string))
                    else:
                        file_object2.write(line)
        else:
            pass
        if Path("CD_RECORDS.txt").is_file():
            with open("CD_RECORDS_UPDATER.txt", "r+", encoding="utf8") as file_object1, open("CD_RECORDS.txt", "w+", encoding="utf8") as file_object2:
                for line in file_object1:
                    file_object2.write(line)
                file_object1.close()
                file_object2.close()

    def cd_value(self, amount_of_copies):
        
        """ Kalkylerar CDns nuvarande värde """

        return round(self.purchaseprice/amount_of_copies)

# Retrerande funktioner

def sort_and_print(filename):

    """ Funktion som skriver ut media sorterat """

    media_list = []
    if Path(filename).is_file():
        with open(filename, "r+", encoding="utf8") as file_object:
            for line in file_object:
                line_string = line.replace("\n", "")
                media_list.append(line_string)
        media_sorted = sorted(media_list)
        for media_string in media_sorted:
            print(media_string)
    else:
        print("Ingen media registrerad!")

def alternative():

    """ Skriver ut meny-alternativ"""

    print("Välj alternativ: \n1. Registrera bok \n2. Registrera film \n3. Registrera cd-skiva \n4. Skriv ut media \n5. Avsluta programmet")


def menu(media):

    """Huvudmenyn"""

    input_number = 0
    while input_number != 5:

        alternative()
        input_number = (int(input("Välj ett alternativ: ")))

        # Alternativ 1 - Registrerar Böcker

        if input_number == 1:
            print("------------------\nRegistrera Bok\n------------------")
            title = input("Skriv in titel: ").title()
            author = input("Skriv in författare: ").title()
            pages = int(input("Skriv in antal sidnummer: "))
            purchaseyear = int(input("Skriv in inköpsår: "))
            purchaseprice = int(input("Skriv in inköpspris: "))
            currentprice = "Unknown"

            temp_book = books(title, author, pages, purchaseyear, purchaseprice, currentprice)
            current_price = temp_book.book_value()
            temp_book.set_currentprice(current_price)
            temp_book.add_media()

            input("Tryck Enter för att fortsätta...")

        # Alternativ 2 - Registrerar Filmer

        elif input_number == 2:
            print("------------------\nRegistrera Film\n------------------")
            title = input("Skriv in titel: ").title()
            director = input("Skriv in regissör: ").title()
            length = int(input("Skriv in längd i minuter: "))
            purchaseyear = int(input("Skriv in inköpsår: "))
            purchaseprice = int(input("Skriv in inköpspris: "))
            currentprice = "Unknown"
            
            temp_movie = movies(title, director, length, purchaseyear, purchaseprice, currentprice)
            current_price = temp_movie.movie_value()
            temp_movie.set_currentprice(current_price)
            temp_movie.add_media()

            input("Tryck Enter för att fortsätta...")

        # Alternativ 3 - Registrerar CD-Skivor 

        elif input_number == 3:
            print("------------------\nRegistrera CD-Skiva\n------------------")
            title = input("Skriv in titel: ").title()
            artist = input("Skriv in artist: ").title()
            tracks = int(input("Skriv in antal spår: "))
            length = int(input("Skriv in längd i minuter: " ))
            purchaseprice = int(input("Skriv in inköpspris: "))
            currentprice = "Unknown"

            temp_cd = cd_records(title, artist, tracks, length, purchaseprice, currentprice)
            amount_of_copies = temp_cd.copies_counter()
            temp_cd.cd_records_updater(amount_of_copies)
            current_price = purchaseprice//amount_of_copies
            temp_cd.set_currentprice(current_price)
            temp_cd.add_media()

            input("Tryck Enter för att fortsätta...")

        # Alternativ 4 - Skriver utall registrerad media

        elif input_number == 4:
            print("------------------------------------")
            print("---------------BÖCKER---------------")
            print("------------------------------------")
            sort_and_print("BOOKS.txt")
            print("------------------------------------")
            print("---------------FILMER---------------")
            print("------------------------------------")
            sort_and_print("MOVIES.txt")
            print("-------------------------------------")
            print("--------------CD-SKIVOR--------------")
            print("-------------------------------------")
            sort_and_print("CD_RECORDS.txt")
            print("-------------------------------------")

            input("Tryck Enter för att fortsätta...")

        # Alternativ 5 - Avslutar programmet

        elif input_number == 5:
            exit()
        else:
            print("Fel inmatning, välj ett alternativ mellan 1-5")

menu(media)