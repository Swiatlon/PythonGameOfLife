[ENG]
What has been done:

1.0 Fixed functionality logic.
2.0 Added additional functionalities:
a) Save/Load button.
b) Real-time simulation start/stop button.
c) Deleting save button.
3.0 Split the code into smaller sections (abstraction):
a) Buttons
b) UiManager
c) GameLogic
d) GameState
e) FileManager
f) GridState
4.0 Introduced 3 design patterns:
a) Singleton: Used in UiManager to ensure only one UI instance exists.
b) State/Memento: Implemented in FileManager and GameState to track game states and the board's state.
c) Command: Applied to button actions, where each button has a unique command.
5.0 Refactored the code, removed unused portions, and corrected naming conventions.

[PL]
Co zostało zrobione:

1.0 Naprawienie logiki funkcjonalności
2.0 Dodanie dodatkowych funkcjonalności
a) Save/Load => button
b) Real time simulation => start/stop button
c) Usuwanie save'a =>  delete button
3.0 Rozdzielenie kodu na mniejsze sekcje (abstrakcja)
a) Buttony, UiManager, GameLogic, GameState, FileManager, GridState
4.0 Wprowadzenie 3 design patternów:
a) Singleton => Wykorzystany w UiManagerze ponieważ chcemy żeby była tylko jedna instancja UI
b) State/Memento => Wykorzystany w FileManagerze oraz GameState.Służyć może do trakowania stanów gry oraz stanu planszy.
c) Command => Wykorzystany do akcji buttonów.Jeden button posiada jeden command który zawsze jest różny
5.0 Refaktoryzacja, pozbycie się nieużywanego kodu i poprawienie nazewnictwa.
