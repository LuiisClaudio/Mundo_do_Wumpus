:- dynamic inicio/2.
:- dynamic parede/2.
:- dynamic vazia/2.
:- dynamic inimigo/4. 
:- dynamic ouro/2.
:- dynamic pegar/2.
:- dynamic poco/2.
:- dynamic energia/1.
:- dynamic score/1.
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
:- dynamic powerup/2.
:- dynamic ouro/2.
:- dynamic inimigo/4.
:- dynamic ouviu_passos_inimigo/2.

%funcionou
adjacente(X, Y, XX, Y) :- XX is X+1, pode_ser_acessada(XX, Y).
adjacente(X, Y, XX, Y) :- XX is X-1, pode_ser_acessada(XX, Y).
adjacente(X, Y, X, YY) :- YY is Y+1, pode_ser_acessada(X, YY).
adjacente(X, Y, X, YY) :- YY is Y-1, pode_ser_acessada(X, YY).

%funcionou
pode_ser_acessada(X, Y) :- inicio(X, Y); vazia(X, Y); tem_inimigo(X, Y); ouro(X, Y); poco(X, Y);!. 


estado_atual_arqueiro(X, Y, Direcao, Energia, Score, Municao) :- local_arqueiro(X, Y, Direcao), energia(Energia), score(Score), municao(Municao), !.



%Percepcoes FUNCIONA
sentiu_brisa_poco(X, Y) :- adjacente(X, Y, XX, YY), poco(XX, YY), !. 
sentiu_brisa_poco() :- local_arqueiro(X, Y, _), sentiu_brisa_poco(X, Y), !.

pode_ter_poco(XX, YY) :- sentiu_brisa_poco(X, Y), adjacente(XX, YY, X, Y), !.

assert(pode_ter_poco(X, Y)) :- sentiu_brisa_poco(XX, YY), adjacente(X, Y, XX, YY), !.
sentiu_brisa_poco(X,Y) , adjacente(X,Y,XX,YY) :- assert(pode_ter_poco(XX,YY)).

sentiu_fedor(X, Y) :- adjacente(X, Y, XX, YY), inimigo(_, _, XX, YY), !.
sentiu_fedor() :- local_arqueiro(X, Y, _), sentiu_fedor(X, Y), !.

sentiu_alguma_coisa(X, Y) :- sentiu_brisa_poco(X, Y); sentiu_fedor(X, Y), !.
sentiu_alguma_coisa() :- local_arqueiro(X, Y, _), sentiu_alguma_coisa(X, Y), !.


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


%Atualiza todas as certezas do arqueiro

atualizar_certezas_inimigo() :- 
	inimigo(_, _, X, Y),
	pode_ter_inimigo(X, Y),
	XA is X+1, XB is X-1, YA is Y+1, YB is Y-1,
	(
		((parede(XA, Y));visitadas(XA,Y)),
		((parede(XB, Y));visitadas(XB,Y)),
		((parede(X, YA));visitadas(X,YA)),
		((parede(X, YB));visitadas(X,YB))
	),
	retractall(pode_ter_inimigo(X, Y)), assert(tem_inimigo(X, Y)).
	
	
atualizar_certezas_poco() :-
	poco(X, Y),
	pode_ter_poco(X, Y),
	XA is X+1, XB is X-1, YA is Y+1, YB is Y-1,
	(
		((parede(XA, Y));visitadas(XA,Y)),
		((parede(XB, Y));visitadas(XB,Y)),
		((parede(X, YA));visitadas(X,YA)),
		((parede(X, YB));visitadas(X,YB))
	),
	retractall(pode_ter_poco(X, Y)), assert(tem_poco(X, Y)).
	
atualizar_certezas_geral() :-
	(atualizar_certezas_inimigo();1=1),
	(atualizar_certezas_poco();1=1), !.

remover_incertezas_casa_atual() :- 
		local_arqueiro(X, Y, _),
		(
			((not(poco(X, Y)), assert(nao_tem_poco(X, Y)), retractall(pode_ter_poco(X, Y)));1=1),
			((not(inimigo(_, _, X, Y)), assert(nao_tem_inimigo(X, Y)), retractall(pode_ter_inimigo(X, Y)));1=1)
		), !.

atualizar_incertezas() :- (
		(remover_incertezas_casa_atual();1=1),
		((sentiu_brisa_poco(), descobre_poco_adjacente());1=1),
		(descobre_adjacente_pode_ter_inimigo();1=1),
		(( not(sentiu_brisa_poco()), remover_incertezas_pocos_adjacentes() );1=1),
		(remover_incertezas_inimigos_adjacentes() ;1=1),
		((atualizar_certezas_geral());1=1)
	), !.








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



%Atualiza pontuação

arqueiro_somar_score(SOM) :- score(C), CC is C+SOM, retract(score(C)), assert(score(CC)).
arqueiro_subtrair_score(SUB) :- SOM is SUB * -1, arqueiro_somar_score(SOM).

arqueiro_somar_energia(SOM) :- energia(E), EE is E+SOM, retract(energia(E)), assert(energia(EE)).
arqueiro_subtrair_energia(SUB) :- SOM is SUB * -1, arqueiro_somar_energia(SOM).


arqueiro_perdeu_municao() :- municao(Municao), NewAmmo is Municao - 1, retract(municao(Municao)), assert(municao(NewAmmo)), !.




%Parte que Kevin fez! Me explica depois please...
%nao(X):-\+X.

%adjacente(ponto(X,Y),ponto(XX,YY)):-(XX is X,YY is Y-1);(XX is X,YY is Y+1);(YY is Y,XX is X+1);(YY is Y,XX is X-1),!.

%pode_ter_poco(X,Y):-
%sentiu_brisa_poco(X1,Y1);adjacente(ponto(X1,Y1),ponto(X,Y)),!.

%naosafe(X,Y):-(nao(safo(X,Y)),nao(parede(X,Y)),pode_ter_inimigo(X,Y),pode_ter_poco(X,Y)).

