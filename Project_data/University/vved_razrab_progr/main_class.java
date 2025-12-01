import java.util.ArrayList;
import java.util.List;

class Aquarium {
    private List<Fish> fishes;

    public Aquarium() {
        this.fishes = new ArrayList<>();
    }

    public void addFish(Fish fish) {
        fishes.add(fish);
    }

    public void printPredatorsOver100g() {
        System.out.println("Хищные рыбы > 100 гр:");
        for (Fish fish : fishes) {
            if (fish.getType().equalsIgnoreCase("хищная") && fish.getWeight() > 100) {
                System.out.println(fish);
            }
        }
    }

    public void printLongestFish() {
        Fish longest = null;
        for (Fish fish : fishes) {
            if (longest == null || fish.getSize().getLength() > longest.getSize().getLength()) {
                longest = fish;
            }
        }
        System.out.println("\nСамая длинная рыба:");
        System.out.println(longest);
    }
}

public class main_class {
    public static void main(String[] args) {
        Aquarium aquarium = new Aquarium();
        aquarium.addFish(new Fish("хищная", 150, new Size(5, 20)));
        aquarium.addFish(new Fish("мирная", 90, new Size(4, 15)));
        aquarium.addFish(new Fish("хищная", 200, new Size(6, 30)));
        aquarium.addFish(new Fish("мирная", 70, new Size(3, 15)));
        aquarium.addFish(new Fish("хищная", 50, new Size(4, 18)));
        aquarium.addFish(new Fish("нейтральная", 98, new Size(9, 13)));
        aquarium.addFish(new Fish("хищная", 270, new Size(21, 30)));
        aquarium.addFish(new Fish("мирная", 85, new Size(13, 11)));
        aquarium.addFish(new Fish("нейтральная", 52, new Size(14, 35)));

        aquarium.printPredatorsOver100g();
        aquarium.printLongestFish();
    }
}

class Size {
    private double width;
    private double length;

    public Size(double width, double length) {
        this.width = width;
        this.length = length;
    }

    public double getLength() {
        return length;
    }

    @Override
    public String toString() {
        return "Size: " + width + "cm x " + length + "cm";
    }
}

class Fish {
    private String type; // "хищная", "мирная"
    private double weight;
    private Size size;

    public Fish(String type, double weight, Size size) {
        this.type = type;
        this.weight = weight;
        this.size = size;
    }

    public String getType() {
        return type;
    }

    public double getWeight() {
        return weight;
    }

    public Size getSize() {
        return size;
    }

    @Override
    public String toString() {
        return "Fish: " + type + ", Weight: " + weight + "g, " + size;
    }
}