public class Hero {
    String name;
    int hp;

    
    public Hero(String name, int hp) {
        this.name = name;
        this.hp = hp;
    }

    
    public void take_damage(int amount) {
        hp -= amount;
    }

    public static void main(String[] args) {
        
        Hero Arthur = new Hero("Arthur", 100);
        Hero Morgana = new Hero("Morgana", 100);

        
        Arthur.take_damage(10);

        
        System.out.println(Arthur.name + " HP: " + Arthur.hp);
        System.out.println(Morgana.name + " HP: " + Morgana.hp);
    }
}
