package com.example.integrated.app3.v2;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText etQty;
    TextView tvTotal;
    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);
        etQty = findViewById(R.id.etQty);
        tvTotal = findViewById(R.id.tvTotal);
    }
}