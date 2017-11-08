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
:- dynamic arqueiro_location/3.
:- dynamic visitadas/2.
:- dynamic exiting/1.
:- dynamic caminhoAtual/1.
:- dynamic pode_ter_inimigo/2.
:- dynamic pode_ter_poco/2.
:- dynamic nao_tem_inimigo/2.
:- dynamic nao_tem_poco/2.
:- dynamic tem_inimigo/2.
:- dynamic tem_poco/2.

%Percepcoes
sentiu_brisa_poco(X, Y) :- adjacente(X, Y, XX, YY), poco(XX, YY), !.
sentiu_brisa_poco() :- arqueiro_location(X, Y, _), sentiu_brisa_poco(X, Y), !.

%Movimentos possíveis

proximo_movimento(sair) :- arqueiro_location(X, Y, _), inicio(X, Y), exiting(1), !.



proximo_movimento(morreu) :- energia(E), E < 1,format('Regra 1'), !.



proximo_movimento(pegar_ouro) :- arqueiro_location(X, Y, _), ouro(X, Y), retract(ouro(X, Y)), assert(vazia(X, Y)),
					     mario_somar_score(1000),format('Regra 2'), !. 


proximo_movimento(Acao) :- caminhoAtual([]), retract(caminhoAtual([])), proximo_movimento(Acao),format('Regra 3'), !.

proximo_movimento(girar) :- caminhoAtual([[X, Y]|_]), not(mario_andar_para(X, Y)), mario_girar(),format('Regra 4'), !.

proximo_movimento(andar) :- caminhoAtual([[X, Y]|T]), mario_andar_para(X, Y),
					 retractall(caminhoAtual(_)), assert(caminhoAtual(T)), mario_andar(X, Y),format('Regra 5'), !.



proximo_movimento(girar) :- mario_andar_para(X, Y), not(pode_ser_acessada(X, Y)), mario_girar(),format('Regra 6'), !.


proximo_movimento(andar) :- mario_andar_para(X, Y), pode_ser_acessada(X, Y), not(percebeu_algum_perigo()),
					 not(visitadas(X, Y)), mario_andar(X, Y),format('Regra 7'), !.
					 

proximo_movimento(girar) :- protagonista_location(X, Y, _), adjacente(X, Y, XX, YY), not(percebeu_algum_perigo()),
					   not(visitadas(XX,YY)), not(mario_andar_para(XX, YY)), mario_girar(),format('Regra 8'), !.



proximo_movimento(Acao) :- tomar_decisao_segura(), proximo_movimento(Acao), writef('Vai por um caminho seguro!\n'),format('Regra 9'), !.



proximo_movimento(Resultado) :- municao(A), A > 0, protagonista_location(X, Y, _), adjacente(X, Y, XX, YY), tem_inimigo(XX, YY), mario_andar_para(XX, YY),
					   energia(E), E > 50, writef('Vai atirar no inimigo!\n'), atirar(Resultado),format('Regra 10'), !.
				   
proximo_movimento(girar) :- municao(A), A > 0, protagonista_location(X, Y, _), adjacente(X, Y, XX, YY), tem_inimigo(XX, YY), not(mario_andar_para(XX, YY)),
					   energia(E), E > 50, mario_girar(),format('Regra 11'), !.
					   
proximo_movimento(Acao) :- municao(A), A > 0, energia(E), E > 50, tomar_decisao_lutar(), proximo_movimento(Acao), writef('Vai atirar no inimigo!\n'),format('Regra 12'), !.

	


proximo_movimento(andar) :- energia(E), E > 50, mario_andar_para(X, Y), pode_ter_inimigo(X, Y),
					 mario_andar(X, Y),format('Regra 13'), !.

proximo_movimento(girar) :- energia(E), E > 50, protagonista_location(CurX, CurY, _), adjacente(CurX, CurY, XX, YY),
					   pode_ter_inimigo(XX, YY), not(mario_andar_para(XX, YY)), mario_girar(),format('Regra 14'),!.
					   	 
proximo_movimento(Acao) :- energia(E), E > 50, tomar_decisao_pode_encontrar_inimigo(), proximo_movimento(Acao), writef('Vai arriscar inimigo!\n'),format('Regra 15'), !.
					   


proximo_movimento(pegar_power_up) :- protagonista_location(X, Y, _), pegar(X, Y), retract(pegar(X, Y)), assert(vazia(X, Y)),
					        mario_subtrair_score(1), mario_somar_energia(20),format('Regra 16'), !. 

proximo_movimento(Acao) :- tomar_decisao_pegar(), proximo_movimento(Acao), writef('Going to pick a power up!\n'),format('Regra 17'), !.



proximo_movimento(andar) :- score(C), C < 1, mario_andar_para(X, Y), pode_ter_poco(X, Y), mario_andar(X, Y), writef('Vai arriscar cair no poco!\n'),format('Regra 18'), !.
proximo_movimento(girar) :- score(C), C < 1, protagonista_location(X, Y, _), adjacente(X, Y, XX, YY), 
					   pode_ter_poco(XX, YY), not(mario_andar_para(XX, YY)), mario_girar(), writef('Vai arriscar cair no poco!\n'),format('Regra 19'), !.
proximo_movimento(Acao) :- score(C), C < 1, tomar_decisao_pode_cair_poco(), proximo_movimento(Acao), writef('Vai arriscar cair no poco!\n'),format('Regra 20'), !.



proximo_movimento(Acao) :- assert(exiting(1)), tomar_decisao_sair(), proximo_movimento(Acao), writef('Vai sair!\n'),format('Regra 21'), !.



pode_ter_poco(X,Y):-
	sentiu_brisa_poco(XX,YY); adjacente(XX,YY,X,Y)
pode_ter_inimigo(X,Y):-
	sentiu_fedor_inimigo(XX,YY) ; adjacente(XX,YY,X,Y)
	
adjacente(XX,YY,X,Y) :- (XX IS X +1 , XX IS X-1) ; (YY IS Y+1, YY IS Y-1)
