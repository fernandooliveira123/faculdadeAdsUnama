public class Cliente {
    String nome;
    String email;
    String telefone;

    void cadastrar() {
        System.out.println("Cliente cadastrado com sucesso ");
    }

    void comprar() {
        System.out.println(nome + " realizou uma compra!");
    }
    void email() {
        System.out.println("Email do cliente: " + email);
    }
    void telefone() {
        System.out.println("Telefone do cliente: " + telefone);
    }
}
