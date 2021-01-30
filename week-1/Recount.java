import java.util.*;

public class Recount {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		HashMap<String, int> recount = new HashMap<String, int>();
		
		while (scan.hasNextLine()) {
			String vote = scan.nextLine();
			
			if (recount.containsKey(vote))
				recount.put(vote, recount.get(vote)+1);
			else
				recount.put(vote, 1);
		}
		
		String maxName = "";
		int maxVotes = -1;
		boolean isRunoff = false;
		
		for(String key : recount.keySet()) {
			if (recount.get(key) > maxVotes) {
				maxName = key;
				maxVotes = recount.get(key);
				isRunoff = false;
			} else if (recount.get(key) == maxVotes) {
				isRunoff = true;
			}
		}
		
		if(isRunoff)
			System.out.println("Runoff!");
		else
			System.out.println(maxName);
	}
}