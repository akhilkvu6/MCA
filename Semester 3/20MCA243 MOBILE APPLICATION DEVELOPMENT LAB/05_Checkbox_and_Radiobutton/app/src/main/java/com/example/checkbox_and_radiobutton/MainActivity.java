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

        // Gender Toast
        rg.setOnCheckedChangeListener(
                new RadioGroup.OnCheckedChangeListener() {

                    @Override
                    public void onCheckedChanged(
                            RadioGroup group,
                            int checkedId) {

                        if (checkedId == R.id.male) {

                            Toast.makeText(
                                    MainActivity.this,
                                    "Male",
                                    Toast.LENGTH_SHORT
                            ).show();

                        } else if (checkedId == R.id.female) {

                            Toast.makeText(
                                    MainActivity.this,
                                    "Female",
                                    Toast.LENGTH_SHORT
                            ).show();
                        }
                    }
                }
        );

        // Submit Button
        b1.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {

                t.setText("Languages Known:");

                if (e.isChecked()) {
                    t.setText(
                            t.getText().toString()
                                    + " " + e.getText()
                    );
                }

                if (m.isChecked()) {
                    t.setText(
                            t.getText().toString()
                                    + " " + m.getText()
                    );
                }

                if (h.isChecked()) {
                    t.setText(
                            t.getText().toString()
                                    + " " + h.getText()
                    );
                }

                Toast.makeText(
                        MainActivity.this,
                        "Registration Submitted",
                        Toast.LENGTH_SHORT
                ).show();
            }
        });
    }
}