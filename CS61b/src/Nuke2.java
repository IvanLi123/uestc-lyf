import java.io.*;
public class Nuke2 {
public static void stringdel(String s){
		char[]ch=s.toCharArray();
		for(int i=0;i<ch.length;i++){
			if(i!=1)
				System.out.print(ch[i]);
		}
}
public static void main(String[] args) throws IOException{
	 BufferedReader keyboard ;
	    String inputLine;
	    keyboard = new BufferedReader(new InputStreamReader(System.in));
	    inputLine=keyboard.readLine();
	    stringdel(inputLine);
	    
}
}
