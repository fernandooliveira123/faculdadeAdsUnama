public class Main {
    public static void main(String[] args) {
        Fila fila = new Fila(5);
        fila.enqueue(10);
        fila.enqueue(20);
        fila.enqueue(30);

        System.out.println("Primeiro elemento: " + fila.peek());

        while (!fila.isEmpty()) {
            System.out.println("Removido: " + fila.dequeue());
        }
    }
}
