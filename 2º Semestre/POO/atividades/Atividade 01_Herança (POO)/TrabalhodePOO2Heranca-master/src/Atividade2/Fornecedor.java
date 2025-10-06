package Atividade2;

public class Fornecedor extends Pessoa{
    float valorCredito;
    float valorDivida;

    public Fornecedor() {
        super();
    }

    public Fornecedor(String nome, String endereco, String telefone, float valorCredtito, float valorDivida) {
        super(nome, endereco, telefone);
        this.valorCredito = valorCredtito;
        this.valorDivida = valorDivida;
    }

    public float getValorCredito() {
        return valorCredito;
    }

    public void setValorCredito(float valorCredito) {
        this.valorCredito = valorCredito;
    }

    public float getValorDivida() {
        return valorDivida;
    }

    public void setValorDivida(float valorDivida) {
        this.valorDivida = valorDivida;
    }

    public float obterSaldo() {
        if(this.valorDivida > valorCredito) {
            return this.valorDivida - this.valorCredito;
        }
        return this.valorCredito - this.valorDivida;
    }
}
