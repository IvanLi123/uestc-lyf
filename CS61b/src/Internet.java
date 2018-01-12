
import java.net.*;
import java.io.*;
class Internet {
 public static void main(String[] arg) throws Exception {
 URL u = new URL("http://www.1point3acres.com/bbs/");
 InputStream ins = u.openStream();
 InputStreamReader isr = new InputStreamReader(ins);
 BufferedReader whiteHouse = new BufferedReader(isr);
 System.out.println(whiteHouse.readLine());
 }
}