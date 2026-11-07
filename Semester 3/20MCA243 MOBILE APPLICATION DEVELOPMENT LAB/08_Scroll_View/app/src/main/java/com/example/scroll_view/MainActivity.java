package com.example.scroll_view;

import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        LinearLayout linearLayout = findViewById(R.id.linearLayoutContainer);

        for (int i = 1; i <= 25; i++) {
            TextView textView = new TextView(this);
            textView.setText("Scroll Item " + i + ": Android MCA Lab");
            textView.setTextSize(20);
            textView.setPadding(24, 24, 24, 24);
            linearLayout.addView(textView);
        }
    }
}
