
** Struktura systemu lub aplikacji

Projekt składa się z następujących plików:

- `computer_api_tests.py`: Plik zawierający testy jednostkowe dla API Komputera.
- `README.md`: Plik zawierający dokumentację projektu.

** Scenariusze testowe

* Test 1: Pobieranie podstawowych informacji o komputerze

- Opis: Testuje funkcjonalność pobierania podstawowych informacji o komputerze z API.
- Kroki:
  1. Wyślij żądanie GET do `http://mojastrona.net/api.php` z poprawnym identyfikatorem komputera i typem "basic".
  2. Sprawdź kod odpowiedzi.
  3. Porównaj dane odpowiedzi z oczekiwanymi danymi.

* Test 2: Pobieranie informacji o komputerze do gier

- Opis: Testuje funkcjonalność pobierania informacji o komputerze do gier z API.
- Kroki:
  1. Wyślij żądanie GET do `http://mojastrona.net/api.php` z poprawnym identyfikatorem komputera i typem "gaming".
  2. Sprawdź kod odpowiedzi.
  3. Porównaj dane odpowiedzi z oczekiwanymi danymi.

* Test 3: Obsługa nieprawidłowego identyfikatora komputera

- Opis: Testuje obsługę nieprawidłowego identyfikatora komputera przez API.
- Kroki:
  1. Wyślij żądanie GET do `http://mojastrona.net/api.php` z nieprawidłowym identyfikatorem komputera i poprawnym typem.
  2. Sprawdź kod odpowiedzi.
  3. Upewnij się, że kod odpowiedzi wskazuje na błąd serwera.

* Test 4: Obsługa nieistniejącego identyfikatora komputera

- Opis: Testuje obsługę nieistniejącego identyfikatora komputera przez API.
- Kroki:
  1. Wyślij żądanie GET do `http://mojastrona.net/api.php` z nieistniejącym identyfikatorem komputera i poprawnym typem.
  2. Sprawdź kod odpowiedzi.
  3. Upewnij się, że kod odpowiedzi wskazuje na brak zasobu.

* Test 5: Obsługa nieprawidłowej ścieżki

- Opis: Testuje obsługę nieprawidłowej ścieżki przez API.
- Kroki:
  1. Wyślij żądanie GET do `http://mojastrona.net/api.php` bez podania identyfikatora komputera i typu.
  2. Sprawdź kod odpowiedzi.
  3. Upewnij się, że kod odpowiedzi wskazuje na błąd serwera.

** Wykorzystane narzędzia i biblioteki

Projekt wykorzystuje następujące narzędzia i biblioteki:

- Python: Język programowania używany do napisania testów jednostkowych.
- unittest: Moduł biblioteki standardowej Pythona do tworzenia i uruchamiania testów jednostkowych.
- requests: Biblioteka Pythona do wykonywania żądań HTTP.

** Ewentualne problemy i ich rozwiązanie

* Problem: Błąd odpowiedzi o kodzie 500 dla nieprawidłowego identyfikatora komputera

Opis: Test `test_invalid_computer_id` oczekuje kodu odpowiedzi 500 dla nieprawidłowego identyfikatora komputera, ale w niektórych przypadkach może zwrócić inny kod odpowiedzi.

Rozwiązanie: Można zaktualizować test, aby uwzględnić inne kody odpowiedzi, które również wskazują na błąd związany z nieprawidłowym identyfikatorem komputera.

* Problem: Błąd odpowiedzi o kodzie 500 dla nieprawidłowej ścieżki

Opis: Test `test_invalid_path` oczekuje kodu odpowiedzi 500 dla nieprawidłowej ścieżki, ale w niektórych przypadkach może zwrócić inny kod odpowiedzi.

Rozwiązanie: Można zaktualizować test, aby uwzględnić inne kody odpowiedzi, które również wskazują na błąd związany z nieprawidłową ścieżką.

To jest tylko przykładowa dokumentacja, którą można dostosować do swoich potrzeb. Ważne jest, aby opisać strukturę projektu, scenariusze testowe, narzędzia i biblioteki użyte w projekcie oraz ewentualne problemy, na jakie można napotkać i jak je rozwiązać.