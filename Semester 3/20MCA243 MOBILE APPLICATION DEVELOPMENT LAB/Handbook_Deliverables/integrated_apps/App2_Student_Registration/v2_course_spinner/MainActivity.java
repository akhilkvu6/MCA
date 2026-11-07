package com.example.integrated.app2.v2;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    Spinner spCourse;
    String[] courses = {"MCA", "M.Tech", "B.Tech", "MBA"};
    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);
        spCourse = findViewById(R.id.spCourse);
        ArrayAdapter<String> ad = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, courses);
        spCourse.setAdapter(ad);
    }
}