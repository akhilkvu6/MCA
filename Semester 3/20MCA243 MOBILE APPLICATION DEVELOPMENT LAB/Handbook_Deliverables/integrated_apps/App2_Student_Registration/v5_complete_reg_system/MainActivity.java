package com.example.integrated.app2.v5;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    EditText etName, etRoll, etAge;
    Spinner spCourse;
    RadioGroup rgGender;
    CheckBox cbWeb, cbMobile, cbAI;
    Button btnRegister;

    String[] courses = {"MCA (Master of Computer Applications)", "M.Tech CSE", "B.Tech CSE"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etName = findViewById(R.id.etName);
        etRoll = findViewById(R.id.etRoll);
        etAge = findViewById(R.id.etAge);
        spCourse = findViewById(R.id.spCourse);
        rgGender = findViewById(R.id.rgGender);
        cbWeb = findViewById(R.id.cbWeb);
        cbMobile = findViewById(R.id.cbMobile);
        cbAI = findViewById(R.id.cbAI);
        btnRegister = findViewById(R.id.btnRegister);

        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, courses);
        spCourse.setAdapter(adapter);

        btnRegister.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name = etName.getText().toString().trim();
                String roll = etRoll.getText().toString().trim();
                String age = etAge.getText().toString().trim();

                if (name.isEmpty() || roll.isEmpty() || age.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Fill required fields", Toast.LENGTH_SHORT).show();
                    return;
                }

                int genderId = rgGender.getCheckedRadioButtonId();
                String gender = genderId != -1 ? ((RadioButton) findViewById(genderId)).getText().toString() : "Not Specified";
                String course = spCourse.getSelectedItem().toString();

                ArrayList<String> skills = new ArrayList<>();
                if (cbWeb.isChecked()) skills.add("Web");
                if (cbMobile.isChecked()) skills.add("Mobile");
                if (cbAI.isChecked()) skills.add("AI");

                Intent intent = new Intent(MainActivity.this, StudentSummaryActivity.class);
                intent.putExtra("NAME", name);
                intent.putExtra("ROLL", roll);
                intent.putExtra("COURSE", course);
                intent.putExtra("GENDER", gender);
                intent.putStringArrayListExtra("SKILLS", skills);
                startActivity(intent);
            }
        });
    }
}