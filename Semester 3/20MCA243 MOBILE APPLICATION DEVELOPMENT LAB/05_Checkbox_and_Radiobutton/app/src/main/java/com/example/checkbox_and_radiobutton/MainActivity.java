package com.example.checkbox_and_radiobutton;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    Button b1;
    RadioGroup rg;
    RadioButton r1, r2;
    CheckBox e, m, h;
    TextView t;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        b1 = findViewById(R.id.submit);

        r1 = findViewById(R.id.male);
        r2 = findViewById(R.id.female);

        e = findViewById(R.id.e);
        m = findViewById(R.id.m);
        h = findViewById(R.id.h);

        t = findViewById(R.id.tv);
        rg = findViewById(R.id.rg);

        // Gender Toast (Optional live feedback)
        rg.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                if (checkedId == R.id.male) {
                    Toast.makeText(MainActivity.this, "Male", Toast.LENGTH_SHORT).show();
                } else if (checkedId == R.id.female) {
                    Toast.makeText(MainActivity.this, "Female", Toast.LENGTH_SHORT).show();
                }
            }
        });

        // Submit Button
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String result = "";

                // 1. Get Selected Gender
                int selectedGenderId = rg.getCheckedRadioButtonId();
                if (selectedGenderId != -1) {
                    RadioButton selectedGenderButton = findViewById(selectedGenderId);
                    result += "Gender: " + selectedGenderButton.getText().toString() + "\n";
                } else {
                    result += "Gender: Not Selected\n";
                }

                // 2. Get Known Languages
                result += "Languages Known:";
                if (e.isChecked()) {
                    result += " " + e.getText().toString();
                }
                if (m.isChecked()) {
                    result += " " + m.getText().toString();
                }
                if (h.isChecked()) {
                    result += " " + h.getText().toString();
                }

                // Display combined result
                t.setText(result);

                Toast.makeText(
                        MainActivity.this,
                        "Registration Submitted",
                        Toast.LENGTH_SHORT
                ).show();
            }
        });
    }
}