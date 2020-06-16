% Ejercicio String prolog 1
% Ramirez Aguilar Jose Oswaldo & Sanchez Avila Gustavo
% Desarrolle un predicado que permita validar un NIP de una banco que 
% Responde a la siguiente gramatica
% Nip ::= <Digito> ' ' <Digito> ' ' <Digito> ' ' <Digito>
% Digito ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9


%nip("1235").
%true.

%nip("123").
%false.

latom_lstring([],[]).
latom_lstring([F|C],R) :- latom_lstring(C,S), atom_string(F,SF), append([SF],S,R).

preparar_string(Term,LS) :-
    atom(Term),
    atom_string(Term,Str),
    preparar_string(Str,LS).

preparar_string(Str,LS) :-
    string(Str),
    string_chars(Str,LAC),
    latom_lstring(LAC,LS).

digito(N) :-
        N == "0"; N == "1"; N == "2"; N == "3"; N == "4";
        N == "5"; N == "6"; N == "7"; N == "8"; N == "9".

nip(N) :- preparar_string(N,R), nip_a(R).
nip_a([F|C]) :- digito(F), nip_b(C).
nip_b([F|C]) :- digito(F), nip_c(C).
nip_c([F|C]) :- digito(F), nip_d(C).
nip_d([F|[]]) :- digito(F).


% Desarrolle un predicado que permita validar un octeto de una ip
% Responde a la siguiente gramatica
% Octeto ::= '2'<R5><R5> | '1'<Digito><Digito> | <Digito><Digito> | <Digito>
% R5 ::= 0 | 1 | 2 | 3 | 4 | 5
% Digito ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

r5(V) :-
        V == "0"; V == "1"; V == "2"; V == "3"; V == "4";
        V == "5".

ip(N) :- preparar_string(N,R), octeto(R).

octeto_f([F|[]]) :- digito(F).
octeto([F|[]]) :- digito(F).
octeto([F|C]) :- digito(F), octeto_f(C).
octeto([F|C]) :- F == "1", octeto(C).
octeto([F|C]) :- F == "2", octeto_r(C).
octeto_r([F|C]) :- r5(F), octeto_r(C).
octeto_r([F|[]]) :- r5(F).


%ip("255").
%true.
%ip("256").
%false
