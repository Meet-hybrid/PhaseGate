import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ParkingLot lot = new ParkingLot();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("\nHello " + name.toUpperCase() + "! Get ready to begin");
        System.out.println("Press ENTER to start\n");
        scanner.nextLine();

        while (true) {
            System.out.println("""
            =======================================================================
            | Welcome to HYBRID'S parking lot service. Choose a number (1 - 5):   |
            | 1: Check if there's an available slot                               |
            | 2: Book for a parking slot                                          |
            | 3: Leave a parking slot                                             |
            | 4: Book for a future parking slot                                   |
            | 5: Exit the app                                                     |
            =======================================================================
            """);

            System.out.print("Enter your choice: ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    boolean available = lot.hasFreeSlot();
                    if (available) {
                        System.out.println("A slot is available.");
                    } else {
                        System.out.println("No slots available.");
                    }
                    break;

                case "2":
                    int slot = lot.enterCar();
                    if (slot != -1) {
                        System.out.println("Car parked in slot " + slot);
                    } else {
                        System.out.println("Parking lot is full.");
                    }
                    break;

                case "3":
                    System.out.print("Enter slot number to leave: ");
                     {
                        int slotNumber = Integer.parseInt(scanner.nextLine());
                        boolean result = lot.leaveCar(slotNumber);
                        if (result) {
                            System.out.println("Car left slot " + slotNumber);
                        } else {
                            System.out.println("Invalid or empty slot.");
                        }
                    }  (NumberFormatException e) {
                        System.out.println("Please enter a valid number.");
                    }
                    break;

                case "4":
                    System.out.println("Future booking feature coming soon!");
                    break;

                case "5":
                    System.out.println("Goodbye!");
                    return;

                default:
                    System.out.println("Invalid choice. Please select between 1 and 5.");
            }
        }
    }
}
