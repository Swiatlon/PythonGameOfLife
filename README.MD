[ENG]  </br>
What has been done:

1.0 Fixed functionality logic. </br>
2.0 Added additional functionalities:   </br>
a) Save/Load button.  </br>
b) Real-time simulation start/stop button.  </br>
c) Deleting save button.  </br>
3.0 Split the code into smaller sections (abstraction):  </br>
a) Buttons  </br>
b) UiManager  </br>
c) GameLogic  </br>
d) GameState  </br>
e) FileManager  </br>
f) GridState  </br>
4.0 Introduced 3 design patterns:  </br>
a) Singleton: Used in UiManager to ensure only one UI instance exists.  </br>
b) State/Memento: Implemented in FileManager and GameState to track game states and the board's state.  </br>
c) Command: Applied to button actions, where each button has a unique command.  </br>
5.0 Refactored the code, removed unused portions, and corrected naming conventions.  </br>
 </br>
[PL]  </br>
Co zostało zrobione:  </br>
  </br>
1.0 Naprawienie logiki funkcjonalności  </br>
2.0 Dodanie dodatkowych funkcjonalności  </br>
a) Save/Load => button  </br>
b) Real time simulation => start/stop button  </br>
c) Usuwanie save'a =>  delete button  </br>
3.0 Rozdzielenie kodu na mniejsze sekcje (abstrakcja)  </br>
a) Buttony, UiManager, GameLogic, GameState, FileManager, GridState  </br>
4.0 Wprowadzenie 3 design patternów:  </br>
a) Singleton => Wykorzystany w UiManagerze ponieważ chcemy żeby była tylko jedna instancja UI  </br>
b) State/Memento => Wykorzystany w FileManagerze oraz GameState.Służyć może do trakowania stanów gry  oraz stanu planszy.   </br>
c) Command => Wykorzystany do akcji buttonów.Jeden button posiada jeden command który zawsze jest  różny   </br>
5.0 Refaktoryzacja, pozbycie się nieużywanego kodu i poprawienie nazewnictwa.  </br>
