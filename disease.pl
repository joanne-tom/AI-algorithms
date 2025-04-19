symptom(fever).
symptom(headache).
symptom(sore_throat).
symptom(runny_nose).
symptom(cough).
symptom(body_ache).
symptom(sneezing).
symptom(itchy_eyes).

disease(flu):-
    has_symptom(fever),
    has_symptom(body_ache),
    has_symptom(cough).
disease(cold):-
    has_symptom(headache),
    has_symptom(sore_throat),
    has_symptom(runny_nose).
disease(allergies):-
    has_symptom(sneezing),
    has_symptom(itchy_eyes),
    has_symptom(runny_nose).

diagnose:-
    write('Does the patient have fever (yes/no)'),nl,
    read(Ans1),
    process_symptom(fever,Ans1),
    write('Does the patient have headache (yes/no)'),nl,
    read(Ans2),
    process_symptom(headache,Ans2),
    write('Does the patient have sore throat (yes/no)'),nl,
    read(Ans3),
    process_symptom(sore_throat,Ans3),
    write('Does the patient have runny nose (yes/no)'),nl,
    read(Ans4),
    process_symptom(runny_nose,Ans4),
    write('Does the patient have cough (yes/no)'),nl,
    read(Ans5),
    process_symptom(cough,Ans5),
    write('Does the patient have body ache (yes/no)'),nl,
    read(Ans6),
    process_symptom(body_ache,Ans6),
    write('Does the patient have sneezing (yes/no)'),nl,
    read(Ans7),
    process_symptom(sneezing,Ans7),
    write('Does the patient have itchy eyes (yes/no)'),nl,
    read(Ans8),
    process_symptom(itchy_eyes,Ans8),
    find_disease.

process_symptom(Symptom,yes):-assertz(has_symptom(Symptom)).
process_symptom(_,no).
find_disease:-
    disease(D),
    write('The likely disease is '),write(D),nl,
    retractall(has_symptom(_)).
find_disease:-
    write('No matching diagnosis found'),nl,
    retractall(has_symptom(_)).
