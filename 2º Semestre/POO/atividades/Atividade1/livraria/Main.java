public class Main {
    String titulo;
    int numeroPaginas;
    int anoPublicacao;
    double preco;

    void cadastrar() {
        System.out.println("Cadastrando no banco de dados...");
    }

    void vender() {
        System.out.println("Vendendo livro por R$ " + preco);
    }
}
