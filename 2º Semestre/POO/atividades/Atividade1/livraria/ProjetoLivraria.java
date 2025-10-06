public class ProjetoLivraria {
    public static void main(String[] args) {
        
        Livro obj1 = new Livro();
        Livro obj2 = new Livro();

      
        obj1.titulo = "Vire o jogo- Dave Spray";
        obj1.numeroPaginas = 178;
        obj1.anoPublicacao = 2012;
        obj1.preco = 89.99;

        obj2.titulo = "Mãos à obra- Aprendizado de máquina com Scikit Learn, keras & TensorFlow: Conceitos, ferramentas e técnicas para a Construção de Sistemas Inteligentes.";
        obj2.numeroPaginas = 640;
        obj2.anoPublicacao = 2021
;
        obj2.preco = 86.90;

        
        System.out.println("Livro 1: " + obj1.titulo + " - R$ " + obj1.preco);
        System.out.println("Livro 2: " + obj2.titulo + " - R$ " + obj2.preco);

        
        obj1.cadastrar();
        obj1.vender();
    }
}
