import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ParkingLotTest {

    @Test
    public void testIfFunctionExists() {
        ParkingLot lot = new ParkingLot();
        int result = lot.enterCar(); 
        assertTrue(result >= 1 || result == -1);
    }

    @Test
    public void testIfParkingHasFreeSlot() {
        ParkingLot lot = new ParkingLot();
        boolean result = lot.hasFreeSlot();
        assertEquals(true, result);
    }

    @Test
    public void testWhenCarLeavesTheLot() {
        ParkingLot lot = new ParkingLot();
        lot.enterCar();
        boolean result = lot.leaveCar(1);
        assertEquals(true, result);
    }

    @Test
    public void testForEmptySlot() {
        ParkingLot lot = new ParkingLot();
        int emptyCount = 0;
        for (int slot : lot.getSlots()) {
            if (slot == 0) emptyCount++;
        }
        assertEquals(20, emptyCount);
    }

    @Test
    public void testWhenLotIsFilledUp() {
        ParkingLot lot = new ParkingLot();
        for (int i = 0; i < 20; i++) {
            lot.enterCar();
        }
        int result = lot.enterCar();
        assertEquals(-1, result);
    }

    @Test
    public void testForInvalidSlot() {
        ParkingLot lot = new ParkingLot();
        boolean resultLow = lot.leaveCar(0);
        boolean resultHigh = lot.leaveCar(21);
        assertEquals(false, resultLow);
        assertEquals(false, resultHigh);
    }
}
