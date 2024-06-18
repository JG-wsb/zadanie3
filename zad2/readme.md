# Automatyzacja procesów z wykorzystaniem Makefile

## Opis

Ten projekt zawiera prostą aplikację napisaną w Pythonie oraz skrypt Makefile do automatyzacji procesów instalacji, testowania i uruchamiania aplikacji.

## Struktura projektu

zad2/

├── app.py

├── test_app.py

├── Makefile

└── README.md

### app.py

Prosta aplikacja z jedną funkcją `add(a, b)`, która zwraca sumę dwóch liczb.

### test_app.py

Testy jednostkowe dla aplikacji, sprawdzające poprawność funkcji `add`.

## Makefile

Plik Makefile zawiera następujące reguły:

- `install`: Instaluje zależności (w tym przypadku brak zewnętrznych zależności).
- `test`: Uruchamia testy jednostkowe za pomocą unittest.
- `run`: Uruchamia aplikację.

## Użycie

1. Zainstaluj zależności (jeśli są):

```sh
make install
make test
make run
```
![image](https://github.com/JG-wsb/zadanie3/assets/169584693/dba3a8fb-f83c-49ce-a5d4-baf0d5973cbe)


### Podsumowanie

Wykonane zadanie obejmuje stworzenie prostej aplikacji w Pythonie, napisanie testów jednostkowych oraz utworzenie pliku Makefile do automatyzacji procesów.







