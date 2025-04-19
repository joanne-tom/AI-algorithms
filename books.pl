:-dynamic book/4.
book(to_kill_a_mockingbird,harper_lee,fiction,available).
book(1984,george_orwell,dystopian,checked_out).
book(the_great_gatsby,f_scott_fitzgerald,fiction,available).
book(moby_dick,herman_melville,adventure,available).
book(pride_and_prejudice,jane_austen,romance,checked_out).

american(harper_lee).
american(f_scott_fitzgerald).
american(herman_melville).
british(george_orwell).
british(jane_austen).

book_available(X):-book(X,_,_,available).
book_avail(X):-book(X,_,_,available)->(retractall(book(X,_,_,available)),assertz(book(X,_,_,checked_out)),write('Can be checked out'));write('Already checked out').
book_genre(X,Y):-book(X,_,Y,_).
