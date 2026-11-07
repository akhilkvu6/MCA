package com.example.integrated.app5.v5;

import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    Button btnWeb, btnMaps, btnCalc, btnProfile, btnExit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnWeb = findViewById(R.id.btnWeb);
        btnMaps = findViewById(R.id.btnMaps);
        btnCalc = findViewById(R.id.btnCalc);
        btnProfile = findViewById(R.id.btnProfile);
        btnExit = findViewById(R.id.btnExit);

        // Implicit Intent: CET Portal
        btnWeb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.cet.ac.in"));
                startActivity(i);
            }
        });

        // Implicit Intent: Campus Location
        btnMaps.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(Intent.ACTION_VIEW, Uri.parse("geo:8.5458,76.9063?q=College+of+Engineering+Trivandrum"));
                startActivity(i);
            }
        });

        // Explicit Intent: Integrated Calculator Utility
        btnCalc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this, CalculatorActivity.class);
                startActivity(i);
            }
        });

        // Explicit Intent: Profile Details
        btnProfile.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this, ProfileDetailsActivity.class);
                i.putExtra("DEPT", "Computer Applications (MCA)");
                startActivity(i);
            }
        });

        // AlertDialog on Exit
        btnExit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new AlertDialog.Builder(MainActivity.this)
                        .setTitle("Exit Portal")
                        .setMessage("Are you sure you want to exit the application?")
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                finish();
                            }
                        })
                        .setNegativeButton("No", null)
                        .show();
            }
        });
    }
}