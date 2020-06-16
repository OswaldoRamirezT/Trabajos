% Desarrollo una gramatica bnf (como la del video) para validar una 
% direccion ipv4 asi como una mascara de red.
% https://es.wikipedia.org/wiki/M%C3%A1scara_de_red#Tabla_de_m%C3%A1scaras_de_red
% Realice la implementacion de dicha gramatica en prolog donde
% se pueda validar la cadena donde esta esa ip o mascara ejemplo

%ip("192.168.1.1").
%true.
%ip("256.168.1.1").
%false.
%maskR("255.255.255.0").
%true.
%maskR("255.255.255.1").
%false.

latom_lstring([],[]).
latom_lstring([F|C],R) :- latom_lstring(C,S), atom_string(F,SF), append([SF],S,R).

preparar_string(Str,LS) :-
    string(Str),
    string_chars(Str,LAC),
    latom_lstring(LAC,LS).


ip(D) :- split_string(D, ".", "", R), direccion(R).
direccion([F|[]]):- preparar_string(F,R), ipv(R).
direccion([F|C]):- preparar_string(F,R), ipv(R), direccion(C).

ipv_f([F|[]]) :- digito(F).
ipv([F|[]]) :- digito(F).
ipv([F|C]) :- digito(F), ipv_f(C).
ipv([F|C]) :- F == "1", ipv(C).
ipv([F|C]) :- F == "2", ipv_r(C).
ipv_r([F|C]) :- r5(F), ipv_r(C).
ipv_r([F|[]]) :- r5(F).

digito(N) :-
        N == "0"; N == "1"; N == "2"; N == "3"; N == "4";
        N == "5"; N == "6"; N == "7"; N == "8"; N == "9".

r5(V) :-
        V == "0"; V == "1"; V == "2"; V == "3"; V == "4";
        V == "5".


maskR(D) :- split_string(D, ".", "", R), mascara(R).
mascara(R):- mask(R).

mask([F|[]]):- oct(F).
mask([F|C]):- oct(F), mask(C).
mask([F|[]]) :- octeto(F).
mask([F|C]) :- octeto(F), mask_f(C).
mask_f([F|[]]) :- cero(F).
mask_f([F|C]) :- cero(F),mask(C).


oct(D) :- D=="255".
octeto(D) :-D=="0"; D=="128"; D=="192"; D=="224"; D=="240"; D=="248"; D=="252"; D=="254". 
cero(D) :- D=="0".