public class MarginCalculator {

    // Kalkuliert den Gewinn pro Container (Türkei -> DE) inklusive Provision
    public static void calculateOrder(int stueckzahl, double einkaufspreisProBecher, double verkaufspreisProBecher) {
        double gesamtEinkauf = stueckzahl * einkaufspreisProBecher;
        double gesamtVerkauf = stueckzahl * verkaufspreisProBecher;
        
        // Logistik-Pauschale (Schiffscontainer / LKW-Transit)
        double frachtkosten = 2500.00; 
        double margeGesamt = gesamtVerkauf - gesamtEinkauf - frachtkosten;
        
        // Deine Vermittler-Provision (z.B. 5% vom Gesamt-Verkaufsumsatz)
        double deineProvision = gesamtVerkauf * 0.05; 

        System.out.println("=== LOGISTIK & MARGEN BERECHNUNG ===");
        System.out.println("Becher-Anzahl: " + stueckzahl + " Stück");
        System.out.println("Gesamter Verkaufsumsatz: " + gesamtVerkauf + " €");
        System.out.println("Netto-Marge Großhändler: " + margeGesamt + " €");
        System.out.println("Deine Vermittler-Provision: " + deineProvision + " €");
    }

    public static void main(String[] args) {
        // Beispiel: 1 Container = 500.000 Becher
        calculateOrder(500000, 0.015, 0.035);
    }
}
