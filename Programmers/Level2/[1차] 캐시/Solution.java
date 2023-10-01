import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        Map<String, String> cache = new LinkedHashMap<>();
    
        for (int citiesIdx = 0; citiesIdx < cities.length; citiesIdx++) {
            String city = getCity(cities[citiesIdx]);
            if (cache.getOrDefault(city, null) != null) {
                answer += 1;
                cache.remove(city);
                cache.put(city, city);
                continue;
            }
            
            answer += 5;
            
            if (cache.size() == cacheSize && cache.size() > 0) {
                String first = cache.keySet().iterator().next();
                cache.remove(first);
            } 
            if (cache.size() < cacheSize) {
                cache.put(city,city);    
            }
            
        }
        return answer;
    }
    
    public String getCity(String city) {
        return city.toLowerCase();
    } 
}
