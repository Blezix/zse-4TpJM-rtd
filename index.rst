Nagłówki tekstowe (poziomy 1-4)
=============================

.. _naglowki_sekcja:

Nagłówek 1 poziomu
------------------
Nagłówek 2 poziomu
~~~~~~~~~~~~~~~~~~
Nagłówek 3 poziomu
^^^^^^^^^^^^^^^^^^
Nagłówek 4 poziomu
..................

Akapit tekstowy (treść)

Akapit informacyjny (Note, Tip)
==============================

.. _informacyjne_sekcja:

.. note::
    To jest akapit informacyjny w formie noty.

.. tip::
    To jest akapit informacyjny w formie wskazówki.

Fragment kodu (liniowy, blokowy)
=============================

.. _kod_sekcja:

Liniowy fragment kodu:

 ``print("Hello, World!")``

Blokowy fragment kodu:

.. code-block:: python

    def hello_world():
        print("Hello, World!")

Odnośnik (lokalny RtD, zewnętrzny-inny serwis)
===========================================

Lokalny odnośnik w ReadTheDocs:

:ref:`naglowki_sekcja` - Link do sekcji "Nagłówki tekstowe"


`Zewnętrzny odnośnik: <https://www.youtube.com/watch?v=dQw4w9WgXcQ>`_

Listy (numerowana, wypunktowana, definicji)
=========================================

Numerowana lista:

1. Pierwszy element

2. Drugi element

3. Trzeci element

Wypunktowana lista:

- Item 1

- Item 2

- Item 3

Lista definicji:

Termin 1

    Definicja pierwszego terminu.

Termin 2

    Definicja drugiego terminu.

Obraz (z alternatywnym tekstem oraz podpisem)
==========================================

.. figure:: `./Assets/photo.png`

   :alt: Przykładowy obraz
   :figclass: align-center
   :caption: To jest przykładowy obraz.

Tabela (jeżeli istnieje)
========================

+-----------+-----------+-----------+
| Kolumna 1 | Kolumna 2 | Kolumna 3 |
+===========+===========+===========+
| Wartość 1 | Wartość 2 | Wartość 3 |
+-----------+-----------+-----------+
| Wartość 4 | Wartość 5 | Wartość 6 |
+-----------+-----------+-----------+
