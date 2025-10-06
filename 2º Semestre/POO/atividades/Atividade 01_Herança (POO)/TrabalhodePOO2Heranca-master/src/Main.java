import Atividade2.Fornecedor;
import Atividade4.Carro;
import Atividade4.Moto;
import Atividade4.Veiculo;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        // Atividade 3
        Fornecedor fornecedor = new Fornecedor("Testando", "Rua Barão do Rio Branco, 3192", "91928344591", 5000.0f, 200.0f);

        System.out.println("Saldo atual do fornecedor: " + fornecedor.obterSaldo());
        System.out.println("Nome do fornecedor: " + fornecedor.getNome());
        // --------------------------------------------------------------

        // Atividade 4
        List<Veiculo> veiculos = new ArrayList<>();
        Carro carro1 = new Carro("Civic", "Honda", 4);
        Carro carro2 = new Carro("Gol", "Volkswagen", 2);
        Carro carro3 = new Carro("Corolla", "Toyota", 4);

        // Instanciando várias motos
        Moto moto1 = new Moto("CB 500", "Honda", 500);
        Moto moto2 = new Moto("Ninja ZX-6R", "Kawasaki", 636);
        Moto moto3 = new Moto("Fazer", "Yamaha", 250);
        veiculos.add(carro1);
        veiculos.add(carro2);
        veiculos.add(carro3);
        veiculos.add(moto1);
        veiculos.add(moto2);
        veiculos.add(moto3);

        for(var veiculo : veiculos) {
            veiculo.exibirInfo();
        }



        // --------------------------------------------------------------
    }
}
