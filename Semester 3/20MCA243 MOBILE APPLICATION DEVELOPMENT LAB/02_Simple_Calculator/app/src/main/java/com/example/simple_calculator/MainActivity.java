package com.example.simple_calculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText t1;
    Button b0, b1, b2, b3, b4, b5, b6, b7, b8, b9;
    Button b10, b11, b12, b13, b14, b15, b16, bac;

    String firstNumber = "";
    String operator = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        t1 = findViewById(R.id.t1);

        b0 = findViewById(R.id.b0);
        b1 = findViewById(R.id.b1);
        b2 = findViewById(R.id.b2);
        b3 = findViewById(R.id.b3);
        b4 = findViewById(R.id.b4);
        b5 = findViewById(R.id.b5);
        b6 = findViewById(R.id.b6);
        b7 = findViewById(R.id.b7);
        b8 = findViewById(R.id.b8);
        b9 = findViewById(R.id.b9);

        b10 = findViewById(R.id.b10); // .
        b11 = findViewById(R.id.b11); // backspace
        b12 = findViewById(R.id.b12); // +
        b13 = findViewById(R.id.b13); // -
        b14 = findViewById(R.id.b14); // x
        b15 = findViewById(R.id.b15); // /
        b16 = findViewById(R.id.b16); // =
        bac = findViewById(R.id.bac); // AC

        // Digits
        View.OnClickListener digitListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Button b = (Button) view;
                t1.append(b.getText().toString());
            }
        };

        b0.setOnClickListener(digitListener);
        b1.setOnClickListener(digitListener);
        b2.setOnClickListener(digitListener);
        b3.setOnClickListener(digitListener);
        b4.setOnClickListener(digitListener);
        b5.setOnClickListener(digitListener);
        b6.setOnClickListener(digitListener);
        b7.setOnClickListener(digitListener);
        b8.setOnClickListener(digitListener);
        b9.setOnClickListener(digitListener);

        // Decimal point
        b10.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String text = t1.getText().toString();
                if (!text.contains(".")) {
                    if (text.isEmpty()) {
                        t1.append("0.");
                    } else {
                        t1.append(".");
                    }
                }
            }
        });

        // Operators (+, -, x, /)
        View.OnClickListener opListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String currentText = t1.getText().toString().trim();
                if (!currentText.isEmpty()) {
                    firstNumber = currentText;
                    Button b = (Button) view;
                    operator = b.getText().toString();
                    t1.setText("");
                }
            }
        };

        b12.setOnClickListener(opListener);
        b13.setOnClickListener(opListener);
        b14.setOnClickListener(opListener);
        b15.setOnClickListener(opListener);

        // Backspace
        b11.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String text = t1.getText().toString();
                if (!text.isEmpty()) {
                    t1.setText(text.substring(0, text.length() - 1));
                }
            }
        });

        // All Clear (AC)
        bac.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                t1.setText("");
                firstNumber = "";
                operator = "";
            }
        });

        // Equals (=)
        b16.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String secondNumber = t1.getText().toString().trim();

                if (firstNumber.isEmpty() || secondNumber.isEmpty() || operator.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Enter numbers and operator", Toast.LENGTH_SHORT).show();
                    return;
                }

                try {
                    double num1 = Double.parseDouble(firstNumber);
                    double num2 = Double.parseDouble(secondNumber);
                    double result = 0;

                    if (operator.equals("+")) {
                        result = num1 + num2;
                    } else if (operator.equals("-")) {
                        result = num1 - num2;
                    } else if (operator.equals("x")) {
                        result = num1 * num2;
                    } else if (operator.equals("/")) {
                        if (num2 == 0) {
                            Toast.makeText(MainActivity.this, "Cannot divide by zero", Toast.LENGTH_SHORT).show();
                            return;
                        }
                        result = num1 / num2;
                    }

                    // Format nicely: display whole numbers without trailing .0
                    String resultStr;
                    if (result == (long) result) {
                        resultStr = String.valueOf((long) result);
                    } else {
                        resultStr = String.valueOf(result);
                    }

                    t1.setText(resultStr);
                    firstNumber = resultStr;
                    operator = "";
                } catch (NumberFormatException e) {
                    Toast.makeText(MainActivity.this, "Invalid number", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
