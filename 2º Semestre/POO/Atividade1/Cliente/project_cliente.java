public class project_cliente {
    public static void main(String[] args) {
        Cliente cliente1 = new Cliente();
        cliente1.nome = "Fernando Oliveira";
        cliente1.email = "fernando_ibp@hotmail.com";
        cliente1.telefone = "91983259001";

        cliente1.cadastrar();
        cliente1.comprar();
        cliente1.email();
        cliente1.telefone();
    }
}
