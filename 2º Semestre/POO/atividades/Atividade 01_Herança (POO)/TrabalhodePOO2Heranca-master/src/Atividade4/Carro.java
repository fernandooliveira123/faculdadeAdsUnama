package Atividade4;

public class Carro extends Veiculo{
    int quantidadePortas;

    public Carro(int quantidadePortas) {
        super();
        this.quantidadePortas = quantidadePortas;
    }

    public Carro(String modelo, String marca, int quantidadePortas) {
        super(modelo, marca);
        this.quantidadePortas = quantidadePortas;
    }

    public int getQuantidadePortas() {
        return quantidadePortas;
    }

    public void setQuantidadePortas(int quantidadePortas) {
        this.quantidadePortas = quantidadePortas;
    }
}
