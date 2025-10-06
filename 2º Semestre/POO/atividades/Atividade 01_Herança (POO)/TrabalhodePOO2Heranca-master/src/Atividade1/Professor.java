package Atividade1;

public class Professor extends Pessoa {
    String especialidade;
    float salario;

    public void receberAumento(float aumento) {
        this.salario += aumento;
    }
}
