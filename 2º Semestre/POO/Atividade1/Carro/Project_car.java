public class Project_car {
    public static void main(String[] args) {
        Carro carro1 = new Carro();
        carro1.marca = "Toyota";
        carro1.modelo = "Corolla";
        carro1.ano = 2024;

        Carro carro2 = new Carro();
        carro2.marca = "Honda";
        carro2.modelo = "Civic";
        carro2.ano = 2015;

        carro2.modelo = "Civic Turbo";
        carro2.ano = 2023;

        carro1.carrodados();
        carro1.ligar();

        carro2.carrodados();
        carro2.ligar();
    }
}
