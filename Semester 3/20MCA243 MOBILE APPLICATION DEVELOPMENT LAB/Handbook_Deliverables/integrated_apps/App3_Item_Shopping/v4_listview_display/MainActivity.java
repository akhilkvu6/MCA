package com.example.integrated.app3.v4;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    ListView lvCart;
    ArrayList<String> cartItems = new ArrayList<>();
    ArrayAdapter<String> adapter;

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);
        lvCart = findViewById(R.id.lvCart);
        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, cartItems);
        lvCart.setAdapter(adapter);
    }
}