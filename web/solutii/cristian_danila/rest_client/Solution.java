import org.json.JSONObject;

import javax.print.DocFlavor;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class NetClientGet {

    public static void main(String[] args) {

        try {

            // do a get request for all the users
            String[] resources = new String[] {"posts", "comments", "albums", "photos", "todos", "users"};

            for (String resource : resources) {

                URL url = new URL("http://jsonplaceholder.typicode.com/" + resource);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");
                conn.setRequestProperty("Accept", "application/json");

                if (conn.getResponseCode() != 200) {
                    throw new RuntimeException("Failed : HTTP error code : "
                            + conn.getResponseCode());
                }

                BufferedReader br = new BufferedReader(new InputStreamReader(
                        (conn.getInputStream())));

                String output;
                String finalOutput = null;
//                System.out.println("Output from Server .... \n");
                while ((output = br.readLine()) != null) {
//                    System.out.println(output);
                    finalOutput += output;
                }

//                JSONObject serverOutput = new JSONObject(finalOutput);

                conn.disconnect();
            }


            // prepare some data for the post request
            String newPost = "{\"userId\":1, \"title\":\"dsfsdsdfsd\", \"body\":\"dsfsdsdf\"}";
            String newComment = "{\"userId\":1, \"title\":\"dsfsdsdfsd\", \"body\":\"dsfsdsdf\", \"email\":\"dsfsdfsdf@fsdfsdf.sdfsdf\"}";
            String newAlbum = "{\"userId\": 1, \"title\": \"dsfsfdsfsddsf\"}";

            // we won't take care of all the cases, just some basic resources
            String[] resourcesPost = new String[] {"posts", "comments", "albums"};

            String input = null;
            for (int i = 0; i < 3; ++i) {

                if (i == 0) {
                    input = newPost;
                } else if (i == 1) {
                    input = newComment;
                } else {
                    input = newAlbum;
                }

                URL url = new URL("http://jsonplaceholder.typicode.com/" + resourcesPost[i]);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setDoOutput(true);
                conn.setRequestMethod("POST");
                conn.setRequestProperty("Content-Type", "application/json");

                OutputStream os = conn.getOutputStream();
                os.write(input.getBytes());
                os.flush();

                if (conn.getResponseCode() != HttpURLConnection.HTTP_CREATED) {
                    throw new RuntimeException("Failed : HTTP error code : "
                            + conn.getResponseCode());
                }

                BufferedReader br = new BufferedReader(new InputStreamReader(
                        (conn.getInputStream())));

                String output;
                System.out.println("Output from Server .... \n");
                while ((output = br.readLine()) != null) {
                    System.out.println(output);
                }

                conn.disconnect();
            }

        } catch (MalformedURLException e) {

            e.printStackTrace();

        } catch (IOException e) {

            e.printStackTrace();
        }
    }
}