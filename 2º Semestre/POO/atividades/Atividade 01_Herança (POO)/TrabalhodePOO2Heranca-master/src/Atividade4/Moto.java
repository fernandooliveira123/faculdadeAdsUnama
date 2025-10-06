package Atividade4;

public class Moto extends Veiculo{
    int cilindradas;

    public Moto(int cilindradas) {
        super();
        this.cilindradas = cilindradas;
    }

    public Moto(String modelo, String marca, int cilindradas) {
        super(modelo, marca);
        this.cilindradas = cilindradas;
    }

    public int getCilindradas() {
        return cilindradas;
    }

    public void setCilindradas(int cilindradas) {
        this.cilindradas = cilindradas;
    }
}
