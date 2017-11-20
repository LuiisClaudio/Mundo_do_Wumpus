:- dynamic inicio/2.
:- dynamic parede/2.
:- dynamic vazia/2.
:- dynamic inimigo/4. 
:- dynamic ouro/2.
:- dynamic pegar/2.
:- dynamic poco/2.
:- dynamic energia/1.
:- dynamic pontuacao/1.
:- dynamic municao/1.
:- dynamic local_arqueiro/3.
:- dynamic visitadas/2.
:- dynamic exiting/1.
:- dynamic caminhoAtual/1.
:- dynamic pode_ter_inimigo/2.
:- dynamic pode_ter_poco/2.
:- dynamic nao_tem_inimigo/2.
:- dynamic nao_tem_poco/2.
:- dynamic tem_inimigo/2.
:- dynamic tem_poco/2.
:- dynamic inicio/2.
:- dynamic ouro/2.
:- dynamic inimigo/4.
:- dynamic ouviu_passos_inimigo/2.
:- dynamic seguro/2.



%funcionou
adjacente(X, Y, XX, Y) :- XX is X+1, pode_ser_acessada(XX, Y).
adjacente(X, Y, XX, Y) :- XX is X-1, pode_ser_acessada(XX, Y).
adjacente(X, Y, X, YY) :- YY is Y+1, pode_ser_acessada(X, YY).
adjacente(X, Y, X, YY) :- YY is Y-1, pode_ser_acessada(X, YY).

%funcionou
pode_ser_acessada(X, Y) :- inicio(X, Y); vazia(X, Y); tem_inimigo(X, Y); ouro(X, Y); poco(X, Y);!. 

mesmo_local_inimigo(X,Y) :- inimigo(_, _, XX, YY), local_arqueiro(X, Y, _), !.


deu_dano(X, Y, D, Z, W) :- X > Z, Y == W,  D == norte.
deu_dano(X, Y, D, Z, W) :- X < Z, Y == W,  D == sul.
deu_dano(X, Y, D, Z, W) :- Y < W, X == Z,  D == leste.
deu_dano(X, Y, D, Z, W) :- Y < W, X == Z,  D == oeste.

estado_atual_arqueiro(X, Y, Direcao, Energia, Pontuacao, Municao) :- local_arqueiro(X, Y, Direcao), energia(Energia), pontuacao(Pontuacao), municao(Municao), !.



%Percepcoes FUNCIONA
sentiu_brisa_poco(X, Y) :- adjacente(X, Y, XX, YY), poco(XX, YY), !. 


sentiu_fedor(X, Y) :- adjacente(X, Y, XX, YY), inimigo(_, _, XX, YY), !.

sentiu_alguma_coisa(X, Y) :- sentiu_brisa_poco(X, Y); sentiu_fedor(X, Y), !.


%Movimentos
%Funciona
arqueiro_andar_direcao(X, Y) :- local_arqueiro(XX, YY, Direcao), Y is YY-1, XX = X, Direcao=norte, !.
arqueiro_andar_direcao(X, Y) :- local_arqueiro(XX, YY, Direcao), X is XX+1, YY = Y, Direcao=leste, !.
arqueiro_andar_direcao(X, Y) :- local_arqueiro(XX, YY, Direcao), Y is YY+1, XX = X, Direcao=sul, !.
arqueiro_andar_direcao(X, Y) :- local_arqueiro(XX, YY, Direcao), X is XX-1, YY = Y, Direcao=oeste, !.


%Base de conhecimento

%descorbertas

descobre_pode_ter_poco(X, Y) :- not(visitadas(X, Y)), not(nao_tem_poco(X, Y)), assert(pode_ter_poco(X, Y)), !.

descobre_pode_ter_inimigo(X, Y) :- not(visitadas(X, Y)), not(tem_inimigo(X, Y)), not(nao_tem_inimigo(X, Y)), assert(pode_ter_inimigo(X, Y)), !.


descobre_adjacente_pode_ter_poco() :-
	local_arqueiro(X, Y, _),
	(( XX is X+1, adjacente(X, Y, XX, Y), descobre_pode_ter_poco(XX, Y) );1=1),
	(( XXX is X-1, adjacente(X, Y, XXX, Y), descobre_pode_ter_poco(XXX, Y) );1=1),
	(( YY is Y+1, adjacente(X, Y, X, YY), descobre_pode_ter_poco(X, YY) );1=1),
	(( YYY is Y-1, adjacente(X, Y, X, YYY), descobre_pode_ter_poco(X, YYY) );1=1), !.


descobre_adjacente_pode_ter_inimigo() :-
	local_arqueiro(X, Y, _),
	(( XX is X+1, adjacente(X, Y, XX, Y), descobre_pode_ter_inimigo(XX, Y) );1=1),
	(( XXX is X-1, adjacente(X, Y, XXX, Y), descobre_pode_ter_inimigo(XXX, Y) );1=1),
	(( YY is Y+1, adjacente(X, Y, X, YY), descobre_pode_ter_inimigo(X, YY) );1=1),
(( YYY is Y-1, adjacente(X, Y, X, YYY), descobre_pode_ter_inimigo(X, YYY) );1=1), !.







remover_incerteza_poco_adjacente(X, Y) :- assert(nao_tem_poco(X, Y)), retractall(pode_ter_poco(X, Y)), !.	
remover_incertezas_inimigos_adjacentes(X, Y) :- assert(nao_tem_inimigo(X, Y)), retractall(pode_ter_inimigo(X, Y)), !.

remover_incertezas_pocos_adjacentes() :-
	local_arqueiro(X, Y, _),
	(( XX is X+1, adjacente(X, Y, XX, Y), remover_incerteza_poco_adjacente(XX, Y) );1=1),
	(( XXX is X-1, adjacente(X, Y, XXX, Y), remover_incerteza_poco_adjacente(XXX, Y) );1=1),
	(( YY is Y+1, adjacente(X, Y, X, YY), remover_incerteza_poco_adjacente(X, YY) );1=1),
	(( YYY is Y-1, adjacente(X, Y, X, YYY), remover_incerteza_poco_adjacente(X, YYY) );1=1), !.


remover_incertezas_inimigos_adjacentes() :-
	local_arqueiro(X, Y, _),
	(( XX is X+1, adjacente(X, Y, XX, Y), remover_incertezas_inimigos_adjacentes(XX, Y) );1=1),
	(( XXX is X-1, adjacente(X, Y, XXX, Y), remover_incertezas_inimigos_adjacentes(XXX, Y) );1=1),
	(( YY is Y+1, adjacente(X, Y, X, YY), remover_incertezas_inimigos_adjacentes(X, YY) );1=1),
	(( YYY is Y-1, adjacente(X, Y, X, YYY), remover_incertezas_inimigos_adjacentes(X, YYY) );1=1), !.

tem_poco(X,Y) :- local_arqueiro(X,Y,_), poco(X,Y), !.
tem_ouro(X,Y) :- local_arqueiro(X,Y,_), ouro(X,Y), !.
tem_inimigo(X,Y) :- local_arqueiro(X,Y,_), inimigo(_,_,X,Y), !.
