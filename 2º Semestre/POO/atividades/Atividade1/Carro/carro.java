public class Carro {
    public String marca;
    public String modelo;
    public int ano;

    public void carrodados() {
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Ano: " + ano);
    }

    public void ligar() {
        System.out.println("O carro " + modelo + " está ligado!");
    }
}
