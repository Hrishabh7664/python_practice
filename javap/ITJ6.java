//a runner runs 15 km in 50 min 30 secs write a java program that displays average speed in miles per hour



public class ITJ6{
    public static void main(String[] args) {
        float time = 50.03f/60;
        int distanceKM = 15;
        float distanceMILE = distanceKM/1.6f;
        float speed = distanceMILE/time;

        System.out.println("speed of the car is:"+speed);

    }
}
