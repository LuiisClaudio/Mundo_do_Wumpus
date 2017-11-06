import org.jpl7.*;
import java.util.Map;

public class Integracao_Prolog {
private static Query q1 = new Query("consult", new Term[] {new Atom("database.pl")});
	
	public Integracao_Prolog() {
		System.out.println( "consult " + (q1.hasSolution() ? "succeeded" : "failed"));
        
        Map<String, Term> esvaziarMapa = fazQuery("mario_esvaziamapa().");
        Query consultaMapa = new Query("consult", new Term[] {new Atom("map.pl")});
        
        if(!consultaMapa.hasSolution()) {
            return;
        }
        
        Map<String, Term> reset = fazQuery("mario_reset().");
        
        if(esvaziarMapa == null ||reset == null)
        {
            System.out.println("NULL");
            return;
        }

	}

	public void getNextMove(Arqueiro arqueiro) {
		
		Map<String, Term> s = fazQuery("estado_atual_mario(X,Y,Direcao,Score,Energia,Municao)");
		System.out.println(s.get("X").toString());
		System.out.println(s.get("Y").toString());
		System.out.println(s.get("Direcao").toString());
		System.out.println(s.get("Score").toString());
		System.out.println(s.get("Energia").toString());
		System.out.println(s.get("Municao").toString());
		
		Map<String, Term> solution = fazQuery("proximo_movimento(Acao).");
		
		if(solution == null) {
			System.out.println("NULL");
			return;
		}
		String action = solution.get("Acao").toString();
		
		System.out.println(action);
		
		switch(action) {
			case "girar":
				arqueiro.mudaDirecao();
				break;
			case "atacou_nao_matou":
				arqueiro.ataca();
				break;
			case "andar":
				System.out.println("Andou");
				arqueiro.andar();
				break;
			case "pegar_ouro":
				arqueiro.pegar(1000);
				break;
			case "pegar_power_up":
				arqueiro.pegar(20);
				break;
			case "morreu":
				System.out.println("BUSTED");
				System.exit(1);
			case "matou":
				arqueiro.matar();
				break;
			case "sair":
				System.out.println("GANHOU");
				System.out.println(arqueiro.energia);
				System.exit(1);
			default:
				System.out.println("ACTION INVALIDA");
				System.out.println(action);
				System.exit(1);
		}
		
		
	}
	
	public Map<String, Term> fazQuery(String query) {
		Query q3 = new Query(query);
		Map<String, Term> solution = q3.oneSolution();
		
		if(solution == null) {
			System.out.println("NULL");
			return null;
		}
		
		return solution;
	}
}
