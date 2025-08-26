public class Main {
    public static void main(String[] args) throws Exception {
        ContaBancaria conta1 = new ContaBancaria();

        conta1.numeroConta = "93803-3";
        conta1.titular = "Felipe";

        conta1.depositar(2000);
        conta1.sacar(650);
        conta1.consultarSaldo();
    }
}
