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
:- dynamic sentiu_brisa/2.
:- dynamic estado/3.
:- dynamic sentiu_fedor_in/2.

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

adjacente(X, Y, XX, Y) :- XX is X+1, pode_ser_acessada(XX, Y).

inimigo_a_frente(X, Y, D) :- T is X -1, D == norte, tem_inimigo(T, Y).
inimigo_a_frente(X, Y, D) :- T is X + 1, D == sul, tem_inimigo(T, Y).
inimigo_a_frente(X, Y, D) :- T is Y - 1, D == leste, tem_inimigo(X, T).
inimigo_a_frente(X, Y, D) :- T is Y + 1, D == oeste, tem_inimigo(X, T).

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


%descorbertas

descobre_pode_ter_poco(X, Y) :- not(visitadas(X, Y)), not(nao_tem_poco(X, Y)), assert(pode_ter_poco(X, Y)), !.

descobre_pode_ter_inimigo(X, Y) :- not(visitadas(X, Y)), not(tem_inimigo(X, Y)), not(nao_tem_inimigo(X, Y)), assert(pode_ter_inimigo(X, Y)), !.



muda_estado(X,Y) :- estado(X,Y,V), Z is V+1, retract(estado(X,Y,V)), assert(estado(X,Y,Z)).
tem_poco(X,Y) :- local_arqueiro(X,Y,_), poco(X,Y), !.
tem_ouro(X,Y) :- local_arqueiro(X,Y,_), ouro(X,Y), !.
tem_inimigo(X,Y) :- local_arqueiro(X,Y,_), inimigo(_,_,X,Y), !.
