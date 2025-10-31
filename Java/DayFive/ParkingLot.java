public class ParkingLot {
    private int[] slots;

    public ParkingLot() {
        this.slots = new int[20];
    }

    public boolean hasFreeSlot() {
        for (int slot : slots) {
            if (slot == 0) return true;
        }
        return false;
    }

    public int enterCar() {
        for (int number = 0; number < slots.length; number++) {
            if (slots[number] == 0) {
                slots[number] = 1;
                return number + 1;
            }
        }
        return -1;
    }

    public boolean leaveCar(int slotNumber) {
        if (slotNumber >= 1 && slotNumber <= slots.length) {
            if (slots[slotNumber - 1] == 1) {
                slots[slotNumber - 1] = 0;
                return true;
            }
        }
        return false;
    }

    public int[] getSlots() {
        return slots;
    }
}
