//ENTRADA E SAÍDA DE DADOS COM MÉTODO SCANNER
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        System.out.println("Qual seu nome?");
        String nome = teclado.nextLine();
        
        System.out.println("Qual seu Salario?");
        float salario = teclado.nextFloat();
        
        

        System.out.println("Seu nome é:" + nome + " Seu salario é:" + salario);
    }

}
