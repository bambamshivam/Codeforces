import java.io.*;
import java.util.*;

public class over {
    
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        OutputWriter out = new OutputWriter(System.out);
        // Always print a trailing "\n" and close the OutputWriter as shown at the end of your output
        
        // example:
        int t = scan.nextInt();
        while(t-->0){
			int n=scan.nextInt();
			int ar[]=new int[n];
			int d[]=new int[n];
			for(int i=0;i<n;i++){
				ar[i]=scan.nextInt();
				d[i]=0;
			}
			
			int i=0;
			int c=0;
			while(i<n){
				ArrayList<Integer> a=new ArrayList();
				int j=i;
				int f=0;
				while(j>=0 && j<n){
					if(d[j]==1)
						break;
					if(d[j]==-1){
						f=1;
						break;
					}
					d[j]=-1;
					a.add(j);
					j=j+ar[j];
				}
				if(f==0){
					for(int k=0;k<a.size();k++){
						d[a.get(k)]=1;
					}
					c+=a.size();
				}
				while(i<n && d[i]!=0){
					i+=1;
				}
			}
			out.print(c+"\n");
			int j=0;
			for(int k=0;k<c;k++){
				while(d[j]!=1){
					j+=1;
				}
				out.print((j+1)+" ");
				j+=1;
			}
			out.print("\n");
		}
        
        
        out.close();
    }

    // fast input
    static class Scanner {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public Scanner(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    String line = reader.readLine();
                    if (line == null)
                        return null;
                    tokenizer = new StringTokenizer(line);
                } catch (Exception e) {
                    throw(new RuntimeException());
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() { return Integer.parseInt(next()); }
        public long nextLong() { return Long.parseLong(next()); }
        public double nextDouble() { return Double.parseDouble(next()); }
    }

    // fast output
    static class OutputWriter {
        BufferedWriter writer;

        public OutputWriter(OutputStream stream) {
            writer = new BufferedWriter(new OutputStreamWriter(stream));
        }

        public void print(int i) throws IOException { writer.write(i); }
        public void print(String s) throws IOException { writer.write(s); }
        public void print(char[] c) throws IOException { writer.write(c); }
        public void close() throws IOException { writer.close(); }
    }


}