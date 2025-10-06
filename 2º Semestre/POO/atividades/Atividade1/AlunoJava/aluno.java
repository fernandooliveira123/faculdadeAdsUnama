public class Aluno {
    public String nome;
    public String matricula;
    public double notaAv1;
    public double notaAv2;

    public String dadosAluno() {
        return "Aluno: \nNome: " + nome + "\nMatricula: " + matricula + "\nNota AV1: " + notaAv1 + "\nNota AV2: "
                + notaAv2 + "\n";
    }

    public double calcularMedia() {
        return (notaAv1 + notaAv2) / 2;
    }

    public void aprovado() {
        if (calcularMedia() >= 7) {
            System.out.println("Aluno aprovado! \n");
        } else if (calcularMedia() >= 4) {
            System.out.println("Aluno vai pra prova final \n");
        } else {
            System.out.println("Aluno reprovado \n");
        }
    }
}
