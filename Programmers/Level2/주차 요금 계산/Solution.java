import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        
        
        Map<String, ParkingData> cars = new TreeMap<>();
        
        for (String record: records) {
            String[] data = record.split(" ");
            String time = data[0];
            String carCode = data[1];
            String inAndOut = data[2];

            if (cars.getOrDefault(carCode, null) == null) {
                cars.put(carCode, new ParkingData());
            }
            ParkingData getData = cars.get(carCode);
            getData.setParkDate(inAndOut, time);
            cars.put(carCode, getData);

        }
        List<Integer> answer = new ArrayList<>();
        
        cars.entrySet().forEach(el -> answer.add(calFees(fees, el.getValue())));
        
        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
    
    public int calFees(int[] fees, ParkingData data) {
        int time = calTime(data.in, data.out) + data.time - fees[0];

        if (time<= 0) {
            return fees[1];
        } else {
            return fees[1] + (int)(Math.ceil((double)time / fees[2]) * fees[3]);
        }
    }
    
    public class ParkingData {
        String in = "";
        String out = "";
        int time = 0;
        
        public void setParkDate(String identify, String date) {
            if (identify.equals("IN")) {
                this.in = date;
                this.out = "23:59";
            } else {
                time += calTime(this.in, date);
                this.in = "00:00";
                this.out = "00:00";
            }
        }
    }
    
    public int calTime(String in, String out) {
        String[] inDate = in.split(":");
        int inHour = Integer.parseInt(inDate[0]);
        int inMinute = Integer.parseInt(inDate[1]);
        
        String[] outDate = out.split(":");
        int outHour = Integer.parseInt(outDate[0]);
        int outMinute = Integer.parseInt(outDate[1]);
        
        int hourToMinute = (outHour - inHour) * 60;
        int minute = outMinute - inMinute;
        
        return hourToMinute + minute;
    }
}
