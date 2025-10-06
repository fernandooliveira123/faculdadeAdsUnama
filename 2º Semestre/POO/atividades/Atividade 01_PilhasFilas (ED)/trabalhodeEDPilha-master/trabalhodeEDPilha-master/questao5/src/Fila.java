public class Fila {
    private int[] elementos;
    private int inicio;
    private int fim;
    private int tamanho;
    private int capacidade;

    public Fila(int capacidade) {
        this.capacidade = capacidade;
        elementos = new int[capacidade];
        inicio = 0;
        fim = 0;
        tamanho = 0;
    }

    public void enqueue(int valor) {
        if (tamanho == capacidade) {
            System.out.println("Fila cheia. Não é possível adicionar " + valor);
            return;
        }
        elementos[fim] = valor;
        fim = (fim + 1) % capacidade;
        tamanho++;
    }

    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Fila vazia. Não é possível remover.");
            return -1;
        }
        int removido = elementos[inicio];
        inicio = (inicio + 1) % capacidade;
        tamanho--;
        return removido;
    }

    public int peek() {
        if (isEmpty()) {
            System.out.println("Fila vazia.");
            return -1;
        }
        return elementos[inicio];
    }

    public boolean isEmpty() {
        return tamanho == 0;
    }
}

