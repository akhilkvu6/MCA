package com.example.integrated.app3.v1;
import android.os.Bundle;
import android.widget.Spinner;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    Spinner spProducts;
    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);
        spProducts = findViewById(R.id.spProducts);
    }
}