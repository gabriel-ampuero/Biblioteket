Dokumentation - Biblioteksregister för böcker, filmer och CD-Skivor.

-Installation

Ingen installation förutom Python behövs, .py filen går att kör direkt i IDEs/terminaler etc.

-Navigation

Programmet startar med att ta dig direkt till huvudmenyn där du kan välja mellan fem olika alternativ. 
Du väljer alternativ genom att trycka på en siffra och sedan Enter.

Alternativ 1 - Registrera bok:
Programmet ber dig mata in bokens titel, författare, sidor, inköpsår, inköpspris och sparar det sedan i bokregistret
med ett nuvarande pris.

Alternativ 2 - Registrera film:
Programmet ber dig mata in filmens titel, regissör, längd (i minuter), inköpsår, inköpspris och sparar det sedan i filmregistret
med ett nuvarande pris.

Alternativ 3 - Registrera CD-skiva:
Programmet ber dig mata in CDns titel, artist, längd (i minuter), antal spår, inköpspris och sparar det sedan i CD-registret
med ett nuvarande pris.

Alternativ 4 - Skriv ut media:

Skriver ut all media som finns registrerat i registret. Föst böcker, sedan filmer och sist CD-skivor.
Sorterat i titelns bokstavsordning.

Alternativ 5 - Avsluta programmet:
Avslutar programmet

-Övrig information

Om du använt programmet fullt och registrerat all typ av media kommer 4 filer sammanlagt ha skapats i samma ställe
som .py-filen ligger i. "BOOKS.txt", "MOVIES.txt", "CD_RECORDS.txt" och "UPDATER.txt"

BOOKS, MOVIES och CD_RECORDS innehåller data för varje mediatyp. Raderas dessa så raderas mediatyperna från registret. 
UPDATER är en textfil som för nuvarande hjälper till att editera CD_RECORDS register. Inget nämnvärt händer om man
skulle radera den här filen.